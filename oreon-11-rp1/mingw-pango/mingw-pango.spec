%global source0_hash 890640c841dae77d3ae3d8fe8953784b930fa241b17423e6120c7bfdf8b891e7

%{?mingw_package_header}

Name:           mingw-pango
Version:        1.57.0
Release:        2%{?dist}
Summary:        MinGW Windows Pango library

License:        LGPL-2.0-or-later
URL:            http://www.pango.org
# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        http://download.gnome.org/sources/pango/%{release_version}/pango-%{version}.tar.xz

# Make the dependencies on freetype and fontconfig runtime dependencies
# FIXME: See TODO in patch
#Patch1001:      pango-enable-delay-load-of-freetype-and-fontconfig.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-fribidi
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-harfbuzz

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-fribidi
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-harfbuzz

BuildRequires:  pkgconfig
BuildRequires:  meson
BuildRequires:  gcc-c++

# Needed for the delay-load patch
# BuildRequires:  mingw-w64-tools

%description
MinGW Windows Pango library.

# Win32
%package -n mingw32-pango
Summary:        MinGW Windows Pango library
Requires:       pkgconfig

%description -n mingw32-pango
MinGW Windows Pango library.

%package -n mingw32-pango-static
Summary:        Static version of the MinGW Windows Pango library
Requires:       mingw32-pango = %{version}-%{release}

%description -n mingw32-pango-static
Static version of the MinGW Windows Pango library.

# Win64
%package -n mingw64-pango
Summary:        MinGW Windows Pango library
Requires:       pkgconfig

%description -n mingw64-pango
MinGW Windows Pango library.

%package -n mingw64-pango-static
Summary:        Static version of the MinGW Windows Pango library
Requires:       mingw64-pango = %{version}-%{release}

%description -n mingw64-pango-static
Static version of the MinGW Windows Pango library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pango-%{version}

%build
%mingw_meson --default-library=both -Dintrospection=disabled -Dgtk_doc=false -Dfontconfig=enabled
%mingw_ninja

%install
%mingw_ninja_install

mkdir -p %{buildroot}%{mingw32_sysconfdir}/pango/
mkdir -p %{buildroot}%{mingw64_sysconfdir}/pango/

# Win32
%files -n mingw32-pango
%license COPYING
%{mingw32_bindir}/libpango-1.0-0.dll
%{mingw32_bindir}/libpangocairo-1.0-0.dll
%{mingw32_bindir}/libpangoft2-1.0-0.dll
%{mingw32_bindir}/libpangowin32-1.0-0.dll
%{mingw32_bindir}/pango-list.exe
%{mingw32_bindir}/pango-segmentation.exe
%{mingw32_bindir}/pango-view.exe
%{mingw32_includedir}/pango-1.0/
%{mingw32_libdir}/libpango-1.0.dll.a
%{mingw32_libdir}/libpangocairo-1.0.dll.a
%{mingw32_libdir}/libpangoft2-1.0.dll.a
%{mingw32_libdir}/libpangowin32-1.0.dll.a
%{mingw32_libdir}/pkgconfig/pango.pc
%{mingw32_libdir}/pkgconfig/pangocairo.pc
%{mingw32_libdir}/pkgconfig/pangofc.pc
%{mingw32_libdir}/pkgconfig/pangoft2.pc
%{mingw32_libdir}/pkgconfig/pangoot.pc
%{mingw32_libdir}/pkgconfig/pangowin32.pc
%{mingw32_sysconfdir}/pango/

%files -n mingw32-pango-static
%{mingw32_libdir}/libpango-1.0.a
%{mingw32_libdir}/libpangocairo-1.0.a
%{mingw32_libdir}/libpangoft2-1.0.a
%{mingw32_libdir}/libpangowin32-1.0.a

# Win64
%files -n mingw64-pango
%license COPYING
%{mingw64_bindir}/libpango-1.0-0.dll
%{mingw64_bindir}/libpangocairo-1.0-0.dll
%{mingw64_bindir}/libpangoft2-1.0-0.dll
%{mingw64_bindir}/libpangowin32-1.0-0.dll
%{mingw64_bindir}/pango-list.exe
%{mingw64_bindir}/pango-segmentation.exe
%{mingw64_bindir}/pango-view.exe
%{mingw64_includedir}/pango-1.0/
%{mingw64_libdir}/libpango-1.0.dll.a
%{mingw64_libdir}/libpangocairo-1.0.dll.a
%{mingw64_libdir}/libpangoft2-1.0.dll.a
%{mingw64_libdir}/libpangowin32-1.0.dll.a
%{mingw64_libdir}/pkgconfig/pango.pc
%{mingw64_libdir}/pkgconfig/pangocairo.pc
%{mingw64_libdir}/pkgconfig/pangofc.pc
%{mingw64_libdir}/pkgconfig/pangoft2.pc
%{mingw64_libdir}/pkgconfig/pangoot.pc
%{mingw64_libdir}/pkgconfig/pangowin32.pc
%{mingw64_sysconfdir}/pango/

%files -n mingw64-pango-static
%{mingw64_libdir}/libpango-1.0.a
%{mingw64_libdir}/libpangocairo-1.0.a
%{mingw64_libdir}/libpangoft2-1.0.a
%{mingw64_libdir}/libpangowin32-1.0.a

%changelog
%autochangelog
