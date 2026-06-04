%global source0_hash none

%{?mingw_package_header}

Name:           mingw-harfbuzz
Version:        13.0.1
Release:        1%{?dist}
Summary:        MinGW Windows Harfbuzz library

License:        MIT
URL:            http://www.harfbuzz.org
Source0:        https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz

# Invoke versioned python
Patch0:        harfbuzz-python.patch

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  python3

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-icu

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-icu


%description
HarfBuzz is an implementation of the OpenType Layout engine.


# Win32
%package -n mingw32-harfbuzz
Summary:        MinGW Windows Harfbuzz library

%description -n mingw32-harfbuzz
HarfBuzz is an implementation of the OpenType Layout engine.

%package -n mingw32-harfbuzz-static
Summary:        Static version of the MinGW Windows Harfbuzz library
Requires:       mingw32-harfbuzz = %{version}-%{release}
Requires:       mingw32-glib2-static

%description -n mingw32-harfbuzz-static
Static version of the MinGW Windows Harfbuzz library.

# Win64
%package -n mingw64-harfbuzz
Summary:        MinGW Windows Harfbuzz library

%description -n mingw64-harfbuzz
HarfBuzz is an implementation of the OpenType Layout engine.

%package -n mingw64-harfbuzz-static
Summary:        Static version of the MinGW Windows Harfbuzz library
Requires:       mingw64-harfbuzz = %{version}-%{release}
Requires:       mingw64-glib2-static

%description -n mingw64-harfbuzz-static
Static version of the MinGW Windows Harfbuzz library.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n harfbuzz-%{version}


%build
export MINGW_BUILDDIR_SUFFIX=static
%mingw_meson --default-library=static
%mingw_ninja
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_meson --default-library=shared
%mingw_ninja


%install
export MINGW_BUILDDIR_SUFFIX=static
%mingw_ninja_install
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_ninja_install


# Win32
%files -n mingw32-harfbuzz
%license COPYING
%{mingw32_bindir}/hb-info.exe
%{mingw32_bindir}/hb-shape.exe
%{mingw32_bindir}/hb-subset.exe
%{mingw32_bindir}/hb-vector.exe
%{mingw32_bindir}/hb-view.exe
%{mingw32_bindir}/libharfbuzz-0.dll
%{mingw32_bindir}/libharfbuzz-gobject-0.dll
%{mingw32_bindir}/libharfbuzz-icu-0.dll
%{mingw32_bindir}/libharfbuzz-subset-0.dll
%{mingw32_bindir}/libharfbuzz-cairo-0.dll
%{mingw32_bindir}/libharfbuzz-raster-0.dll
%{mingw32_bindir}/libharfbuzz-vector-0.dll
%{mingw32_includedir}/harfbuzz/
%{mingw32_libdir}/libharfbuzz.dll.a
%{mingw32_libdir}/libharfbuzz-gobject.dll.a
%{mingw32_libdir}/libharfbuzz-icu.dll.a
%{mingw32_libdir}/libharfbuzz-subset.dll.a
%{mingw32_libdir}/libharfbuzz-cairo.dll.a
%{mingw32_libdir}/libharfbuzz-raster.dll.a
%{mingw32_libdir}/libharfbuzz-vector.dll.a
%{mingw32_libdir}/pkgconfig/harfbuzz.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-gobject.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-icu.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-subset.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-cairo.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-raster.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-vector.pc
%{mingw32_libdir}/cmake/harfbuzz/

%files -n mingw32-harfbuzz-static
%{mingw32_libdir}/libharfbuzz.a
%{mingw32_libdir}/libharfbuzz-cairo.a
%{mingw32_libdir}/libharfbuzz-gobject.a
%{mingw32_libdir}/libharfbuzz-icu.a
%{mingw32_libdir}/libharfbuzz-subset.a
%{mingw32_libdir}/libharfbuzz-raster.a
%{mingw32_libdir}/libharfbuzz-vector.a

# Win64
%files -n mingw64-harfbuzz
%license COPYING
%{mingw64_bindir}/hb-info.exe
%{mingw64_bindir}/hb-shape.exe
%{mingw64_bindir}/hb-subset.exe
%{mingw64_bindir}/hb-vector.exe
%{mingw64_bindir}/hb-view.exe
%{mingw64_bindir}/libharfbuzz-0.dll
%{mingw64_bindir}/libharfbuzz-gobject-0.dll
%{mingw64_bindir}/libharfbuzz-icu-0.dll
%{mingw64_bindir}/libharfbuzz-subset-0.dll
%{mingw64_bindir}/libharfbuzz-cairo-0.dll
%{mingw64_bindir}/libharfbuzz-raster-0.dll
%{mingw64_bindir}/libharfbuzz-vector-0.dll
%{mingw64_includedir}/harfbuzz/
%{mingw64_libdir}/libharfbuzz.dll.a
%{mingw64_libdir}/libharfbuzz-gobject.dll.a
%{mingw64_libdir}/libharfbuzz-icu.dll.a
%{mingw64_libdir}/libharfbuzz-subset.dll.a
%{mingw64_libdir}/libharfbuzz-cairo.dll.a
%{mingw64_libdir}/libharfbuzz-raster.dll.a
%{mingw64_libdir}/libharfbuzz-vector.dll.a
%{mingw64_libdir}/pkgconfig/harfbuzz.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-gobject.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-icu.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-subset.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-cairo.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-raster.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-vector.pc
%{mingw64_libdir}/cmake/harfbuzz/

%files -n mingw64-harfbuzz-static
%{mingw64_libdir}/libharfbuzz.a
%{mingw64_libdir}/libharfbuzz-cairo.a
%{mingw64_libdir}/libharfbuzz-gobject.a
%{mingw64_libdir}/libharfbuzz-icu.a
%{mingw64_libdir}/libharfbuzz-subset.a
%{mingw64_libdir}/libharfbuzz-raster.a
%{mingw64_libdir}/libharfbuzz-vector.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.1-1
- Prepare for Oreon 11 (RP1)
