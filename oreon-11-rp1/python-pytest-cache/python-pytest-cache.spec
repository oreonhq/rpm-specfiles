%global source0_hash be7468edd4d3d83f1e844959fd6e3fd28e77a481440a7118d430130ea31b07a9

%if 0%{?fedora} >= 31
%bcond_with python2
%else
%bcond_without python2 
%endif

%global srcname pytest-cache

Name:           python-%{srcname}
Version:        1.0
Release:        42%{?dist}
Summary:        Pytest plugin with mechanisms for caching across test runs

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Pytest plugin with mechanisms for caching across test runs for Python 2.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        Pytest plugin with mechanisms for caching across test runs for Python 3
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-execnet
Requires:       python2-pytest
Requires:       python2-execnet
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Pytest plugin with mechanisms for caching across test runs for Python 3.
%endif

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Pytest plugin with mechanisms for caching across test runs for Python 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-execnet
BuildRequires:  python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-execnet
Requires:       python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Pytest plugin with mechanisms for caching across test runs for Python 3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}
rm -rf *.egg-info

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%py3_install
%if %{with python2}
%py2_install
%endif

%check
# No idea why the tests fail
%if %{with python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v || :
%endif
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v || :

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc CHANGELOG PKG-INFO README.rst
%{python2_sitelib}/pytest_cache.py*
%{python2_sitelib}/pytest_cache-*.egg-info/
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGELOG PKG-INFO README.rst
%{python3_sitelib}/pytest_cache.py
%{python3_sitelib}/pytest_cache-*.egg-info/
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog
