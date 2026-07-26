%global source0_hash 7255f0ae1213d34a3bdb1081830ab25afb9b263250875e3e61e46ba586adaeba

%global srcname etcd3gw

%if 0%{?fedora} && 0%{?fedora} < 30
%bcond_without python2
%bcond_without python3
%else
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif
%endif

Name:           python-%{srcname}
Version:        2.5.0
Release:        2%{?dist}
Summary:        An etcd3 gateway Python client

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

%description
A python client for etcd3 grpc-gateway v3alpha API

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel

BuildRequires:  python2-futurist
BuildRequires:  python2-oslotest
BuildRequires:  python2-pytest
BuildRequires:  python2-requests

Requires:  python2-futurist
Requires:  python2-pbr
Requires:  python2-requests
Requires:  python2-six

%description -n python2-%{srcname}
A python client for etcd3 grpc-gateway v3alpha API
%endif

%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

BuildRequires:  python3-futurist
BuildRequires:  python3-oslotest
BuildRequires:  python3-pytest
BuildRequires:  python3-requests

Requires: python3-futurist
Requires: python3-pbr
Requires: python3-requests
Requires: python3-six

%description -n python3-%{srcname}
A python client for etcd3 grpc-gateway v3alpha API
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Let's manage dependencies using rpm deps.
rm -f *requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%pyproject_wheel
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%pyproject_install
%pyproject_save_files -l %{srcname}
%endif

%check
%pyproject_check_import

%if %{with python2}
export PYTHON=%{__python2}
py.test
%endif

%if %{with python3}
export PYTHON=%{__python3}
# workaround for https://bugs.launchpad.net/testrepository/+bug/1229445
rm -rf .testrepository/times.dbm
py.test-3
%endif

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md CONTRIBUTING.rst HACKING.rst
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%if %{with python3}
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CONTRIBUTING.rst HACKING.rst
%endif

%changelog
%autochangelog
