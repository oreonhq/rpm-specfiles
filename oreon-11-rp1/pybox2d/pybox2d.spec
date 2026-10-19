%global source0_hash 5471722f290b7285dcbdee9bef61d1cb424e5a610fa6e19e9ddeb854c7e3b937
Name:           pybox2d
Version:        2.3.10
Release:        1%{?dist}
Summary:        A 2D rigid body simulation library for Python
License:        zlib
URL:            https://github.com/pybox2d/%{name}
Source0:        https://github.com/pybox2d/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		replace-deprecated-swigconstant.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pybox2d = %{version}-%{release}
# /oreon:deps
%description
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation.

%package -n python3-%{name}
Summary:        A 2D rigid body simulation library for Python
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation.

This package provides the Python 3 build of %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pybox2d* usr/lib64/python3*/site-packages/pybox2d* usr/bin/*

%files
%files -n python3-pybox2d -f %{oreon_filedir}/python3-pybox2d.list

%changelog

%autochangelog
