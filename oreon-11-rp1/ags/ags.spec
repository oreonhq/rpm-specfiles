%global source0_hash a62c12aeca8c8acc5a6ac36c77a7ebb70af4696b2a1fa0b5ca8af6b2833e8e1a

%bcond_without openal

%global fver v%{version}
# avoid building bundled libraries as shared
%undefine _cmake_shared_libs

Name: ags
Summary: Engine for creating and running videogames of adventure (quest) genre
Version: 3.6.2.16
URL:     http://www.adventuregamestudio.co.uk/site/ags/
Release: 3%{?dist}
Source0: https://github.com/adventuregamestudio/ags/archive/%{fver}/ags-%{fver}.tar.gz
Patch0: ags-use-system-libraries.patch
Patch1: ags-build-tests-with-cxx17.patch
# Most code is under Artistic-2.0, except:
# Common/libsrc/aastr-0.1.1: LicenseRef-Fedora-UltraPermissive
# Common/libsrc/alfont-2.0.9: FTL
# Engine/libsrc/apeg-1.2.1: MPEG-SSG
# Engine/libsrc/glad: Apache-2.0 AND MIT-Khronos-old
# Engine/libsrc/libcda-0.5: Zlib
# Plugins/agsblend/agsblend: MIT
# Plugins/agspalrender/agspalrender/raycast.{cpp,h}: BSD-2-Clause
# Plugins/AGSSpriteFont: CC0-1.0
# libsrc/allegro: Giftware
License: Artistic-2.0 AND LicenseRef-Fedora-UltraPermissive AND FTL AND MPEG-SSG AND Apache-2.0 AND MIT-Khronos-old AND Zlib AND MIT AND BSD-2-Clause AND CC0-1.0 AND Giftware
# incorrect rendering with new FT: https://github.com/adventuregamestudio/ags/issues/1528
Provides: bundled(freetype) = 2.1.3
%if %{with openal}
BuildRequires: openal-soft-devel
%else
# https://github.com/icculus/mojoAL (zlib)
Provides: bundled(mojoal)
%endif
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glad
BuildRequires: glm-devel
BuildRequires: gtest-devel
# for KHR/khrplatform.h
BuildRequires: libglvnd-devel
BuildRequires: libogg-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: make
BuildRequires: cmake(miniz)
BuildRequires: SDL2-devel
BuildRequires: SDL2_sound-devel
BuildRequires: tinyxml2-devel
# https://web.archive.org/web/20050323070052/http://www.inp.nsk.su/~bukinm/dusty/aastr/ (Giftware)
# dead upstream, might be possible to use aastr2:
# https://www.allegro.cc/resource/Libraries/Graphics/AASTR2
Provides: bundled(aastr) = 0.1.1
# bundled alfont is patched
Provides: bundled(alfont) = 2.0.9
# bundled allegro is stripped and patched
Provides: bundled(allegro) = 4.4.3
# http://kcat.strangesoft.net/apeg.html (Public Domain)
Provides: bundled(apeg) = 1.2.1
# https://web.archive.org/web/20040104090747/http://www.alphalink.com.au/~tjaden/libcda/index.html (zlib)
# dead upstream
Provides: bundled(libcda) = 0.5

%description
Adventure Game Studio (AGS) - is the IDE and the engine meant for creating and
running videogames of adventure (aka "quest") genre. It has potential, although
limited, support for other genres as well.

Originally created by Chris Jones back in 1999, AGS was opensourced in 2011 and
since continued to be developed by contributors.

%package tools
Summary: Tools for Adventure Game Studio engine game development
Requires: %{name}%{_isa} = %{version}-%{release}

%description tools
This package contains the AGS engine game development tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1 -b .orig
%patch 1 -p1 -b .cxx17
# delete unused bundled stuff
pushd Common/libinclude
rm -r ogg
rm -r theora
rm -r vorbis
popd
pushd Common/libsrc
rmdir googletest
popd
pushd Engine/libsrc
rm -r glad{,-gles2}/{src,include}
glad --reproducible --out-path=glad       --profile="compatibility" --api="gl=2.1"    --generator="c" --spec="gl" --extensions="GL_EXT_framebuffer_object"
glad --reproducible --out-path=glad-gles2 --profile="core"          --api="gles2=2.0" --generator="c" --spec="gl" --extensions=""
rm -r ogg
rm -r theora
rm -r vorbis
popd
pushd libsrc
rm -r glm
rm -r miniz
%if %{with openal}
rm -r mojoAL
%endif
rm -r tinyxml2
popd
iconv -o Changes.txt.utf-8 -f iso8859-1 -t utf-8 Changes.txt && \
touch -r Changes.txt Changes.txt.utf-8 && \
mv Changes.txt.utf-8 Changes.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DAGS_BUILD_TOOLS=TRUE \
    -DAGS_TESTS=TRUE \
    -DAGS_USE_LOCAL_SDL2=TRUE \
    -DAGS_USE_LOCAL_SDL2_SOUND=TRUE \
    -DAGS_USE_LOCAL_OGG=TRUE \
    -DAGS_USE_LOCAL_VORBIS=TRUE \
    -DAGS_USE_LOCAL_THEORA=TRUE \
    -DAGS_USE_LOCAL_GLM=TRUE \
    -DAGS_USE_LOCAL_TINYXML2=TRUE \
    -DAGS_USE_LOCAL_MINIZ=TRUE \
    -DAGS_USE_LOCAL_GTEST=TRUE \

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license License.txt
%doc Changes.txt Copyright.txt OPTIONS.md README.md
%{_bindir}/ags

%files tools
%{_bindir}/agscc
%{_bindir}/agf2dlgasc
%{_bindir}/agfexport
%{_bindir}/agspak
%{_bindir}/agsunpak
%{_bindir}/crm2ash
%{_bindir}/crmpak
%{_bindir}/trac
%{_bindir}/ags

%changelog
%autochangelog
