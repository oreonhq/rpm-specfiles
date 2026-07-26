%global source0_hash 69b93e09139b80c0ee661503d60deb5a5874a31772b5184b9cd5462a4100ab68

%{?mingw_package_header}

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-gdk-pixbuf
Version:        2.44.5
Release:        1%{?dist}
Summary:        MinGW Windows GDK Pixbuf library

License:        LGPL-2.0-or-later
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdk-pixbuf/%{release_version}/gdk-pixbuf-%{version}.tar.xz

# If you want to rebuild this, do:
# wine /usr/i686-w64-mingw32/sys-root/mingw/bin/gdk-pixbuf-query-loaders.exe | sed s@'Z:/usr/i686-w64-mingw32/sys-root/mingw'@'..'@ > gdk-pixbuf.loaders
Source1:        gdk-pixbuf.loaders

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff

BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkg-config
# For glib-compile-resources
BuildRequires:  glib2-devel

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

%autosetup -p1 -n gdk-pixbuf-%{version}

%build
%mingw_meson \
  -Drelocatable=true \
  -Dbuiltin_loaders=bmp,gif,ico,jpeg,tiff,png \
  -Dman=false \
  -Ddocumentation=false \
  -Dothers=enabled

# Copy the loaders.cache file to the source tree
install -m 0644 %{SOURCE1} build_win32/gdk-pixbuf/loaders.cache
install -m 0644 %{SOURCE1} build_win64/gdk-pixbuf/loaders.cache

%mingw_ninja

%install
%mingw_ninja_install

# The .dll.a files are import libraries, but as the regular .dll's are
# only dlopen'ed by GTK they provide no additional value so they can be dropped
rm -f %{buildroot}%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.dll.a

# Install the loaders.cache file
install -m 0644 %{SOURCE1} %{buildroot}%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
install -m 0644 %{SOURCE1} %{buildroot}%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache

%mingw_find_lang %{name} --all-name

%files -n mingw32-gdk-pixbuf -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/gdk-pixbuf-csource.exe
%{mingw32_bindir}/gdk-pixbuf-pixdata.exe
%{mingw32_bindir}/gdk-pixbuf-query-loaders.exe
%{mingw32_bindir}/libgdk_pixbuf-2.0-0.dll
%dir %{mingw32_libdir}/gdk-pixbuf-2.0
%dir %{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.dll
%{mingw32_libdir}/libgdk_pixbuf-2.0.dll.a
%{mingw32_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{mingw32_includedir}/gdk-pixbuf-2.0/

%files -n mingw64-gdk-pixbuf -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/gdk-pixbuf-csource.exe
%{mingw64_bindir}/gdk-pixbuf-pixdata.exe
%{mingw64_bindir}/gdk-pixbuf-query-loaders.exe
%{mingw64_bindir}/libgdk_pixbuf-2.0-0.dll
%dir %{mingw64_libdir}/gdk-pixbuf-2.0
%dir %{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.dll
%{mingw64_libdir}/libgdk_pixbuf-2.0.dll.a
%{mingw64_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{mingw64_includedir}/gdk-pixbuf-2.0/

%changelog
%autochangelog
