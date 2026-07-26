%global source0_hash none

# The version of MuseScore itself
%global musescore_ver             4.6.5
%global musescore_maj             %{gsub %musescore_ver ^(%d*%.%d*)%..*$ %1}
%global giturl                    https://github.com/musescore/MuseScore

# Font versions.  Use otfinfo -v to extract these values.
# Most are in the fonts directory.  Exceptions:
# - src/framework/ui/data/MusescoreIcon.ttf
# - share/sound/SF_VERSION
%global mscore_font_ver           2.003
%global mscoretext_font_ver       1.0
%global musescoreicon_font_ver    1.0
%global mscorebc_font_ver         1.0
%global mscoretabulature_font_ver 001.000
%global musejazz_font_ver         1.0
%global gootville_font_ver        1.3
%global gootville_text_font_ver   1.2
%global soundfont_ver             0.2.0

# NOTE: The Release tag can be reset to one only if ALL version numbers above
# increase.  This is unlikely to happen.  Resign yourself to bumping the release
# number indefinitely.
Name:           musescore
Summary:        Music Composition & Notation Software
Version:        %{musescore_ver}
Release:        37%{?dist}

# The MuseScore project itself is GPL-3.0-only WITH Font-exception-2.0.  Other
# licenses in play:
# GPL-2.0-or-later
# - thirdparty/beatroot
# (GPL-2.0-only OR GPL-3.0-only)
# - thirdparty/KDDockWidgets
# GPL-3.0-or-later:
# - share/plugins/courtesy_accidentals/
# - share/plugins/intervals/
# - share/plugins/tuning/
# - share/plugins/tuning_modal/
# LGPL-3.0-only
# - share/wallpapers/paper5.png
# LGPL-2.1-or-later
# - thirdparty/fluidsynth
# - thirdparty/rtf2html
# MIT
# - thirdparty/intervaltree
# - src/framework/audio/thirdparty/fluidsynth/fluidsynth-2.3.3/src/bindings/fluid_rtkit.{c,h}
# - src/framework/global/thirdparty/kors_async/LICENSE
# - src/framework/global/thirdparty/kors_logger/LICENSE
# - src/framework/global/thirdparty/kors_modularity/LICENSE
# - src/framework/global/thirdparty/kors_msgpack/LICENSE
# - src/framework/global/thirdparty/kors_profiler/LICENSE
# BSL-1.0
# - code from the utf8cpp header-only library
# BSD-2-Clause
# - code from the picojson header-only library
# Unlicense OR MIT-0
# - code from the dr_libs header-only library
# Unlicense OR MIT
# - code from the stb_vorbis header-only library
License:      %{shrink:
                GPL-3.0-only WITH Font-exception-2.0 AND
                GPL-2.0-or-later AND
                (GPL-2.0-only OR GPL-3.0-only) AND
                GPL-3.0-or-later AND
                LGPL-3.0-only AND
                LGPL-2.1-or-later AND
                MIT AND
                BSD-2-Clause AND
                (Unlicense OR MIT-0) AND
                (Unlicense OR MIT)
		}
URL:            https://musescore.org/
VCS:            git:%{giturl}.git

%global fontorg         org.musescore
%global fontdocs        fonts/README.md

%global fontfamily1     MScore
%global fontsummary1    MuseScore base music font
%global fontlicense1    GPL-3.0-or-later WITH Font-exception-2.0
%global fonts1          fonts/mscore/MScore.otf
%global fontconfs1      %{SOURCE1}
%global fontdescription1 %{expand:This package contains the base MuseScore music font.  It is derived from the
Emmentaler font created for Lilypond, but has been modified for MuseScore.}
%global fontpkgheader1  %{expand:
Epoch:          1
Version:        %{mscore_font_ver}
}

%global fontfamily2     MScoreText
%global fontsummary2    MuseScore base text font
%global fontlicense2    OFL-1.1-RFN
%global fonts2          fonts/mscore/MScoreText.otf
%global fontconfs2      %{SOURCE2}
%global fontdescription2 This package contains the base MuseScore text font.
%global fontpkgheader2  %{expand:
Version:        %{mscoretext_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-mscoretext-fonts < 4.0
Provides:       mscore-mscoretext-fonts = %{musescore_ver}-%{release}
}

%global fontfamily3     MusescoreIcon
%global fontsummary3    MuseScore icon set
%global fontlicense3    GPL-3.0-or-later WITH Font-exception-2.0
%global fonts3          src/framework/ui/data/MusescoreIcon.ttf
%global fontconfs3      %{SOURCE3}
%global fontdescription3 This package contains a set of MuseScore icons.
%global fontpkgheader3  %{expand:
Version:        %{musescoreicon_font_ver}
}

%global fontfamily4     MScoreBC
%global fontsummary4    Font with Basso Continuo digits and symbols
%global fontlicense4    OFL-1.1-RFN
%global fonts4          fonts/mscore-BC.ttf
%global fontconfs4      %{SOURCE4}
%global fontdescription4 %{expand:This package contains a MuseScore font with Basso Continuo digits and symbols,
matching glyphs in the main MuseScore font.}
%global fontpkgheader4  %{expand:
Version:        %{mscorebc_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-bc-fonts < 4.0
Provides:       mscore-bc-fonts = %{musescore_ver}-%{release}
}

%global fontfamily5     MScoreTabulature
%global fontsummary5    Font with Renaissance-style tabulatures
%global fontlicense5    OFL-1.1-RFN
%global fonts5          fonts/mscoreTab.ttf
%global fontconfs5      %{SOURCE5}
%global fontdescription5 This package contains a MuseScore font with Renaissance-style tabulatures.
%global fontpkgheader5  %{expand:
Version:        %{mscoretabulature_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-mscoretab-fonts < 4.0
Provides:       mscore-mscoretab-fonts = %{musescore_ver}-%{release}
}

%global fontfamily6     MuseJazz
%global fontsummary6    Handwritten font for text, chord names, and so forth
%global fontlicense6    OFL-1.1
%global fontlicenses6   fonts/musejazz/OFL.txt
%global fonts6          fonts/musejazz/MuseJazz.otf
%global fontconfs6      %{SOURCE6}
%global fontdescription6 %{expand:This package contains a MuseScore font with a handwritten look for text, chord
names, etc.}
%global fontpkgheader6  %{expand:
Version:        %{musejazz_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-musejazz-fonts < 4.0
Provides:       mscore-musejazz-fonts = %{musescore_ver}-%{release}
}

%global fontfamily7     MuseJazz Text
%global fontsummary7    Text font to complement MuseJazz
%global fontlicense7    OFL-1.1
%global fontlicenses7   fonts/musejazz/OFL.txt
%global fonts7          fonts/musejazz/MuseJazzText.otf
%global fontconfs7      %{SOURCE7}
%global fontdescription7 The MuseJazz Text font is designed to complement the MuseJazz font.
%global fontpkgheader7  %{expand:
Version:        %{musejazz_font_ver}
}

%global fontfamily8     Gootville
%global fontsummary8    Derivative of the Gonville font
%global fontlicense8    OFL-1.1
%global fonts8          fonts/gootville/Gootville.otf
%global fontdocs8       fonts/gootville/readme.txt
%global fontconfs8      %{SOURCE8}
%global fontdescription8 %{expand:Gootville is a derivative of the Gonville font created by Simon Tatham for
Lilypond.  The two fonts have common graphic aspects, but the registration,
glyph order, and other aspects of Gootville have been modified for MuseScore.}
%global fontpkgheader8  %{expand:
Version:        %{gootville_font_ver}
# This can be removed when F42 reaches EOL
Obsoletes:      mscore-gootville-fonts < 4.0
Provides:       mscore-gootville-fonts = %{musescore_ver}-%{release}
}

%global fontfamily9     Gootville Text
%global fontsummary9    Text font to complement Gootville
%global fontlicense9    OFL-1.1
%global fonts9          fonts/gootville/GootvilleText.otf
%global fontdocs9       fonts/gootville/readme.txt
%global fontconfs9      %{SOURCE9}
%global fontdescription9 The Gootville Text font is designed to complement the Gootville font.
%global fontpkgheader9  %{expand:
Version:        %{gootville_text_font_ver}
}

Source0:        %{giturl}/archive/v%{musescore_ver}/MuseScore-%{musescore_ver}.tar.gz
# Fontconfig files
Source1:        65-%{fontpkgname1}.conf
Source2:        65-%{fontpkgname2}.conf
Source3:        65-%{fontpkgname3}.conf
Source4:        65-%{fontpkgname4}.conf
Source5:        65-%{fontpkgname5}.conf
Source6:        65-%{fontpkgname6}.conf
Source7:        65-%{fontpkgname7}.conf
Source8:        65-%{fontpkgname8}.conf
Source9:        65-%{fontpkgname9}.conf

# Unbundle dr_libs, gtest, lame, liblouis, pugixml, stb, and utf8cpp.
# We cannot unbundle KDDockWidgets because the Fedora package builds the
# QtWidgets version, but MuseScore needs the QtQuick version.
# See https://bugzilla.redhat.com/show_bug.cgi?id=2227098
Patch:          %{name}-unbundle-libs.patch
# Unbundle the fonts to comply with the font packaging guidelines
Patch:          %{name}-unbundle-fonts.patch
# Workaround to avoid an out-of-bounds vector access that causes crashes.
# This patch treats the symptom, not the actual disease.  We need to find
# and fix the underlying cause.
Patch:          %{name}-vector.patch
# Avoid using an uninitialized variable
Patch:          %{name}-uninit.patch
# Do not add unnecessary rpaths
Patch:          %{name}-no-rpath.patch
# Fix build failures due to missing #include directives
Patch:          %{name}-include.patch
# Update tinyxml2 from version 10 to version 11 to address CVE-2024-50615
# https://github.com/musescore/MuseScore/pull/29652
Patch:          %{name}-tinyxml2-11.patch
# Update fluidsynth from version 2.3.3 to 2.3.7 to fix several bugs
Patch:          %{name}-fluidsynth-2.3.7.patch
# https://github.com/KDAB/KDDockWidgets/commit/5a86cf69207bfbcc683343b2faf1d3466be2af56.patch
# https://github.com/musescore/MuseScore/pull/30422
Patch:          %{name}-fix-build-against-qt-6-10.patch
# Fix build with FFmpeg 8
Patch:          %{name}-ffmpeg8.patch
# Fix a CVE in the bundled fluidsynth
Patch:          %{name}-CVE-2025-56225.patch
# Enable building with the Fedora VST 3 SDK package
Patch:          %{name}-vst.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  dr_libs-static
BuildRequires:  fdupes
BuildRequires:  font(bravura)
BuildRequires:  font(bravuratext)
BuildRequires:  font(campania)
BuildRequires:  font(finalebroadway)
BuildRequires:  font(finalebroadwaytext)
BuildRequires:  font(finalemaestro)
BuildRequires:  font(finalemaestrotext)
BuildRequires:  font(freesans)
BuildRequires:  font(freeserif)
BuildRequires:  font(petaluma)
BuildRequires:  font(petalumascript)
BuildRequires:  font(petalumatext)
BuildRequires:  fontforge
BuildRequires:  fonts-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  lame-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(liblouis)
BuildRequires:  pkgconfig(libopusenc)
BuildRequires:  (pkgconfig(libpostproc) if libavcodec-free < 8.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  qt6-doctools
BuildRequires:  stb_vorbis-static
BuildRequires:  utf8cpp-static
BuildRequires:  vst3sdk-devel

# Test dependencies
#BuildRequires:  mesa-dri-drivers
#BuildRequires:  mutter
#BuildRequires:  qt6-qtwayland
#BuildRequires:  xwayland-run

Requires:       gootville-fonts = %{gootville_font_ver}-%{release}
Requires:       gootville-text-fonts = %{gootville_text_font_ver}-%{release}
Requires:       mscore-fonts = 1:%{mscore_font_ver}-%{release}
Requires:       mscorebc-fonts = %{mscorebc_font_ver}-%{release}
Requires:       mscoretabulature-fonts = %{mscoretabulature_font_ver}-%{release}
Requires:       mscoretext-fonts = %{mscoretext_font_ver}-%{release}
Requires:       musejazz-fonts = %{musejazz_font_ver}-%{release}
Requires:       musejazz-text-fonts = %{musejazz_font_ver}-%{release}
Requires:       musescoreicon-fonts = %{musescoreicon_font_ver}-%{release}
Requires:       %{name}-data = %{musescore_ver}-%{release}
Requires:       %{name}-soundfont = %{soundfont_ver}-%{release}

Requires:       font(bravura)
Requires:       font(bravuratext)
Requires:       font(campania)
Requires:       font(edwin)
Requires:       font(finalebroadway)
Requires:       font(finalebroadwaytext)
Requires:       font(finalemaestro)
Requires:       font(finalemaestrotext)
Requires:       font(freesans)
Requires:       font(freeserif)
Requires:       font(leland)
Requires:       font(lelandtext)
Requires:       font(petaluma)
Requires:       font(petalumascript)
Requires:       font(petalumatext)
Requires:       hicolor-icon-theme
Requires:       liblouis-tables
Requires:       soundfont2
Requires:       soundfont2-default

# The following products have been modified from their upstream versions,
# or MuseScore uses internal (non-public) APIs
Provides:       bundled(beatroot-vamp) = 1.0
Provides:       bundled(fluidsynth) = 2.3.7
Provides:       bundled(intervaltree) = 0.1
Provides:       bundled(picojson) = 1.3.0
Provides:       bundled(rtf2html) = 0.2.0
Provides:       bundled(tinyxml2) = 11.0.0
Provides:       bundled(KDDockWidgets) = 1.5.0

# The following products were developed specifically for MuseScore and their
# documentation identifies them as copylibs.
Provides:       bundled(kors_async) = 1.3
Provides:       bundled(kors_logger) = 1.3
Provides:       bundled(kors_modularity) = 1.2
Provides:       bundled(kors_msgpack_cpp) = 1.0
Provides:       bundled(kors_profiler) = 1.2

# It might be possible to unbundle libmei.  However, libmei is unmaintained
# upstream: https://github.com/DDMAL/libmei
Provides:       bundled(libmei) = 3.1.0

# This can be removed when F42 reaches EOL
Obsoletes:      mscore < 4.0
Provides:       mscore = %{musescore_ver}-%{release}
Obsoletes:      mscore-fonts-all < 4.0
Provides:       mscore-fonts-all = %{musescore_ver}-%{release}
Obsoletes:      mscore-doc < 4.0
Provides:       mscore-doc = %{musescore_ver}-%{release}

%description
MuseScore is a free cross platform WYSIWYG music notation program.  Some
highlights:

    * WYSIWYG, notes are entered on a "virtual note sheet"
    * Unlimited number of staves
    * Up to four voices per staff
    * Easy and fast note entry with mouse, keyboard or MIDI
    * Integrated sequencer and FluidSynth software synthesizer
    * Import and export of MusicXML and Standard MIDI Files (SMF)
    * Translated in 26 languages

%package        data
Summary:        Common data for MuseScore
Version:        %{musescore_ver}
License:        GPL-3.0-only WITH Font-exception-2.0
BuildArch:      noarch

%description    data
Shared data for all MuseScore installations.

%package        soundfont
Summary:        Basic soundfont for MuseScore
Version:        %{soundfont_ver}
License:        MIT
BuildArch:      noarch

%description    soundfont
This is a scaled-down version of MuseScore_General-HQ.sf2 that replaces some
of the larger instruments to save memory and CPU on older PCs.  This SoundFont
is currently a work-in-progress.  Some samples are derived from FluidR3Mono.

%fontpkg -a

%prep
%autosetup -n MuseScore-%{musescore_ver} -p1

%conf
# Remove bundled stuff
rm -rf \
   thirdparty/dtl \
   src/braille/thirdparty/liblouis \
   src/framework/audio/thirdparty/{dr_libs,flac,lame,opus,opusenc,stb} \
   src/framework/draw/thirdparty/freetype \
   src/framework/global/thirdparty/{pugixml,utfcpp*} \
   src/framework/testing/thirdparty/googletest

# Font compatibility symlinks so we can use resource files in place
cd fonts
ln -s edwin %{name}-edwin-fonts
ln -s gootville %{name}-gootville-fonts
ln -s gootville %{name}-gootville-text-fonts
ln -s leland %{name}-leland-fonts
ln -s leland %{name}-leland-text-fonts
ln -s mscore %{name}-fonts
ln -s mscore %{name}-mscoretext-fonts
ln -s musejazz %{name}-musejazz-fonts
ln -s musejazz %{name}-musejazz-text-fonts

mkdir %{name}-mscorebc-fonts
ln -s ../mscore-BC.sfd %{name}-mscorebc-fonts/mscore-BC.sfd
ln -s ../mscore-BC.ttf %{name}-mscorebc-fonts/mscore-BC.ttf

mkdir %{name}-mscoretabulature-fonts
ln -s ../mscoreTab.sfd %{name}-mscoretabulature-fonts/mscoreTab.sfd
ln -s ../mscoreTab.ttf %{name}-mscoretabulature-fonts/mscoreTab.ttf
cd ..

%build
# Build the actual program
export CFLAGS='%{build_cflags} -I%{_includedir}/ffmpeg -I%{_includedir}/freetype2 -I%{_includedir}/harfbuzz -I%{_includedir}/vst3sdk'
export CXXFLAGS='%{build_cxxflags} -I%{_includedir}/ffmpeg -I%{_includedir}/freetype2 -I%{_includedir}/harfbuzz -I%{_includedir}/vst3sdk'
# now binding breaks RTLD_LAZY, used by Muse Sounds
export LDFLAGS='%{build_ldflags} -Wl,-z,lazy'
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RELEASE         \
    -DMUE_BUILD_IMPEXP_VIDEOEXPORT_MODULE:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_FLAC:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_FREETYPE:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_HARFBUZZ:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_OPUS:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_OPUSENC:BOOL=ON \
    -DMUE_DOWNLOAD_SOUNDFONT:BOOL=OFF \
    -DMUSE_APP_BUILD_MODE:STRING=release \
    -DMUSE_COMPILE_STRING_DEBUG_HACK:BOOL=OFF \
    -DMUSE_COMPILE_USE_PCH:BOOL=OFF \
    -DMUSE_ENABLE_UNIT_TESTS:BOOL=OFF \
    -DMUSE_MODULE_GLOBAL_LOGGER_DEBUGLEVEL:BOOL=OFF \
    -DMUSE_MODULE_NETWORK_WEBSOCKET:BOOL=ON \
    -DMUSE_MODULE_VST:BOOL=ON \
    -DMUSE_PIPEWIRE_AUDIO_DRIVER:BOOL=ON \
    -DQT_NO_PRIVATE_MODULE_WARNING:BOOL=ON
PREFIX=%{_prefix} VERBOSE=1 %cmake_build
PREFIX=%{_prefix} %cmake_build --target manpages

# Build the fonts
%fontbuild -a

%install
PREFIX=%{_prefix} %cmake_install

# Delete files that we don't want to install
rm -rf %{buildroot}%{_includedir} %{buildroot}%{_libdir}

# Install fonts
%fontinstall -a
mkdir -p %{buildroot}%{_datadir}/mscore-%{musescore_maj}/fonts
cp -p fonts/*.xml %{buildroot}%{_datadir}/mscore-%{musescore_maj}/fonts

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
  -i %{buildroot}%{_metainfodir}/%{fontorg}.gootville-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.gootville-text-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscore-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscorebc-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscoretabulature-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.mscoretext-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.musejazz-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.musejazz-text-fonts.metainfo.xml \
  %{buildroot}%{_metainfodir}/%{fontorg}.musescoreicon-fonts.metainfo.xml

# Install SMuFL metadata
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/MScore
cp -p fonts/mscore/metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/MScore
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/MScore/MScore.json
ln -s MScore %{buildroot}%{_datadir}/SMuFL/Fonts/Emmentaler
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/Gootville
cp -p fonts/gootville/metadata.json \
      %{buildroot}%{_datadir}/SMuFL/Fonts/Gootville
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/Gootville/Gootville.json
ln -s Gootville %{buildroot}%{_datadir}/SMuFL/Fonts/Gonville
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/MuseJazz
cp -p fonts/musejazz/metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/MuseJazz
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/MuseJazz/MuseJazz.json

# Validate the desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/org.musescore.MuseScore.desktop

# Validate appdata
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.musescore.MuseScore.appdata.xml

# There are many doc files spread around the tarball. Let's collect them
mv thirdparty/rtf2html/ChangeLog        ChangeLog.rtf2html
mv thirdparty/rtf2html/COPYING.LESSER   COPYING.LESSER.rtf2html
mv thirdparty/rtf2html/README           README.rtf2html
mv thirdparty/rtf2html/README.mscore    README.mscore.rtf2html
mv thirdparty/rtf2html/README.ru        README.ru.rtf2html
mv share/wallpapers/COPYRIGHT           COPYING.wallpapers

# Put a link to the soundfont from the system soundfont directory
mkdir -p %{buildroot}%{_datadir}/soundfonts
ln -s ../mscore-%{musescore_maj}/sound/MS\ Basic.sf3 \
   %{buildroot}%{_datadir}/soundfonts

# Hardlink duplicate files
%fdupes %{buildroot}%{_datadir}/mscore-%{musescore_maj}

%check
%fontcheck -a

# We would like to do this, but the test suite is designed to work with a dev
# build only.  We build in release mode, which causes spurious test failures.
#%%global __ctest xwfb-run -c mutter -- %%{_bindir}/ctest
#export XDG_RUNTIME_DIR=$(mktemp -d /tmp/runtime-mockbuild-XXXX)
#chmod 0700 $XDG_RUNTIME_DIR
#%%ctest
#rm -fr $XDG_RUNTIME_DIR

%files
%doc README.md
%license LICENSE.txt COPYING.LESSER.rtf2html COPYING.wallpapers
%{_bindir}/mscore
%{_mandir}/man1/mscore.1*
%{_mandir}/man1/musescore.1*
%{_datadir}/icons/hicolor/16x16/apps/mscore.png
%{_datadir}/icons/hicolor/24x24/apps/mscore.png
%{_datadir}/icons/hicolor/32x32/apps/mscore.png
%{_datadir}/icons/hicolor/48x48/apps/mscore.png
%{_datadir}/icons/hicolor/64x64/apps/mscore.png
%{_datadir}/icons/hicolor/96x96/apps/mscore.png
%{_datadir}/icons/hicolor/128x128/apps/mscore.png
%{_datadir}/icons/hicolor/512x512/apps/mscore.png
%{_datadir}/icons/hicolor/512x512/mimetypes/application-x-musescore.png
%{_datadir}/icons/hicolor/512x512/mimetypes/application-x-musescore+xml.png
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-musescore.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-musescore+xml.svg
%{_datadir}/applications/org.musescore.MuseScore.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_metainfodir}/org.musescore.MuseScore.appdata.xml

%files data
%license LICENSE.txt
%{_datadir}/liblouis/tables/*
%dir %{_datadir}/mscore-%{musescore_maj}/
%{_datadir}/mscore-%{musescore_maj}/autobotscripts/
%{_datadir}/mscore-%{musescore_maj}/extensions/
%{_datadir}/mscore-%{musescore_maj}/fonts/
%{_datadir}/mscore-%{musescore_maj}/plugins/
%{_datadir}/mscore-%{musescore_maj}/styles/
%{_datadir}/mscore-%{musescore_maj}/templates/
%{_datadir}/mscore-%{musescore_maj}/wallpapers/
%{_datadir}/mscore-%{musescore_maj}/workspaces/
%dir %{_datadir}/mscore-%{musescore_maj}/locale/
%{_datadir}/mscore-%{musescore_maj}/locale/languages.json
%lang(af) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_af.qm
%lang(ar) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ar.qm
%lang(ar_DZ) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ar_DZ.qm
%lang(ar_EG) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ar_EG.qm
%lang(ar_SD) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ar_SD.qm
%lang(ast) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ast.qm
%lang(be) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_be.qm
%lang(bg) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_bg.qm
%lang(br) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_br.qm
%lang(ca) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ca.qm
%lang(ca@valencia) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ca@valencia.qm
%lang(cs) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_cs.qm
%lang(cy) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_cy.qm
%lang(da) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_da.qm
%lang(de) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_de.qm
%lang(el) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_el.qm
%lang(en) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_en.qm
%lang(en_GB) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_en_GB.qm
%lang(en_US) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_en_US.qm
%lang(eo) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_eo.qm
%lang(es) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_es.qm
%lang(et) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_et.qm
%lang(eu) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_eu.qm
%lang(fa) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_fa.qm
%lang(fi) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_fi.qm
%lang(fil) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_fil.qm
%lang(fo) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_fo.qm
%lang(fr) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_fr.qm
%lang(ga) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ga.qm
%lang(gd) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_gd.qm
%lang(gl) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_gl.qm
%lang(he) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_he.qm
%lang(hi_IN) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_hi_IN.qm
%lang(hr) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_hr.qm
%lang(hu) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_hu.qm
%lang(hy) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_hy.qm
%lang(id) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_id.qm
%lang(ig) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ig.qm
%lang(it) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_it.qm
%lang(ja) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ja.qm
%lang(ka) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ka.qm
%lang(kab) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_kab.qm
%lang(ko) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ko.qm
%lang(lt) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_lt.qm
%lang(lv) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_lv.qm
%lang(ml) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ml.qm
%lang(mn_MN) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_mn_MN.qm
%lang(mt) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_mt.qm
%lang(nb) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_nb.qm
%lang(nl) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_nl.qm
%lang(nn) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_nn.qm
%lang(pl) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_pl.qm
%lang(pt) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_pt.qm
%lang(pt_BR) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_pt_BR.qm
%lang(ro) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ro.qm
%lang(ru) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_ru.qm
%lang(scn) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_scn.qm
%lang(sk) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_sk.qm
%lang(sl) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_sl.qm
%lang(sr) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_sr.qm
%lang(sr_RS) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_sr_RS.qm
%lang(sv) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_sv.qm
%lang(sv_SE) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_sv_SE.qm
%lang(th) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_th.qm
%lang(tr) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_tr.qm
%lang(uk) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_uk.qm
%lang(uz@Latn) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_uz@Latn.qm
%lang(vi) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_vi.qm
%lang(zh_CN) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_zh_CN.qm
%lang(zh_HK) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_zh_HK.qm
%lang(zh_TW) %{_datadir}/mscore-%{musescore_maj}/locale/instruments_zh_TW.qm
%lang(af) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_af.qm
%lang(ar) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ar.qm
%lang(ar_DZ) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ar_DZ.qm
%lang(ar_EG) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ar_EG.qm
%lang(ar_SD) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ar_SD.qm
%lang(ast) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ast.qm
%lang(be) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_be.qm
%lang(bg) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_bg.qm
%lang(br) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_br.qm
%lang(ca) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ca.qm
%lang(ca@valencia) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ca@valencia.qm
%lang(cs) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_cs.qm
%lang(cy) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_cy.qm
%lang(da) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_da.qm
%lang(de) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_de.qm
%lang(el) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_el.qm
%lang(en) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_en.qm
%lang(en_GB) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_en_GB.qm
%lang(en_US) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_en_US.qm
%lang(eo) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_eo.qm
%lang(es) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_es.qm
%lang(et) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_et.qm
%lang(eu) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_eu.qm
%lang(fa) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_fa.qm
%lang(fi) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_fi.qm
%lang(fil) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_fil.qm
%lang(fo) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_fo.qm
%lang(fr) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_fr.qm
%lang(ga) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ga.qm
%lang(gd) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_gd.qm
%lang(gl) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_gl.qm
%lang(he) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_he.qm
%lang(hi_IN) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_hi_IN.qm
%lang(hr) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_hr.qm
%lang(hu) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_hu.qm
%lang(hy) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_hy.qm
%lang(id) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_id.qm
%lang(ig) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ig.qm
%lang(it) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_it.qm
%lang(ja) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ja.qm
%lang(ka) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ka.qm
%lang(kab) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_kab.qm
%lang(ko) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ko.qm
%lang(lt) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_lt.qm
%lang(lv) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_lv.qm
%lang(ml) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ml.qm
%lang(mn_MN) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_mn_MN.qm
%lang(mt) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_mt.qm
%lang(nb) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_nb.qm
%lang(nl) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_nl.qm
%lang(nn) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_nn.qm
%lang(pl) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_pl.qm
%lang(pt) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_pt.qm
%lang(pt_BR) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_pt_BR.qm
%lang(ro) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ro.qm
%lang(ru) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_ru.qm
%lang(scn) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_scn.qm
%lang(sk) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_sk.qm
%lang(sl) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_sl.qm
%lang(sr) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_sr.qm
%lang(sr_RS) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_sr_RS.qm
%lang(sv) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_sv.qm
%lang(sv_SE) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_sv_SE.qm
%lang(th) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_th.qm
%lang(tr) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_tr.qm
%lang(uk) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_uk.qm
%lang(uz@Latn) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_uz@Latn.qm
%lang(vi) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_vi.qm
%lang(zh_CN) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_zh_CN.qm
%lang(zh_HK) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_zh_HK.qm
%lang(zh_TW) %{_datadir}/mscore-%{musescore_maj}/locale/musescore_zh_TW.qm
%lang(bg) %{_datadir}/mscore-%{musescore_maj}/locale/qt_bg.qm
%lang(el) %{_datadir}/mscore-%{musescore_maj}/locale/qt_el.qm
%lang(eu) %{_datadir}/mscore-%{musescore_maj}/locale/qt_eu.qm
%lang(gd) %{_datadir}/mscore-%{musescore_maj}/locale/qt_gd.qm
%lang(id) %{_datadir}/mscore-%{musescore_maj}/locale/qt_id.qm
%lang(lv) %{_datadir}/mscore-%{musescore_maj}/locale/qt_lv.qm
%lang(nb) %{_datadir}/mscore-%{musescore_maj}/locale/qt_nb.qm
%lang(nl) %{_datadir}/mscore-%{musescore_maj}/locale/qt_nl.qm
%lang(nl_BE) %{_datadir}/mscore-%{musescore_maj}/locale/qt_nl_BE.qm
%lang(pt_BR) %{_datadir}/mscore-%{musescore_maj}/locale/qt_pt_BR.qm
%lang(ro) %{_datadir}/mscore-%{musescore_maj}/locale/qt_ro.qm
%lang(tr) %{_datadir}/mscore-%{musescore_maj}/locale/qt_tr.qm
%lang(vi) %{_datadir}/mscore-%{musescore_maj}/locale/qt_vi.qm

%files soundfont
%doc share/sound/MS?Basic_Readme.md share/sound/MS_Basic_Changelog.md
%license share/sound/MS?Basic_License.md
%{_datadir}/mscore-%{musescore_maj}/sound
%{_datadir}/soundfonts/*.sf3

%fontfiles -z 1
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/MScore/
%{_datadir}/SMuFL/Fonts/Emmentaler

%fontfiles -z 2

%fontfiles -z 3

%fontfiles -z 4

%fontfiles -z 5

%fontfiles -z 6
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/MuseJazz/

%fontfiles -z 7

%fontfiles -z 8
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/Gootville/
%{_datadir}/SMuFL/Fonts/Gonville

%fontfiles -z 9

%changelog
%autochangelog
