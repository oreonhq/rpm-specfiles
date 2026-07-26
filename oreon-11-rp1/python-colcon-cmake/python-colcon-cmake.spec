%global source0_hash b51f2de876703c665d0a0f196e4019effdc39bc6a6e44d00ba25e9afdc3d658d

%global srcname colcon-cmake

Name:           python-%{srcname}
Version:        0.2.29
Release:        6%{?dist}
Summary:        Extension for colcon to support CMake packages

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to support CMake projects.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  cmake
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.5.6
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
Recommends:     cmake
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.5.6
Requires:       python%{python3_pkgversion}-colcon-library-path
Requires:       python%{python3_pkgversion}-colcon-test-result >= 0.3.3
Requires:       python%{python3_pkgversion}-packaging
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support CMake projects.

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
%{python3_sitelib}/colcon_cmake/
%{python3_sitelib}/colcon_cmake-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
