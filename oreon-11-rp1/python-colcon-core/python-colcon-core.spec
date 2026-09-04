%global source0_hash d716a01b585d00f1a87cbd2c37be06af5df2828d96566e0d3b01acfd2613f57f

%global srcname colcon-core

Name:           python-%{srcname}
Version:        0.21.1
Release:        1%{?dist}
Summary:        Command line tool to build sets of software packages

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Not submitted upstream - make pytest dependency weak
Patch0:         %{name}-0.5.3-remove-pytest.patch
# Not submitted upstream - compatibility with pytest 2.9.X
Patch1:         %{name}-0.19.0-pytest-compat.patch

BuildArch:      noarch

%description
colcon is a command line tool to improve the workflow of building, testing and
using multiple software packages. It automates the process, handles the ordering
and sets up the environment to use the packages.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  (python%{python3_pkgversion} >= 3.8 or python%{python3_pkgversion}-importlib-metadata)
BuildRequires:  (python%{python3_pkgversion} >= 3.11 or python%{python3_pkgversion}-tomli >= 1)
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-distlib >= 0.2.5
BuildRequires:  python%{python3_pkgversion}-empy
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
BuildRequires:  python%{python3_pkgversion}-setuptools < 80
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       (python%{python3_pkgversion} >= 3.8 or python%{python3_pkgversion}-importlib-metadata)
Requires:       (python%{python3_pkgversion} >= 3.11 or python%{python3_pkgversion}-tomli >= 1)
Requires:       python%{python3_pkgversion}-distlib >= 0.2.5
Requires:       python%{python3_pkgversion}-empy
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-setuptools < 80
%endif

Recommends:     python%{python3_pkgversion}-coloredlogs
Recommends:     python%{python3_pkgversion}-pytest
Recommends:     python%{python3_pkgversion}-pytest-cov
Recommends:     python%{python3_pkgversion}-pytest-repeat
Recommends:     python%{python3_pkgversion}-pytest-rerunfailures
Recommends:     python%{python3_pkgversion}-pytest-runner

%description -n python%{python3_pkgversion}-%{srcname}
colcon is a command line tool to improve the workflow of building, testing and
using multiple software packages. It automates the process, handles the ordering
and sets up the environment to use the packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -m 'not linter' test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon/
%{python3_sitelib}/colcon_core/
%{python3_sitelib}/colcon_core-%{version}-py%{python3_version}.egg-info/
%{_bindir}/colcon

%changelog
%autochangelog
