%global source0_hash 7322236cd12090c3eb40b9728be4d49c76f66ad17d04369584d4ecad5cf77c68
%{?mingw_package_header}
Name:           mingw-SDL3
Version:        3.4.16
Release:        1%{?dist}
Summary:        MinGW Windows port of SDL3 cross-platform multimedia library
License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            http://www.libsdl.org/
Source0:        http://www.libsdl.org/release/SDL3-%{version}.tar.gz
BuildArch:      noarch
%ifarch %{ix86}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win32
%package -n mingw32-SDL3
Summary:        MinGW32 Windows port of SDL cross-platform multimedia library
Provides:       bundled(hidraw)
%description -n mingw32-SDL3
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win32 (static)
%package -n mingw32-SDL3-static
Summary:        MinGW32 Windows port of SDL cross-platform multimedia library
Requires:       mingw32-SDL3 = %{version}-%{release}
%description -n mingw32-SDL3-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64
%package -n mingw64-SDL3
Summary:        MinGW64 Windows port of SDL cross-platform multimedia library
Provides:       bundled(hidraw)
%description -n mingw64-SDL3
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64 (static)
%package -n mingw64-SDL3-static
Summary:        MinGW64 Windows port of SDL cross-platform multimedia library
Requires:       mingw64-SDL3 = %{version}-%{release}
%description -n mingw64-SDL3-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir SDL3-%{version}
%oreon_prep
%build

%mingw_cmake -DSDL_STATIC=ON -DSDL_STATIC_PIC=ON -DSDL_VENDOR_INFO="%{?dist_vendor} %{version}-%{release}"
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/licenses
rm -rf %{buildroot}%{mingw64_datadir}/licenses
%oreon_autofiles mingw32-SDL3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-SDL3-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-SDL3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-SDL3-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-SDL3 -f %{oreon_filedir}/mingw32-SDL3.list
%files -n mingw32-SDL3-static -f %{oreon_filedir}/mingw32-SDL3-static.list
%files -n mingw64-SDL3 -f %{oreon_filedir}/mingw64-SDL3.list
%files -n mingw64-SDL3-static -f %{oreon_filedir}/mingw64-SDL3-static.list

%changelog

%autochangelog
