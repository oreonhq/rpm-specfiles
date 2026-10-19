%global source0_hash 960a3dff0ded859c7c170da4273b6a16ba31000052d7ca1cb921002ecceb7ab1
%global srcname colcon-recursive-crawl
Name:           python-%{srcname}
Version:        0.2.3
Release:        1%{?dist}
Summary:        Extension for colcon to recursively crawl for packages
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
An extension for colcon-core to recursively crawl for packages.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extension for colcon to recursively crawl for packages
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.7.0
%endif
%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to recursively crawl for packages.

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
%files -n python3-colcon-recursive-crawl -f %{oreon_filedir}/python3-colcon-recursive-crawl.list

%changelog

%autochangelog
