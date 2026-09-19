%global source0_hash ede6a52d8945aa8cc4fb231124bc2e5650bc9d272a7e17558c34d2a9cfa00754

%global srcname colcon-lcov-result

Name:           python-%{srcname}
Version:        0.5.3
Release:        7%{?dist}
Summary:        Extension for colcon to provide test results using LCOV

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to provide aggregate coverage results using LCOV.

LCOV is a graphical front-end for GCC's coverage testing tool gcov, producing
the following coverage metrics:
- Statement coverage
- Function coverage
- Branch coverage

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.5.6
%endif

Recommends:     binutils
Recommends:     gcc
Recommends:     lcov

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide aggregate coverage results using LCOV.

LCOV is a graphical front-end for GCC's coverage testing tool gcov, producing
the following coverage metrics:
- Statement coverage
- Function coverage
- Branch coverage

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_lcov_result/
%{python3_sitelib}/colcon_lcov_result-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
