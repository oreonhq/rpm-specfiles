%global source0_hash 4fbd26b4af24c9787d84cf5448e34eb8dca064b732479aaecd03109520eebd5f
Name: pycairo
Version: 1.29.1
Release:        1%{?dist}
Summary:        Python bindings for the cairo library
License: LGPL-2.1-only OR MPL-1.1
URL: https://www.cairographics.org/pycairo
Source0:        https://github.com/pygobject/pycairo/releases/download/v%{version}/pycairo-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# /oreon:deps
%description
Python bindings for the cairo library.

%package -n python3-cairo
Summary: Python 3 bindings for the cairo library
%{?python_provide:%python_provide python3-cairo}
%description -n python3-cairo
Python 3 bindings for the cairo library.

%package -n python3-cairo-devel
Summary: Libraries and headers for py3cairo
Requires: python3-cairo%{?_isa} = %{version}-%{release}
Requires: python3-devel
%description -n python3-cairo-devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with py3cairo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles python3-cairo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-cairo-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n python3-cairo -f %{oreon_filedir}/python3-cairo.list
%files -n python3-cairo-devel -f %{oreon_filedir}/python3-cairo-devel.list

%changelog

%autochangelog
