%global source0_hash 28ba4ac1c04f86eac09b79a163cb163a4c2b54442d9f7eccc04679062a581044
%{?mingw_package_header}
%global bin_version 3.0.0
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-gtk3
Version:        4.24.0
Release:        1%{?dist}
Summary:        MinGW Windows GTK+ library
License:        LGPL-2.0-or-later
URL:            http://www.gtk.org
Source0:        https://download.gnome.org/sources/gtk/%{release_version}/gtk-%{version}.tar.xz
Source1:        gtk.immodules
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson
BuildRequires:  mingw32-atk
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-atk
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  ninja-build
BuildRequires:  perl-interpreter
# /oreon:deps
%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%package -n mingw32-gtk3
Summary:        MinGW Windows GTK+ library
Requires:       mingw32-adwaita-icon-theme
Requires:       mingw32-gtk-update-icon-cache
%description -n mingw32-gtk3
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%package -n mingw32-gtk-update-icon-cache
Summary: Icon theme caching utility
%description -n mingw32-gtk-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.

%package -n mingw64-gtk3
Summary:        MinGW Windows GTK+ library
Requires:       mingw64-adwaita-icon-theme
Requires:       mingw64-gtk-update-icon-cache
%description -n mingw64-gtk3
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%package -n mingw64-gtk-update-icon-cache
Summary: Icon theme caching utility
%description -n mingw64-gtk-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtk-%{version}
%oreon_prep
%build

%mingw_meson -Dintrospection=false -Dbuiltin_immodules=no
%mingw_ninja
%install
%mingw_ninja_install
rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc
rm -f %{buildroot}%{mingw32_libdir}/*.def
rm -f %{buildroot}%{mingw64_libdir}/*.def
rm -f %{buildroot}%{mingw32_bindir}/libgtkreftestprivate-0.dll
rm -f %{buildroot}%{mingw64_bindir}/libgtkreftestprivate-0.dll
rm -f %{buildroot}%{mingw32_libdir}/libgtkreftestprivate.dll.a
rm -f %{buildroot}%{mingw64_libdir}/libgtkreftestprivate.dll.a
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
rm -f %{buildroot}%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.dll.a
rm -f %{buildroot}%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/*.la
rm -f %{buildroot}%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.la
rm -f %{buildroot}%{mingw32_datadir}/applications/*.desktop
rm -f %{buildroot}%{mingw64_datadir}/applications/*.desktop
rm -f %{buildroot}%{mingw32_datadir}/icons/hicolor/*/apps/*.png
rm -f %{buildroot}%{mingw64_datadir}/icons/hicolor/*/apps/*.png
mkdir -p %{buildroot}%{mingw32_sysconfdir}/gtk-3.0/
mkdir -p %{buildroot}%{mingw64_sysconfdir}/gtk-3.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw32_sysconfdir}/gtk-3.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw64_sysconfdir}/gtk-3.0/
%mingw_find_lang %{name} --all-name
%oreon_autofiles mingw32-gtk3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-gtk-update-icon-cache usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gtk3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gtk-update-icon-cache usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%postun -n mingw32-gtk3

if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :
fi
%posttrans -n mingw32-gtk3

/usr/bin/glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :
%postun -n mingw64-gtk3

if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :
fi
%posttrans -n mingw64-gtk3

/usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n mingw32-gtk3 -f %{oreon_filedir}/mingw32-gtk3.list
%files -n mingw32-gtk-update-icon-cache -f %{oreon_filedir}/mingw32-gtk-update-icon-cache.list
%files -n mingw64-gtk3 -f %{oreon_filedir}/mingw64-gtk3.list
%files -n mingw64-gtk-update-icon-cache -f %{oreon_filedir}/mingw64-gtk-update-icon-cache.list

%changelog

%autochangelog
