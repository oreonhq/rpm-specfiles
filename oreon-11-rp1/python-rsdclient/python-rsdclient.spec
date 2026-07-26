%global source0_hash 0213cb70fe4880d4a931bf13eb8a1f65347d5d812c75832de1c1b8e83e8832f7

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global sname rsdclient
%global pyname python_rsdclient

Name:           python-%{sname}
Version:        1.0.2
Release:        23%{?dist}
Summary:        OpenStack client plugin for Rack Scale Design

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://git.openstack.org/cgit/openstack/%{name}
Source0:        http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a client for the RSD Pod Manager API, which is based on OpenStack
client framework. It provides a Python API (rsdclient/v1 module) and a RSD
specific plugin for OpenStack client (rsdclient/osc).

%package -n     python3-%{sname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-oslotest >= 1.10.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-testrepository >= 0.0.18
BuildRequires:  python3-testtools >= 1.4.0

Requires:       python3-six >= 1.10.0
Requires:       python3-osc-lib >= 1.7.0
Requires:       python3-pbr >= 2.0
Requires:       python3-rsd-lib >= 1.2.0
%description -n python3-%{sname}
This is a client for the RSD Pod Manager API, which is based on OpenStack
client framework. It provides a Python API (rsdclient/v1 module) and a RSD
specific plugin for OpenStack client (rsdclient/osc).

%package -n python3-%{sname}-tests
Summary: python-rsdclient tests
Requires: python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
Tests for python-rsdclient

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: python-rsdclient documentation
BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme >= 1.11.0

%description -n python-%{sname}-doc
Documentation for python-rsdclient
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{upstream_version} -S git

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/%{pyname}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{pyname}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{pyname}

%files -n python3-%{sname}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{pyname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
%autochangelog
