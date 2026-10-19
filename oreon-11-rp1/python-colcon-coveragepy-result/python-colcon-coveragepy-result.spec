%global source0_hash 3a589bff788aaa3898e3c7a39c2b8e6dced12e5c1d66b0568d2384e3a0643f0e
%global srcname colcon-coveragepy-result
Name:           python-%{srcname}
Version:        0.0.8
Release:        1%{?dist}
Summary:        Extension for colcon to collect coverage.py results
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
A colcon extension for collecting coverage.py results.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extension for colcon to collect coverage.py results
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
Requires:       python%{python3_pkgversion}-coverage
%endif
%description -n python%{python3_pkgversion}-%{srcname}
A colcon extension for collecting coverage.py results.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test
%files -f %{oreon_filedir}/main.list
%files -n python3-colcon-coveragepy-result -f %{oreon_filedir}/python3-colcon-coveragepy-result.list

%changelog

%autochangelog
