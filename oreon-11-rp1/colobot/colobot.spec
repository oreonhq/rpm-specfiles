%global source0_hash 047eb2bc96725598d918c5b500928e3a08fa3e6e7e730a82169da4524b03ddad

Name: colobot
%global orgname info.colobot.Colobot

Version: 0.2.2
Release: 7%{?dist}
Summary: A video game that teaches programming in a fun way

License: GPL-3.0-only
URL: https://colobot.info

%global giturl https://github.com/colobot
%global gittag colobot-gold-%{version}-alpha
Source0: %{giturl}/colobot/archive/%{gittag}/colobot-%{gittag}.tar.gz
Source1: %{giturl}/colobot-data/archive/%{gittag}/colobot-data-%{gittag}.tar.gz
Source2: https://colobot.info/files/music/colobot-music_ogg_%{version}-alpha.tar.gz

# The game uses the translated string "Player" as the default player name
# yet it does not properly handle UTF-8 in player names,
# so non-English speakers may have the game always crash when putting in the player name.
#
# See: https://github.com/colobot/colobot/issues/1268 
Patch0: 0000-do-not-translate-default-player-name.patch

# Fix test compilation failure due to C++ "One Definition Rule" violation
Patch1: 0001-fix-test-compile-failure.patch

# Fix compilation failures due to GCC12 -Wrestrict warnings
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2047428
Patch2: 0002-fix-gcc12-memcpy-restrict-warnings.patch

# Fix compilation failures due to GCC15 -Wpedantic errors
Patch3: 0003-gcc15-pedantic.patch

# Tests fail on ARM architectures. Needs some investigation.
%ifarch %{arm} aarch64
%global with_tests 0
%else
%global with_tests 1
%endif

BuildRequires: cmake >= 2.8
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: po4a
BuildRequires: xmlstarlet
BuildRequires: %{_bindir}/pod2man
BuildRequires: %{_bindir}/rsvg-convert

BuildRequires: boost-devel >= 1.51
BuildRequires: boost-filesystem >= 1.51
BuildRequires: boost-regex >= 1.51
BuildRequires: gettext-devel >= 0.18
BuildRequires: glew-devel >= 1.8.0
%if %{with_tests}
BuildRequires: gtest-devel
%endif
BuildRequires: libogg-devel >= 1.3.0
BuildRequires: libpng-devel >= 1.2
BuildRequires: libsndfile-devel >= 1.0.25
BuildRequires: libvorbis >= 1.3.2
BuildRequires: openal-soft-devel >= 1.13
BuildRequires: physfs-devel
BuildRequires: python3-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_ttf-devel

Requires: colobot-data = %{version}-%{release}
Requires: colobot-music = %{version}-%{release}
Requires: hicolor-icon-theme

%description
Colobot: Gold Edition is a real-time strategy game, where you can program
your units (bots) in a language called CBOT, which is similar to C++ and Java.
Your mission is to find a new planet to live and survive.
You can save the humanity and get programming skills!

%package data
Summary: Data files for Colobot: Gold Edition
BuildArch: noarch

%description data
Data files (graphics, sounds, levels) required to run Colobot Gold.

%package music
Summary: Music for Colobot: Gold Edition
BuildArch: noarch

%description music
Music files used by Colobot Gold.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n colobot-%{gittag} -p1

# Unpack the -data tarball
rm -rf ./data
tar xzf %{SOURCE1}
mv ./colobot-data-%{gittag} ./data

# Unpack the -music tarball
pushd data/music
tar xzf %{SOURCE2}
popd

# Fix install paths
sed \
	-e 's|set(COLOBOT_INSTALL_BIN_DIR ${CMAKE_INSTALL_PREFIX}/games |set(COLOBOT_INSTALL_BIN_DIR %{_bindir}/ |' \
	-e 's|set(COLOBOT_INSTALL_LIB_DIR ${CMAKE_INSTALL_PREFIX}/lib/colobot |set(COLOBOT_INSTALL_LIB_DIR %{_libdir}/colobot |' \
	-e 's|set(COLOBOT_INSTALL_DATA_DIR ${CMAKE_INSTALL_PREFIX}/share/games/colobot |set(COLOBOT_INSTALL_DATA_DIR %{_datadir}/colobot |' \
	-e 's|set(COLOBOT_INSTALL_I18N_DIR ${CMAKE_INSTALL_PREFIX}/share/locale |set(COLOBOT_INSTALL_I18N_DIR %{_datadir}/locale |' \
	-e 's|set(COLOBOT_INSTALL_DOC_DIR ${CMAKE_INSTALL_PREFIX}/share/doc/colobot |set(COLOBOT_INSTALL_DOC_DIR %{_datadir}/doc/colobot |' \
	-i CMakeLists.txt

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DDESKTOP=ON \
	-DPORTABLE=OFF \
	-DPYTHON_EXECUTABLE=%{__python3} \
	-DUSE_RELATIVE_PATHS=OFF \
	-DTESTS=%{with_tests}
%cmake_build

%install
%cmake_install

# Change the .desktop file name to match the .appdata.xml file name
mv %{buildroot}%{_datadir}/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{orgname}.desktop
sed -e 's|%{name}.desktop|%{orgname}.desktop|' -i %{buildroot}%{_metainfodir}/%{orgname}.appdata.xml

%find_lang %{name} --with-man

%check
%if %{with_tests}
# Run unit tests. The test suite includes tests for parsing the .ini file,
# hence the test runner requires a colobot.ini file to read.
mkdir test-run-dir
cp -a --target-directory ./test-run-dir \
	test/unit/common/colobot.ini \
	%{_vpath_builddir}/colobot_ut
pushd test-run-dir
	./colobot_ut
popd
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/%{orgname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{orgname}.appdata.xml

%files -f %{name}.lang
%license LICENSE.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/

%{_datadir}/applications/%{orgname}.desktop
%{_metainfodir}/%{orgname}.appdata.xml

%{_datadir}/icons/hicolor/**/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6*

%files data
%license LICENSE.txt
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/music

%files music
%license LICENSE.txt
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/music/

%changelog
%autochangelog
