%global source0_hash 0b2bf1e7b6568adbdbc9bb924643f79d9dedafe061fa1ed687d1d9ac4e453bfd

%?mingw_package_header

Name:           mingw-SDL2_ttf
License:        Zlib

Version:        2.24.0
Release:        3%{?dist}

%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL2
Summary: %{pkg_summary}

URL:            https://www.libSDL.org/projects/SDL_ttf/
Source0:        %{URL}release/SDL2_ttf-%{version}.tar.gz

# By default, some example programs are also built - we want only the library.
Patch0:         0000-disable-building-example-programs.patch

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw32-SDL2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw64-SDL2

%global  pkg_description  Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library \
designed to provide fast access to the graphics frame buffer and audio device. \
This package contains a library that allows you to use TrueType fonts \
to render text in SDL2 applications.

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

%autosetup -n SDL2_ttf-%{version} -p1

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

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Convert CRLF line endings to LF
sed -i 's/\r$//' README.txt CHANGES.txt LICENSE.txt

# Win32
%files -n mingw32-SDL2_ttf
%doc CHANGES.txt README.txt
%license LICENSE.txt
%{mingw32_bindir}/SDL2_ttf.dll
%{mingw32_libdir}/libSDL2_ttf.dll.a
%{mingw32_libdir}/cmake/SDL2_ttf/
%{mingw32_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_ttf
%doc CHANGES.txt README.txt
%license LICENSE.txt
%{mingw64_bindir}/SDL2_ttf.dll
%{mingw64_libdir}/libSDL2_ttf.dll.a
%{mingw64_libdir}/cmake/SDL2_ttf/
%{mingw64_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw64_includedir}/SDL2

%changelog
%autochangelog
