%global source1_hash 8c7b0c9e4b407960c6eb95e1f29d910c5c65f1c111fe6940aa6535fe0eb8e972
%global source0_hash 457028d9ec6e76e0ec3e2e69a40b1bac392dae4fa4aca724c8a1500dbc54fc8c
%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 32bf70a3032a138baa969c22445f4b7821632c30
%global corename beetle-wswan
Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        1%{?dist}
Summary:        Standalone port of Mednafen WonderSwan to libretro, itself a fork of Cygne
License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{corename}-libretro-%{commit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_wswan.libretro
Supplements:    gnome-games
Supplements:    retroarch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
