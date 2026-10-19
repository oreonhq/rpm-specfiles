%global source0_hash 28ba4ac1c04f86eac09b79a163cb163a4c2b54442d9f7eccc04679062a581044
%{?mingw_package_header}
%global bin_version 4.0.0
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-gtk4
Version:        4.24.0
Release:        1%{?dist}
Summary:        MinGW Windows GTK+ library
License:        LGPLv2+
URL:            http://www.gtk.org
Source0:        https://download.gnome.org/sources/gtk/%{release_version}/gtk-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-graphene
BuildRequires:  mingw32-gstreamer1-plugins-bad-free
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-graphene
BuildRequires:  mingw64-gstreamer1-plugins-bad-free
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  ninja-build
# /oreon:deps
%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.

%package -n mingw32-gtk4
Summary:        MinGW Windows GTK+ library
Requires:       mingw32-adwaita-icon-theme
Requires:       mingw32-gtk4-update-icon-cache
%description -n mingw32-gtk4
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.

%package -n mingw32-gtk4-update-icon-cache
Summary: Icon theme caching utility
%description -n mingw32-gtk4-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.

%package -n mingw64-gtk4
Summary:        MinGW Windows GTK+ library
Requires:       mingw64-adwaita-icon-theme
Requires:       mingw64-gtk4-update-icon-cache
%description -n mingw64-gtk4
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.

%package -n mingw64-gtk4-update-icon-cache
Summary: Icon theme caching utility
%description -n mingw64-gtk4-update-icon-cache
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

%mingw_meson -Dintrospection=disabled -Dvulkan=disabled
%mingw_ninja
%install
%mingw_ninja_install
rm -f %{buildroot}%{mingw32_datadir}/applications/*.desktop
rm -f %{buildroot}%{mingw64_datadir}/applications/*.desktop
rm -rf %{buildroot}%{mingw32_datadir}/icons/
rm -rf %{buildroot}%{mingw64_datadir}/icons/
rm -rf %{buildroot}%{mingw32_datadir}/metainfo/
rm -rf %{buildroot}%{mingw64_datadir}/metainfo/
rm -rf %{buildroot}%{mingw32_datadir}/bash-completion/
rm -rf %{buildroot}%{mingw64_datadir}/bash-completion/
%mingw_find_lang %{name} --all-name
%oreon_autofiles mingw32-gtk4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-gtk4-update-icon-cache usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gtk4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gtk4-update-icon-cache usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gtk4 -f %{oreon_filedir}/mingw32-gtk4.list
%files -n mingw32-gtk4-update-icon-cache -f %{oreon_filedir}/mingw32-gtk4-update-icon-cache.list
%files -n mingw64-gtk4 -f %{oreon_filedir}/mingw64-gtk4.list
%files -n mingw64-gtk4-update-icon-cache -f %{oreon_filedir}/mingw64-gtk4-update-icon-cache.list

%changelog

%autochangelog
