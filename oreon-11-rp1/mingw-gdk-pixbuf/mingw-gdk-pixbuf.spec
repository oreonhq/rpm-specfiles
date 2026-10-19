%global source0_hash 919f529512961a12e81cd4b4b466a48c3933469e7f9a310c6513cd4fb252ba3c
%{?mingw_package_header}
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-gdk-pixbuf
Version:        2.44.8
Release:        1%{?dist}
Summary:        MinGW Windows GDK Pixbuf library
License:        LGPL-2.0-or-later
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdk-pixbuf/%{release_version}/gdk-pixbuf-%{version}.tar.xz
Source1:        gdk-pixbuf.loaders
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libtiff
BuildRequires:  pkg-config
# /oreon:deps
%description
MinGW Windows GDK Pixbuf library.

%package -n mingw32-gdk-pixbuf
Summary:        MinGW Windows GDK Pixbuf library
%description -n mingw32-gdk-pixbuf
MinGW Windows GDK Pixbuf library.

%package -n mingw64-gdk-pixbuf
Summary:        MinGW Windows GDK Pixbuf library
%description -n mingw64-gdk-pixbuf
MinGW Windows GDK Pixbuf library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gdk-pixbuf-%{version}
%oreon_prep
%build

%mingw_meson \
  -Drelocatable=true \
  -Dbuiltin_loaders=bmp,gif,ico,jpeg,tiff,png \
  -Dman=false \
  -Ddocumentation=false \
  -Dothers=enabled
install -m 0644 %{SOURCE1} build_win32/gdk-pixbuf/loaders.cache
install -m 0644 %{SOURCE1} build_win64/gdk-pixbuf/loaders.cache
%mingw_ninja
%install
%mingw_ninja_install
rm -f %{buildroot}%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.dll.a
install -m 0644 %{SOURCE1} %{buildroot}%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
install -m 0644 %{SOURCE1} %{buildroot}%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%mingw_find_lang %{name} --all-name
%oreon_autofiles mingw32-gdk-pixbuf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gdk-pixbuf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gdk-pixbuf -f %{oreon_filedir}/mingw32-gdk-pixbuf.list
%files -n mingw64-gdk-pixbuf -f %{oreon_filedir}/mingw64-gdk-pixbuf.list

%changelog

%autochangelog
