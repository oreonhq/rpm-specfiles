%global source0_hash b070a34acf69ed92e523902683d104abb295d78b6f37663f4668e929b9e90470

%undefine __cmake_in_source_build

#global commit0 5db249cfb09b40cd80a933da8aa2fb8431054a35
#global cdate0  20190318

%global engine  dreamer

Name:           dreamchess
Version:        0.3.0%{?cdate0:~%{cdate0}git}
Release:        7%{?dist}
Summary:        Portable chess game
# GPL-3.0-or-later generally for most of sources
# but BSD-3-Clause for dreamchess/src/include/gamegui/queue.h
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://www.%{name}.org/
%if 0%{?cdate0}
Source0:        https://github.com/%{name}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
%else
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  bison flex

BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  expat-devel
BuildRequires:  glew-devel
BuildRequires:  help2man
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# icons get installed into hicolor folders
Requires:       hicolor-icon-theme

Requires:       chessprogram

%if 0%{?fedora}
Suggests:       %{name}-engine
Suggests:       gnuchess
%endif

Requires:       %{name}-data = %{version}-%{release}

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

%if 0%{?fedora}
Supplements:    %{name}
%endif

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
# generate manpage
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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license LICENSE.txt
%doc README.md NEWS.md AUTHORS.txt LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man*/%{name}.*
%{_metainfodir}/%{name}.appdata.xml

%files engine
%license LICENSE.txt
%doc AUTHORS.txt
%{_bindir}/%{engine}
%{_mandir}/man*/%{engine}.*

%files data
%license LICENSE.txt
%{_datadir}/%{name}/

%changelog
%autochangelog
