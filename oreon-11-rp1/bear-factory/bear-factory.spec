%global source0_hash 1b174deb53e0231a9438e8a3b6ee379361bbeedfd8db288fa8f7504873f5709a
%global commit0 2a785228d85997dc1682ee71899841528fa09c33
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global srcname bear
Name:           %{srcname}-factory
Version:        0.7.0
Release:        1%{?dist}
Summary:        Game engine and editors dedicated to creating great 2D games
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/j-jorge/bear
Source0:        https://github.com/j-jorge/%{srcname}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         bear-engine-boost.patch
Patch1:         0001-Fix-text_layout-compute_line_width.patch
Patch2:         0002-Fix-text_metric-issues.patch
Patch3:         0003-gl_renderer-Protect-pause-unpause-against-unbalanced.patch
Patch4:         0004-sound_manager-Fix-segmentation-fault-due-to-invalid-.patch
Patch5:         0005-world-Fix-assertion-failure-in-physical_item-set_own.patch
Patch6:         bear-boost190.patch
ExcludeArch:    ppc64le
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libclaw-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  wxGTK-devel
# /oreon:deps
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

export CMAKE_POLICY_VERSION_MINIMUM=3.5
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
install -dm 755 %{buildroot}%{_includedir}/%{name}/cmake-helper/
install -D cmake-helper/{*.cmake,*.cmake.in} %{buildroot}%{_includedir}/%{name}/cmake-helper/
for file in $(find bear-engine/{core,lib}/src -name *.hpp -o -name *.tpp);
do
    install -Dm 0644 $file %{buildroot}%{_includedir}/%{name}/$file
done
chmod a-x %{buildroot}%{_includedir}/%{name}/cmake-helper/*.cmake*
rm -rf %{buildroot}%{_datadir}/pixmaps
install -d -m 0755 %{buildroot}%{_datadir}/applications/
install -Dm644 %{_builddir}/%{srcname}-%{commit0}/bear-factory/desktop/applications/*.desktop %{buildroot}%{_datadir}/applications/
%oreon_autofiles bear-engine usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bear-factory-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n bear-engine -f %{oreon_filedir}/bear-engine.list
%files -n bear-factory-devel -f %{oreon_filedir}/bear-factory-devel.list

%changelog

%autochangelog
