%global source102_hash 092dedd605ba6d36cff81167851c71b98bbbf235123c01295ddaf6022fb8ba5c
%global source101_hash 271082d4c831f44763580cd3c6ed1cf8faf8483722e77430ff1b459c387b71e5
%global source0_hash c19452ef12da3c484b69d22a888ce7a74910bdb8783bbe91248c60efa5378810
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global sname glanceclient
%global with_doc 1
%global with_functional_tests 0
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order tempest
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%if ! 0%{?with_functional_tests}
%global excluded_brs %{excluded_brs} os-client-config
%endif
%global common_desc \
This is a client for the OpenStack Glance API. There's a Python API (the \
glanceclient module), and a command-line script (glance). Each implements \
100% of the OpenStack Glance API.
Name:             python-glanceclient
Epoch:            1
Version:          4.7.0
Release:        6%{?dist}
Summary:        Python API and CLI for OpenStack Glance
License:          Apache-2.0
URL:              https://launchpad.net/python-glanceclient
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:        noarch
%if 0%{?sources_gpg} == 1
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-glanceclient = %{version}-%{release}
# /oreon:deps
%description
%{common_desc}

%package -n python3-%{sname}
Summary:          Python API and CLI for OpenStack Glance
BuildRequires:    python3-devel
BuildRequires:    pyproject-rpm-macros
%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Glance API Client
%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Wipe functional tests if they're disabled
%if ! 0%{?with_functional_tests}
rm -rf glanceclient/tests/functional
%endif

# Automatic BR generation
%build

%pyproject_wheel
%install
%pyproject_install
ln -s glance %{buildroot}%{_bindir}/glance-3
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/glance.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/glance
rm -fr %{buildroot}%{python3_sitelib}/glanceclient/tests
%if 0%{?with_doc}
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}
sphinx-build -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/glance.1 %{buildroot}%{_mandir}/man1/glance.1
%oreon_autofiles main usr/lib/python3*/site-packages/glanceclient* usr/lib64/python3*/site-packages/glanceclient* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

unset http_proxy
unset https_proxy
%tox -e %{default_toxenv} -- -- --exclude-regex '(glanceclient.tests.unit.test_ssl.TestHTTPSVerifyCert*|.*test_cache_schemas_gets_when_not_exists|.*test_cache_schemas_gets_when_forced)|.*test_http_chunked_response|.*test_log_request_id_once'
%files
%files -n python3-glanceclient -f %{oreon_filedir}/python3-glanceclient.list
%files -n python-glanceclient-doc -f %{oreon_filedir}/python-glanceclient-doc.list

%changelog

%autochangelog
