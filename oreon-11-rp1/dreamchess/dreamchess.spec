%global source0_hash b070a34acf69ed92e523902683d104abb295d78b6f37663f4668e929b9e90470
%undefine __cmake_in_source_build
%global engine  dreamer
Name:           dreamchess
Version:        0.3.0%{?cdate0:~%{cdate0}git}
Release:        1%{?dist}
Summary:        Portable chess game
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://www.%{name}.org/
%if 0%{?cdate0}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%else
%endif
Requires:       hicolor-icon-theme
Requires:       chessprogram
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  help2man
BuildRequires:  libappstream-glib
# /oreon:deps
%description
DreamChess is an open source chess game.

Features:
- 3D OpenGL graphics
- various chess board sets: from classic wooden to flat figurines
- music, sound effects
- on-screen move lists using SAN notation
- undo functionality
- save-games in PGN format

A moderately strong chess engine as a sub-package: Dreamer.

%package engine
Summary:        A moderately strong chess engine for the game DreamChess
License:        GPL-3.0-or-later
Provides:       chessprogram
%description engine
Should this chess engine be too weak for you, then you can use any other
XBoard-compatible chess engine, including the popular Crafty and GNU Chess.

%package data
Summary:        Data files for the game DreamChess
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description data
Data files for the game DreamChess:
Boards, Pieces, Sounds, Styles, Themes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{?cdate0:-n %{name}-%{commit0}}

%build

%cmake \
 -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}
%cmake_build
help2man -o %{name}.1 --no-discard-stderr \
 --version-string='%{version}' -v'%{release}' \
 %{_vpath_builddir}/%{name}/src/%{name}
%install
%cmake_install
install -D -t %{buildroot}%{_mandir}/man1 %{name}.1
mkdir -p %{buildroot}%{_metainfodir}
cat <<EOF > %{buildroot}%{_metainfodir}/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>org.dreamchess.dreamchess</id>
    <name>DreamChess</name>
    <summary>Portable Chess Game</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-3.0-or-later</project_license>
    <description>
        <p>
            DreamChess is an open source chess game. DreamChess features 3D 
            OpenGL graphics and provides various chess board sets, ranging from 
            classic wooden to flat figurines.
        </p>
        <p>
            A moderately strong chess engine is included: Dreamer. However,
            should this engine be too weak for you, then you can use any other 
            XBoard-compatible chess engine, including GNU Chess.
        </p>
        <p>
            Other features include music, sound effects, on-screen move lists 
            using SAN notation, undo functionality, and savegames in PGN format.
        </p>
    </description>
    <launchable type="desktop-id">%{name}.desktop</launchable>
    <provides>
        <binary>%{name}</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>DreamChess project</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <screenshots>
        <screenshot type="default">
            <caption>Classic Wooden theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/classic.png</image>
        </screenshot>
        <screenshot>
            <caption>Opposing Elements theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/elements.png</image>
        </screenshot>
        <screenshot>
            <caption>Figurine theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/figurine.png</image>
        </screenshot>
        <screenshot>
            <caption>Sketch theme</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/sketch.png</image>
        </screenshot>
        <screenshot>
            <caption>Title screen</caption>
            <image>https://www.dreamchess.org/assets/images/screenshots/title.png</image>
        </screenshot>
    </screenshots>
    <url type="homepage">%{url}</url>
</component>
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n dreamchess-engine -f %{oreon_filedir}/dreamchess-engine.list
%files -n dreamchess-data -f %{oreon_filedir}/dreamchess-data.list

%changelog

%autochangelog
