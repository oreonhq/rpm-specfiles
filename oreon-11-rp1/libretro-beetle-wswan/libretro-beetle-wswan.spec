%global source0_hash 457028d9ec6e76e0ec3e2e69a40b1bac392dae4fa4aca724c8a1500dbc54fc8c

%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 32bf70a3032a138baa969c22445f4b7821632c30
%global corename beetle-wswan

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.8.%autorelease
Summary:        Standalone port of Mednafen WonderSwan to libretro, itself a fork of Cygne

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_wswan.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}

%install
%make_install         \
    libdir=%{_libdir} \
    prefix=%{_prefix} \
    %{nil}
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_wswan.libretro

%files
%license COPYING
%{_libdir}/libretro/

%changelog
%autochangelog
