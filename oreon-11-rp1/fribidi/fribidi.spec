%global source0_hash 6949dcde27d41cebad1fd741fcafc36d55a1020d2d872d4a6eb3914caabbada2
Summary:        Library implementing the Unicode Bidirectional Algorithm
Name: fribidi
Version: 1.0.17
Release:        1%{?dist}
URL: https://github.com/fribidi/fribidi/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
License: LGPL-2.1-or-later AND Unicode-DFS-2016
Patch0: fribidi-drop-bundled-gnulib.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  meson
# /oreon:deps
%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%package devel
Summary: Libraries and include files for FriBidi
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Include files and libraries needed for developing applications which use
FriBidi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# Clean up older file in archive
(cd lib;
 rm arabic-shaping.tab.i bidi-type.tab.i brackets*.tab.i joining-type.tab.i mirroring.tab.i fribidi-unicode-version.h
)

%build

%meson -Ddocs=false
%meson_build
%check

%meson_test
%install
%meson_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fribidi-devel -f %{oreon_filedir}/fribidi-devel.list

%changelog

%autochangelog
