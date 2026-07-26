%global source0_hash 724cd895ecf4da319a3ef164892b72078bd92632a5d812111261cde248ebcdb7

%?mingw_package_header

Name:           mingw-SDL_ttf
Version:        2.0.11
Release:        19%{?dist}

%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL
Summary: %{pkg_summary}

License:        Zlib
URL:            https://www.libSDL.org/projects/SDL_ttf/release-1.2.html
Source0:        https://www.libSDL.org/projects/SDL_ttf/release/SDL_ttf-%{version}.tar.gz

# Upstream bug #830: TTF_RenderGlyph_Shaded is broken
# Patch taken from upstream Bugzilla:
#   https://bugzilla-attachments.libsdl.org/attachments/830/renderglyph_shaded.patch.txt
Patch0:         renderglyph_shaded.patch

BuildArch:      noarch

BuildRequires:  freetype-devel >= 2.0
BuildRequires:  %{_bindir}/iconv
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL >= 1.2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL >= 1.2

%global  pkg_description  Simple DirectMedia Layer (SDL) is a cross-platform multimedia library \
designed to provide fast access to the graphics frame buffer and audio device. \
This package contains a library that allows you to use TrueType fonts \
to render text in SDL 1.2 applications.

%description
%{pkg_description}

# Win32
%package -n mingw32-SDL_ttf
Summary: %{pkg_summary}

%description -n mingw32-SDL_ttf
%{pkg_description}

# Win64
%package -n mingw64-SDL_ttf
Summary: %{pkg_summary}

%description -n mingw64-SDL_ttf
%{pkg_description}

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SDL_ttf-%{version}
%patch -P0 -p0

# Convert file encoding
for FILE in CHANGES; do
  iconv -f ISO-8859-1 -t UTF-8 < "${FILE}" > "${FILE}--UTF8"
  mv "${FILE}--UTF8" "${FILE}"
done

%build
%mingw_configure \
  --disable-static \
  --disable-dependency-tracking \

# The configure script for this library doesn't fully work with MinGW,
# so we have to edit the resulting Makefiles a bit.
sed \
  -e 's| -I%{_includedir}/freetype2 | -I%{mingw32_includedir}/freetype2 |g' \
  -e 's| -I%{_includedir}/libpng16 | -I%{mingw32_includedir}/libpng16 |g'   \
  -i build_win32/libtool build_win32/Makefile

sed \
  -e 's| -I%{_includedir}/freetype2 | -I%{mingw64_includedir}/freetype2 |g' \
  -e 's| -I%{_includedir}/libpng16 | -I%{mingw64_includedir}/libpng16 |g'   \
  -i build_win64/libtool build_win64/Makefile

%mingw_make %{?smp_mflags}

%install
%mingw_make DESTDIR=%{buildroot} install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-SDL_ttf
%doc CHANGES README
%license COPYING
%{mingw32_bindir}/SDL_ttf.dll
%{mingw32_libdir}/libSDL_ttf.dll.a
%{mingw32_libdir}/pkgconfig/SDL_ttf.pc
%{mingw32_includedir}/SDL

# Win64
%files -n mingw64-SDL_ttf
%doc CHANGES README
%license COPYING
%{mingw64_bindir}/SDL_ttf.dll
%{mingw64_libdir}/libSDL_ttf.dll.a
%{mingw64_libdir}/pkgconfig/SDL_ttf.pc
%{mingw64_includedir}/SDL

%changelog
%autochangelog
