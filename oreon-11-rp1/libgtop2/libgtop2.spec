%global source0_hash 775676df958e2ea2452f7568f28b2ea581063d312773dd5c0b7624c1b9b2da8c
Name:           libgtop2
Version:        2.41.3
Release:        1%{?dist}
Summary:        LibGTop library (version 2)
License:        GPL-2.0-or-later
URL:            https://download.gnome.org/sources/libgtop
Source0:        https://download.gnome.org/sources/libgtop/2.41/libgtop-%{version}.tar.xz
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# /oreon:deps
%description
LibGTop is a library for portably obtaining information about processes,
such as their PID, memory usage, etc.

%package        devel
Summary:        Libraries and include files for developing with libgtop
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package provides the necessary development libraries and include
files to allow you to develop with LibGTop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libgtop-%{version}
%oreon_prep
%build

%configure --disable-gtk-doc --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -print -delete
%find_lang libgtop
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgtop2-devel -f %{oreon_filedir}/libgtop2-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.41.3-5
- Prepare for Oreon 11 (RP1)
