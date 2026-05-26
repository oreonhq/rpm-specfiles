# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 1198a91cdbdcfb232df94e71ef5427617d26029e327be3f860c3b0921c448118
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global enable_debugging 0

Name: gnome-menus
Version: 3.38.1
Release: 2%{?dist}
Summary:  A menu system for the GNOME project

License: LGPL-2.0-or-later
URL: https://gitlab.gnome.org/GNOME/gnome-menus
Source0: https://download.gnome.org/sources/gnome-menus/3.38/%{name}-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gnome-menus/merge_requests/14
# Puts eog back to the Utilities submenu
Patch0: 14.patch

BuildRequires: gawk
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: pkgconfig
BuildRequires: gobject-introspection-devel
BuildRequires: make

%if %{defined rhel}
Obsoletes: redhat-menus < 12.0.2-24
Provides:  redhat-menus = 12.0.2-24
Conflicts: redhat-menus < 12.0.2-24
%else
Requires:  redhat-menus
%endif

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
%oreon_verify_sources
%setup -q
%patch -P0 -p1

%build
%configure --disable-static \
   --enable-introspection \
%if %{enable_debugging}
   --enable-debug=yes
%else
   --enable-debug=no
%endif

%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%if %{defined rhel}
cp $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/{gnome-,}applications.menu
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
%endif

%find_lang gnome-menus

%ldconfig_scriptlets

%files -f gnome-menus.lang
%license COPYING.LIB
%doc AUTHORS NEWS
%{_sysconfdir}/xdg/menus/gnome-applications.menu
%if %{defined rhel}
%{_sysconfdir}/xdg/menus/applications.menu
%dir %{_sysconfdir}/xdg/menus/applications-merged
%endif
%{_libdir}/lib*.so.*
%{_datadir}/desktop-directories/*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GMenu-3.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/gnome-menus-3.0
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GMenu-3.0.gir

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.38.1-2
- Prepare for Oreon 11 (RP1)
