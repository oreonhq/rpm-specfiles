%global source0_hash 1c767308174337a74694da0f3ec069c271452163a1ef4540964c50c301f157d4
%{?mingw_package_header}
Name:           mingw-cairo
Version:        1.18.6
Release:        1%{?dist}
Summary:        MinGW Windows Cairo library
License:        LGPL-2.1-only OR MPL-1.1
URL:            http://cairographics.org
Source0:        https://www.cairographics.org/releases/cairo-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  ninja-build
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cairo-%{version}
%oreon_prep
%build

%mingw_meson --default-library both -Dfontconfig=enabled -Dfreetype=enabled
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-cairo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-cairo-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-cairo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-cairo-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-cairo -f %{oreon_filedir}/mingw32-cairo.list
%files -n mingw32-cairo-static -f %{oreon_filedir}/mingw32-cairo-static.list
%files -n mingw64-cairo -f %{oreon_filedir}/mingw64-cairo.list
%files -n mingw64-cairo-static -f %{oreon_filedir}/mingw64-cairo-static.list

%changelog

%autochangelog
