%global source0_hash 1b174deb53e0231a9438e8a3b6ee379361bbeedfd8db288fa8f7504873f5709a

# https://github.com/j-jorge/bear/commit/2a785228d85997dc1682ee71899841528fa09c33
%global commit0 2a785228d85997dc1682ee71899841528fa09c33
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global srcname bear

Name:           %{srcname}-factory
Version:        0.7.0
Release:        0.54.20200220git%{shortcommit0}%{?dist}
Summary:        Game engine and editors dedicated to creating great 2D games
# Automatically converted from old format: GPLv3+ and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/j-jorge/bear
Source0:        https://github.com/j-jorge/bear/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# Boost 1.73 support
Patch0:         bear-engine-boost.patch
# Various crash fixes from https://github.com/jwrdegoede/bear
Patch1:         0001-Fix-text_layout-compute_line_width.patch
Patch2:         0002-Fix-text_metric-issues.patch
Patch3:         0003-gl_renderer-Protect-pause-unpause-against-unbalanced.patch
Patch4:         0004-sound_manager-Fix-segmentation-fault-due-to-invalid-.patch
Patch5:         0005-world-Fix-assertion-failure-in-physical_item-set_own.patch
# Boost 1.90 support https://github.com/j-jorge/bear/issues/15
Patch6:         bear-boost190.patch

# Build is broken on ppc64le
ExcludeArch:    ppc64le

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  libclaw-devel >= 1.7.4-17
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  wxGTK-devel
Requires:       hicolor-icon-theme

%description
The Bear engine is a set of C++ libraries and tools dedicated to creating
great 2D games. It has been used to create Plee the Bear (plee-the-bear),
Andy's Super Great Park (asgp) and Tunnel (tunnel).

The engine comes with a set of tools, namely the Bear Factory, intended to
help creating resources for the game. These tools include a level editor,
a character/model editor and an animation editor.

%package -n %{srcname}-engine
Summary: Run-time libraries for games based on the Bear engine

%description -n %{srcname}-engine
The Bear engine is a set of C++ libraries and tools dedicated to creating
great 2D games. It has been used to create Plee the Bear (plee-the-bear),
Andy's Super Great Park (asgp) and Tunnel (tunnel).

This package contains the run-time libraries used by the games based on
the Bear engine.

%package devel
Summary: Development files for %{name}
Requires: %{srcname}-engine%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{commit0}

# change docbook_to_man to docbook2man
sed -i -e 's|docbook-to-man|docbook2man|g' cmake-helper/docbook-to-man.cmake

# delete glew code because it picks up BSD license
rm -rf bear-engine/core/src/visual/glew/

%build
# TODO: Please submit an issue to upstream (rhbz#2380474)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# https://github.com/j-jorge/bear/issues/9
# The Bear Factory (i.e. the editors for the Bear Engine) requires wiWidgets < 3.
# Changes in the API of wxWidgets broke some parts of the editors.
# The editor needs to be disabled with -DBEAR_EDITORS_ENABLED=0
%cmake -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} \
       -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib} \
       -DCMAKE_CXX_STANDARD=17 \
       -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
       -DCMAKE_SKIP_RPATH:BOOL=ON \
       -DBEAR_USES_FREEDESKTOP=ON \
       -DRUNNING_BEAR_ENABLED=ON \
       -DBEAR_EDITORS_ENABLED=0
%cmake_build

%install
%cmake_install

%find_lang bear-engine

# copy devel files for subpkg bear-devel
install -dm 755 %{buildroot}%{_includedir}/%{name}/cmake-helper/
install -D cmake-helper/{*.cmake,*.cmake.in} %{buildroot}%{_includedir}/%{name}/cmake-helper/
for file in $(find bear-engine/{core,lib}/src -name *.hpp -o -name *.tpp);
do
    install -Dm 0644 $file %{buildroot}%{_includedir}/%{name}/$file
done
# fixes E: script-without-shebang
chmod a-x %{buildroot}%{_includedir}/%{name}/cmake-helper/*.cmake*

rm -rf %{buildroot}%{_datadir}/pixmaps

install -d -m 0755 %{buildroot}%{_datadir}/applications/
install -Dm644 %{_builddir}/%{srcname}-%{commit0}/bear-factory/desktop/applications/*.desktop %{buildroot}%{_datadir}/applications/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE license/CCPL license/GPL
#{_bindir}/bend-image
#{_bindir}/image-cutter
#{_bindir}/bf*editor
#{_libdir}/libbear-editor.so
#{_datadir}/#{name}
#{_datadir}/icons/hicolor/*/apps/#{name}.png
%{_datadir}/applications/desc2img.desktop
%{_datadir}/applications/bf*editor.desktop
#{_mandir}/man1/bf*editor.1*

%files -n %{srcname}-engine -f %{srcname}-engine.lang
%doc README.md
%license LICENSE license/CCPL license/GPL
%{_bindir}/running-bear
%{_libdir}/libbear_*.so
#{_libdir}/libbear-editor.so
%{_mandir}/man6/running-bear.6*

%files devel
%doc README.md
%{_includedir}/%{name}
%{_datadir}/cmake/%{srcname}-engine

%changelog
%autochangelog
