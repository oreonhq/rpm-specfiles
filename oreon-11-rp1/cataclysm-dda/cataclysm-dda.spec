%global source0_hash none

%global _lto_cflags %nil
Name:           cataclysm-dda
Version:        0.H
Release:        3%{?dist}
Summary:        Turn-based survival game set in a post-apocalyptic world

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://cataclysmdda.org
# https://github.com/CleverRaven/Cataclysm-DDA/archive/refs/tags/0.H-RELEASE.tar.gz
Source0:        Cataclysm-DDA-0.H-RELEASE.tar.gz
Patch0:         const_compile_fix.patch

# Due virtual memory exhausted and build fail
ExcludeArch:    i686

BuildRequires:  astyle
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ >= 7
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make

BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)

Requires:       %{name}-data = %{version}-%{release}

Recommends:     %{name}-tiles%{?_isa} = %{version}-%{release}

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
# Recommends:     unifont-fonts

# Bundled, hardcoded fonts. Tiles version doesn't work if delete.
Provides:       bundled(fixedsys)
Provides:       bundled(square)
Provides:       bundled(Square-Smallcaps)
Provides:       bundled(unifont-fonts) = 12.0.01

%description    tiles-data
Data files for %{name}-tiles.

%prep
%autosetup -n Cataclysm-DDA-0.H-RELEASE -p1

%build
%ifarch armv7hl
# This package is triggering a compiler error on armv7hl when LTO is enabled.
# Disable on armv7hl for now.
# Note: Don't use LTO for builds in COPR due to limited resources. COPR build
# will fail because of LTO.
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

# Version with gfx and sound
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

# Version with gfx and sound
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

### FIXME: Remove bundled fonts
###   * This for next builds and requires some testing
# rm -r   %{buildroot}%{_datadir}/%{name}/font
# Bug is currently preventing Terminus from working
rm %{buildroot}%{_datadir}/%{name}/font/Terminus.ttf
rm -r %{buildroot}%{_datadir}/%{name}/LICENSE-OFL-Terminus-Font.txt

# Remove duplicate license file
rm      %{buildroot}%{_datadir}/%{name}/LICENSE.txt

# Move changelog info in proper location
rm      %{buildroot}%{_datadir}/%{name}/changelog.txt

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE.txt
%doc doc/* README.md CODE_OF_CONDUCT.md data/changelog.txt
%{_bindir}/cataclysm

%files data
%{_datadir}/%{name}/cataicon.ico
%{_datadir}/%{name}/core/
%{_datadir}/%{name}/credits/
%{_datadir}/%{name}/json/
%{_datadir}/%{name}/mods/
%{_datadir}/%{name}/motd/
%{_datadir}/%{name}/names/
%{_datadir}/%{name}/raw/
%{_datadir}/%{name}/title/
%dir %{_datadir}/%{name}/

%files tiles
%{_bindir}/cataclysm-tiles

%files tiles-data
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/%{name}/font/
%{_datadir}/%{name}/fontdata.json
%{_datadir}/%{name}/gfx/
%{_datadir}/%{name}/help/
%{_datadir}/%{name}/sound/
%{_metainfodir}/*.xml

%changelog
%autochangelog
