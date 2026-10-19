%global source0_hash 1198a91cdbdcfb232df94e71ef5427617d26029e327be3f860c3b0921c448118
%global enable_debugging 0
Name: gnome-menus
Version: 3.38.1
Release:        2%{?dist}
Summary:        A menu system for the GNOME project
License: LGPL-2.0-or-later
URL: https://gitlab.gnome.org/GNOME/gnome-menus
Source0:        https://download.gnome.org/sources/gnome-menus/3.38/%{name}-%{version}.tar.xz
Patch0: 14.patch
Requires:  redhat-menus
# oreon:deps
BuildRequires:  gawk
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
gnome-menus is an implementation of the draft "Desktop
Menu Specification" from freedesktop.org. This package
also contains the GNOME menu layout configuration files,
.directory files and assorted menu related utility programs
and a simple menu editor.

%package devel
Summary: Libraries and include files for the GNOME menu system
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the necessary development libraries for
writing applications that use the GNOME menu system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1

%build

%configure --disable-static \
   --enable-introspection \
   --enable-debug=no
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang gnome-menus
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-menus-devel -f %{oreon_filedir}/gnome-menus-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.38.1-2
- Prepare for Oreon 11 (RP1)
