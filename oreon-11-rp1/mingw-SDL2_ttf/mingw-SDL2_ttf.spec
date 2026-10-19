%global source0_hash 0b2bf1e7b6568adbdbc9bb924643f79d9dedafe061fa1ed687d1d9ac4e453bfd
%?mingw_package_header
Name:           mingw-SDL2_ttf
License:        Zlib
Version:        2.24.0
Release:        1%{?dist}
%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL2
Summary:        MinGW Windows port of the TrueType font handling library for SDL2
URL:            https://www.libSDL.org/projects/SDL_ttf/
Source0:        https://www.libSDL.org/projects/SDL_ttf/release/SDL2_ttf-%{version}.tar.gz
Patch0:         0000-disable-building-example-programs.patch
BuildArch:      noarch
%global  pkg_description  Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library \
designed to provide fast access to the graphics frame buffer and audio device. \
This package contains a library that allows you to use TrueType fonts \
to render text in SDL2 applications.
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-harfbuzz
# /oreon:deps
%description
%{pkg_description}

# Win32
%package -n mingw32-SDL2_ttf
Summary: %{pkg_summary}
%description -n mingw32-SDL2_ttf
%{pkg_description}

# Win64
%package -n mingw64-SDL2_ttf
Summary: %{pkg_summary}
%description -n mingw64-SDL2_ttf
%{pkg_description}

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir SDL2_ttf-%{version}
%oreon_prep
%build

./autogen.sh
%mingw_configure \
	--disable-static \
	--disable-dependency-tracking \
	--enable-freetype-builtin=no \
	--enable-harfbuzz-builtin=no \
	--enable-harfbuzz=yes \
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
sed -i 's/\r$//' README.txt CHANGES.txt LICENSE.txt
%oreon_autofiles mingw32-SDL2_ttf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-SDL2_ttf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-SDL2_ttf -f %{oreon_filedir}/mingw32-SDL2_ttf.list
%files -n mingw64-SDL2_ttf -f %{oreon_filedir}/mingw64-SDL2_ttf.list

%changelog

%autochangelog
