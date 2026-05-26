# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 445ed8208a6e4823de1226a74ca319d3600e83f6369f99b14265006599c32ccb
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{?mingw_package_header}

Name:           mingw-cairo
Version:        1.18.4
Release:        3%{?dist}
Summary:        MinGW Windows Cairo library

License:        LGPL-2.1-only OR MPL-1.1
URL:            http://cairographics.org
Source0:        https://www.cairographics.org/releases/cairo-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-glib2

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-glib2


%description
MinGW Windows Cairo library.


# Win32
%package -n mingw32-cairo
Summary:        MinGW Windows Cairo library
Requires:       mingw32-fontconfig
Requires:       mingw32-freetype
Requires:       pkgconfig

%description -n mingw32-cairo
MinGW Windows Cairo library.

%package -n mingw32-cairo-static
Summary:        Static version of the MinGW Windows Cairo library
Requires:       mingw32-cairo = %{version}-%{release}

%description -n mingw32-cairo-static
Static version of the MinGW Windows Cairo library.

# Win64
%package -n mingw64-cairo
Summary:        MinGW Windows Cairo library
Requires:       mingw64-fontconfig
Requires:       mingw64-freetype
Requires:       pkgconfig

%description -n mingw64-cairo
MinGW Windows Cairo library.

%package -n mingw64-cairo-static
Summary:        Static version of the MinGW Windows Cairo library
Requires:       mingw64-cairo = %{version}-%{release}

%description -n mingw64-cairo-static
Static version of the MinGW Windows Cairo library.


%{?mingw_debug_package}


%prep
%oreon_verify_sources
%autosetup -p1 -n cairo-%{version}


%build
%mingw_meson --default-library both -Dfontconfig=enabled -Dfreetype=enabled
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-cairo
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{mingw32_bindir}/libcairo-2.dll
%{mingw32_bindir}/libcairo-gobject-2.dll
%{mingw32_bindir}/libcairo-script-interpreter-2.dll
%{mingw32_includedir}/cairo/
%{mingw32_libdir}/libcairo.dll.a
%{mingw32_libdir}/libcairo-gobject.dll.a
%{mingw32_libdir}/libcairo-script-interpreter.dll.a
%{mingw32_libdir}/pkgconfig/cairo-gobject.pc
%{mingw32_libdir}/pkgconfig/cairo-fc.pc
%{mingw32_libdir}/pkgconfig/cairo.pc
%{mingw32_libdir}/pkgconfig/cairo-pdf.pc
%{mingw32_libdir}/pkgconfig/cairo-dwrite-font.pc
%{mingw32_libdir}/pkgconfig/cairo-svg.pc
%{mingw32_libdir}/pkgconfig/cairo-ps.pc
%{mingw32_libdir}/pkgconfig/cairo-win32-font.pc
%{mingw32_libdir}/pkgconfig/cairo-ft.pc
%{mingw32_libdir}/pkgconfig/cairo-png.pc
%{mingw32_libdir}/pkgconfig/cairo-script.pc
%{mingw32_libdir}/pkgconfig/cairo-script-interpreter.pc
%{mingw32_libdir}/pkgconfig/cairo-tee.pc
%{mingw32_libdir}/pkgconfig/cairo-win32.pc


%files -n mingw32-cairo-static
%{mingw32_libdir}/libcairo.a
%{mingw32_libdir}/libcairo-gobject.a
%{mingw32_libdir}/libcairo-script-interpreter.a

# Win64
%files -n mingw64-cairo
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{mingw64_bindir}/libcairo-2.dll
%{mingw64_bindir}/libcairo-gobject-2.dll
%{mingw64_bindir}/libcairo-script-interpreter-2.dll
%{mingw64_includedir}/cairo/
%{mingw64_libdir}/libcairo.dll.a
%{mingw64_libdir}/libcairo-gobject.dll.a
%{mingw64_libdir}/libcairo-script-interpreter.dll.a
%{mingw64_libdir}/pkgconfig/cairo-gobject.pc
%{mingw64_libdir}/pkgconfig/cairo-fc.pc
%{mingw64_libdir}/pkgconfig/cairo.pc
%{mingw64_libdir}/pkgconfig/cairo-pdf.pc
%{mingw64_libdir}/pkgconfig/cairo-dwrite-font.pc
%{mingw64_libdir}/pkgconfig/cairo-svg.pc
%{mingw64_libdir}/pkgconfig/cairo-ps.pc
%{mingw64_libdir}/pkgconfig/cairo-win32-font.pc
%{mingw64_libdir}/pkgconfig/cairo-ft.pc
%{mingw64_libdir}/pkgconfig/cairo-png.pc
%{mingw64_libdir}/pkgconfig/cairo-script.pc
%{mingw64_libdir}/pkgconfig/cairo-script-interpreter.pc
%{mingw64_libdir}/pkgconfig/cairo-tee.pc
%{mingw64_libdir}/pkgconfig/cairo-win32.pc

%files -n mingw64-cairo-static
%{mingw64_libdir}/libcairo.a
%{mingw64_libdir}/libcairo-gobject.a
%{mingw64_libdir}/libcairo-script-interpreter.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.18.4-3
- Prepare for Oreon 11 (RP1)
