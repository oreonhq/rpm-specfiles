%global source0_hash b2a778b723ccae18ac90dd520ce9229b794086388a0e3152670ef9f6d4b9f97d

Name:             openriichi
Version:          0.2.1.1
Release:          11%{?dist}
Summary:          Japanese Mahjong 3D game
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only

Requires:         google-noto-sans-cjk-jp-fonts

%global forgeurl0 https://github.com/FluffyStuff/Engine
%global commit0   0bd410550600a2a0858ca327576bdd32116da188

%global forgeurl1 https://github.com/FluffyStuff/OpenRiichi
%global version1  %{version}

%forgemeta -a

URL:              %{forgeurl}

BuildRequires:    vala
BuildRequires:    gcc-c++
BuildRequires:    meson
BuildRequires:    libgee-devel
BuildRequires:    gtk3-devel
BuildRequires:    glew-devel
BuildRequires:    pango-devel
BuildRequires:    SDL2_image-devel
BuildRequires:    SDL2_mixer-devel
BuildRequires:    SDL2-devel
BuildRequires:    desktop-file-utils

Requires:         %{name}-data = %{version}

Source0:          %{forgesource0}
Source1:          %{forgesource1}
Source2:          %{name}.desktop

# Use lower case for executable file and game directory
Patch0:           0001-Use-lowercase-for-progam-name.patch
# Load application icon from standard directory /usr/share/pixmaps
Patch1:           0002-Change-icon-path.patch
# Load fonts provided by the system
Patch2:           0003-Use-system-fonts.patch

%global common_description %{expand:
OpenRiichi is an open source Japanese Mahjong client written in the Vala 
programming language. It supports singleplayer and multiplayer, with or without 
bots. It features all the standard riichi rules, as well as some optional ones. 
It also supports game logging, so games can be viewed again.}

%description
%{common_description}

%package data
Summary:          Data files for OpenRiichi
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}

%description data
%{common_description}

This package contains the openriichi data files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup -a
# Use system fonts instead of provided ones
rm -r Engine bin/Data/Fonts
mv ../Engine-%{commit0} Engine
mv Engine/LICENSE ENGINE_LICENSE
%autopatch -p1

%build
%global _distro_extra_cflags -Wno-int-conversion
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/pixmaps
# Move application icon to standard directory
mv %{buildroot}%{_datadir}/%{name}/Data/Icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%check
%meson_test

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc README.md CHANGELOG.md
%license LICENSE ENGINE_LICENSE

%files data
%{_datadir}/%{name}
%license LICENSE ENGINE_LICENSE

%changelog
%autochangelog
