%global source0_hash 19cc4bdf222c5bf1c412d11f19f3fee07b310e21a9b731f42f1f71d6faf0e1a0
%bcond_without openal
%global fver v%{version}
%undefine _cmake_shared_libs
Name: ags
Summary:        Engine for creating and running videogames of adventure (quest) genre
Version: 3.6.2.21
URL:     http://www.adventuregamestudio.co.uk/site/ags/
Release:        1%{?dist}
Source0:        https://github.com/adventuregamestudio/%{name}/archive/%{fver}/%{name}-%{fver}.tar.gz
Patch0: ags-use-system-libraries.patch
Patch1: ags-build-tests-with-cxx17.patch
License: Artistic-2.0 AND LicenseRef-Fedora-UltraPermissive AND FTL AND MPEG-SSG AND Apache-2.0 AND MIT-Khronos-old AND Zlib AND MIT AND BSD-2-Clause AND CC0-1.0 AND Giftware
Provides: bundled(freetype) = 2.1.3
%if %{with openal}
%else
Provides: bundled(mojoal)
%endif
Provides: bundled(aastr) = 0.1.1
Provides: bundled(alfont) = 2.0.9
Provides: bundled(allegro) = 4.4.3
Provides: bundled(apeg) = 1.2.1
Provides: bundled(libcda) = 0.5
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_sound-devel
BuildRequires:  cmake
BuildRequires:  cmake(miniz)
BuildRequires:  gcc-c++
BuildRequires:  glad
BuildRequires:  glm-devel
BuildRequires:  gtest-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  tinyxml2-devel
# /oreon:deps
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
%oreon_autofiles ags-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n ags-tools -f %{oreon_filedir}/ags-tools.list

%changelog

%autochangelog
