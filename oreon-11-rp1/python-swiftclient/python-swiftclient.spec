%global source102_hash 092dedd605ba6d36cff81167851c71b98bbbf235123c01295ddaf6022fb8ba5c
%global source101_hash 87fe3b026e95ff97282588e44dc23daf62c645b57ad9970d73b6f0852b1761fb
%global source0_hash d4d18540413893fc16ad87791d740f823f763435e8212e68eb53d60da2638233
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%global with_doc 1
%global sname swiftclient
%global common_desc \
Client library and command line utility for interacting with Openstack \
Object Storage API.
Name:       python-swiftclient
Version:    4.6.0
Release:        6%{?dist}
Summary:        Client Library for OpenStack Object Storage API
License:    Apache-2.0
URL:        http://launchpad.net/python-swiftclient/
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:  noarch
%if 0%{?sources_gpg} == 1
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-swiftclient = %{version}-%{release}
# /oreon:deps
%description
%{common_desc}

%package -n python3-%{sname}
Summary:    Client Library for OpenStack Object Storage API
Requires:  python3-%{sname}+keystone = %{version}-%{release}
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:    Documentation for OpenStack Object Storage API Client
Group:      Documentation
%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.
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
sed -i /.*keystone]/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%build

%pyproject_wheel
%install
%pyproject_install
ln -s swift %{buildroot}%{_bindir}/swift-3
rm -fr %{buildroot}%{python3_sitelib}/swiftclient/tests
%if 0%{?with_doc}
export LANG=en_US.utf-8
export LC_ALL=C
export LANGUAGE=en_US:en
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}
sphinx-build -W -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main usr/lib/python3*/site-packages/swiftclient* usr/lib64/python3*/site-packages/swiftclient* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files
%files -n python3-swiftclient -f %{oreon_filedir}/python3-swiftclient.list
%files -n python-swiftclient-doc -f %{oreon_filedir}/python-swiftclient-doc.list

%changelog

%autochangelog
