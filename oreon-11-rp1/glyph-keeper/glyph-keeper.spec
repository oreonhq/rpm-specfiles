%global source0_hash ab866b7fe2536970fda77257ff6c952d0d51f767af0b83a43f1284134959d604

Name:           glyph-keeper
Version:        0.32
Release:        42%{?dist}
Summary:        Library for text rendering
License:        zlib
URL:            http://www.allegro.cc/resource/Libraries/Text/GlyphKeeper
# Upstream is MIA
Source0:        %{name}-%{version}.zip
Patch0:         glyph-keeper-0.29.1-fixes.patch
Patch1:         glyph-keeper-0.32-so-compat.patch
BuildRequires:  gcc
BuildRequires:  freetype-devel >= 2.1.10
BuildRequires:  SDL_gfx-devel allegro-devel
BuildRequires: make

%description
Glyph Keeper is a library for text rendering. It is written in C and can be
used by C or C++ code. Glyph Keeper helps your program to load a font, render
character glyphs and write them to the target surface. Right now only Allegro
and SDL targets are supported, but there will be more in future. Glyph Keeper
uses FreeType as a font engine.

%package        allegro
Summary:        Library for text rendering with Allegro
# Only the allegro package is currently actually used in Fedora, so make this
# one obsolete the old glyph-keeper package which had both allegro and SDL
# variants in one package
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < 0.32-9

%description    allegro
Glyph Keeper is a library for text rendering. It is written in C and can be
used by C or C++ code. Glyph Keeper helps your program to load a font, render
character glyphs and write them to the target surface. Glyph Keeper uses
FreeType as a font engine. This package contains glyph-keeper build for use
with Allegro apps.

%package        allegro-devel
Summary:        Development files for glyph-keeper-allegro
Requires:       allegro-devel
Requires:       glyph-keeper-allegro = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.32-9

%description    allegro-devel
The glyph-keeper-allegro-devel package contains libraries and header files for
developing applications that use glyph-keeper-allegro.

%package        SDL
Summary:        Library for text rendering with SDL

%description    SDL
Glyph Keeper is a library for text rendering. It is written in C and can be
used by C or C++ code. Glyph Keeper helps your program to load a font, render
character glyphs and write them to the target surface. Glyph Keeper uses
FreeType as a font engine. This package contains glyph-keeper build for use
with SDL apps.

%package        SDL-devel
Summary:        Development files for glyph-keeper-SDL
Requires:       SDL-devel
Requires:       glyph-keeper-SDL = %{version}-%{release}

%description    SDL-devel
The glyph-keeper-SDL-devel package contains libraries and header files for
developing applications that use glyph-keeper-SDL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -z .fix
%patch -P1 -p1 -z .compat
sed -i 's/\r//' docs/*.html *.txt

%build
make %{?_smp_mflags} -f Makefile.GNU.all TARGET=ALLEGRO FT_LIB=-lfreetype \
  OFLAGS="$RPM_OPT_FLAGS -fpic -I/usr/include/freetype2" lib
gcc -shared -o libglyph-alleg.so.0 -Wl,-soname,libglyph-alleg.so.0 \
  obj/glyph-alleg.o -lfreetype $(allegro-config --libs)

make %{?_smp_mflags} -f Makefile.GNU.all TARGET=SDL FT_LIB=-lfreetype \
  OFLAGS="$RPM_OPT_FLAGS -fpic $(sdl-config --cflags) -I/usr/include/freetype2" lib
gcc -shared -o libglyph-sdl.so.0 -Wl,-soname,libglyph-sdl.so.0 \
  obj/glyph-sdl.o -lfreetype -lSDL -lSDL_gfx

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 libglyph-*.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libglyph-alleg.so.0 $RPM_BUILD_ROOT%{_libdir}/libglyph-alleg.so
ln -s libglyph-sdl.so.0 $RPM_BUILD_ROOT%{_libdir}/libglyph-sdl.so
install -m 644 include/glyph.h $RPM_BUILD_ROOT%{_includedir}

%ldconfig_scriptlets allegro

%ldconfig_scriptlets SDL

%files allegro
%doc license.txt changes.txt authors.txt docs/*
%{_libdir}/libglyph-alleg.so.0

%files allegro-devel
%{_includedir}/glyph.h
%{_libdir}/libglyph-alleg.so

%files SDL
%doc license.txt changes.txt authors.txt docs/*
%{_libdir}/libglyph-sdl.so.0

%files SDL-devel
%{_includedir}/glyph.h
%{_libdir}/libglyph-sdl.so

%changelog
%autochangelog
