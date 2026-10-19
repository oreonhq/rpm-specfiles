%global source0_hash 6948297878f17dd1f8fd94feb1451202977b68275ea9bcfe55a00125a2f70edf
%global srcname colcon-library-path
Name:           python-%{srcname}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Extension for colcon adding an environment variable to find libraries
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
An extension for colcon-core to set an environment variable to find shared
libraries at runtime.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extension for colcon adding an environment variable to find libraries
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
%endif # __pythondist_requires
%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to set an environment variable to find shared
libraries at runtime.

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
%files -n python3-colcon-library-path -f %{oreon_filedir}/python3-colcon-library-path.list

%changelog

%autochangelog
