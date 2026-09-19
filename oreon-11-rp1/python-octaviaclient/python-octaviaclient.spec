%global source0_hash c2b621098de0a9c92548af256a9b2016adb9622ddac041a06ab5b66bb5b590ee

%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order pylint
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%global with_doc 1

%global pypi_name octaviaclient

%global common_desc \
Client for OpenStack Octavia (Load Balancer as a Service)

Name:           python-%{pypi_name}
Version:        3.8.0
Release:        6%{?dist}
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)

License:        Apache-2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n     python3-%{pypi_name}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-osc-lib-tests

Summary:        Client for OpenStack Octavia (Load Balancer as a Service)

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for OpenStack Octavia Client

BuildRequires:  python3-sphinxcontrib-rsvgconverter

%description -n python-%{pypi_name}-doc
Documentation for the client library for interacting with Openstack
Octavia API.
%endif

# Test package
%package -n python3-%{pypi_name}-tests
Summary:        OpenStack Octavia client tests

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-fixtures >= 1.3.1
Requires:       python3-mock
Requires:       python3-testtools
Requires:       python3-subunit >= 0.0.18
Requires:       python3-osc-lib >= 1.14.1
Requires:       python3-osc-lib-tests
Requires:       python3-oslo-log
Requires:       python3-openstackclient
Requires:       python3-stestr
Requires:       python3-webob >= 1.2.3

%description -n python3-%{pypi_name}-tests
OpenStack Octavia client tests

This package contains the example client test files.

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

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
rm -f ./octaviaclient/tests/unit/test_hacking.py
%tox -e %{default_toxenv}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_%{pypi_name}-*.dist-info
%exclude %{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/%{pypi_name}/tests

%changelog
%autochangelog
