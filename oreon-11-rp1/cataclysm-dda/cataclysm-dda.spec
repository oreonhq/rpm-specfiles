%global source0_hash none
%global _lto_cflags %nil
Name:           cataclysm-dda
Version:        0.H
Release:        3%{?dist}
Summary:        Turn-based survival game set in a post-apocalyptic world
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://cataclysmdda.org
Source0:        Cataclysm-DDA-0.H-RELEASE.tar.gz
Patch0:         const_compile_fix.patch
ExcludeArch:    i686
Requires:       %{name}-data = %{version}-%{release}
Recommends:     %{name}-tiles%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  astyle
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl2)
# /oreon:deps
%description
Cataclysm - Dark Days Ahead. A turn-based survival game set in a
post-apocalyptic world.

Roguelike set in a post-apocalyptic world. While some have described it as a
"zombie game", there is far more to Cataclysm than that. Struggle to survive in
a harsh, persistent, procedurally generated world. Scavenge the remnants of a
dead civilization for food, equipment, or, if you are lucky, a vehicle with a
full tank of gas to get you the hell out of Dodge. Fight to defeat or escape
from a wide variety of powerful monstrosities, from zombies to giant insects to
killer robots and things far stranger and deadlier, and against the others like
yourself, who want what you have...

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    data
Data files for %{name}.

%package        tiles
Summary:        %{name} version with gfx and sound
Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-tiles-data = %{version}-%{release}
%description    tiles
%{name} version with gfx and sound.

%package        tiles-data
Summary:        Data files for %{name}-tiles
BuildArch:      noarch
Requires:       %{name}-tiles = %{version}-%{release}
Requires:       hicolor-icon-theme
Provides:       bundled(fixedsys)
Provides:       bundled(square)
Provides:       bundled(Square-Smallcaps)
Provides:       bundled(unifont-fonts) = 12.0.01
%description    tiles-data
Data files for %{name}-tiles.

%prep
%global oreon_srcdir Cataclysm-DDA-0.H-RELEASE
%oreon_prep
%build

%ifarch armv7hl
%define _lto_cflags %{nil}
%endif
%set_build_flags
%make_build \
    PREFIX=%{_prefix} \
    USE_HOME_DIR=1 \
    PCH=0 \
    RUNTESTS=0 \
    %if %{with release_build}
    RELEASE=1 \
    %{nil}
    %endif
%make_build \
    PREFIX=%{_prefix} \
    SOUND=1 \
    TILES=1 \
    USE_HOME_DIR=1 \
    RUNTESTS=0 \
    %if %{with release_build}
    RELEASE=1 \
    %{nil}
    %endif
%install
%make_install \
    PREFIX=%{_prefix} \
    USE_HOME_DIR=1 \
    PCH=0 \
    RUNTESTS=0 \
    %if %{with release_build}
    RELEASE=1 \
    %{nil}
    %endif
%make_install \
    PREFIX=%{_prefix} \
    SOUND=1 \
    TILES=1 \
    USE_HOME_DIR=1 \
    RUNTESTS=0 \
    %if %{with release_build}
    RELEASE=1 \
    %{nil}
    %endif
rm %{buildroot}%{_datadir}/%{name}/font/Terminus.ttf
rm -r %{buildroot}%{_datadir}/%{name}/LICENSE-OFL-Terminus-Font.txt
rm      %{buildroot}%{_datadir}/%{name}/LICENSE.txt
rm      %{buildroot}%{_datadir}/%{name}/changelog.txt
%oreon_autofiles cataclysm-dda-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cataclysm-dda-tiles usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cataclysm-dda-tiles-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n cataclysm-dda-data -f %{oreon_filedir}/cataclysm-dda-data.list
%files -n cataclysm-dda-tiles -f %{oreon_filedir}/cataclysm-dda-tiles.list
%files -n cataclysm-dda-tiles-data -f %{oreon_filedir}/cataclysm-dda-tiles-data.list

%changelog

%autochangelog
