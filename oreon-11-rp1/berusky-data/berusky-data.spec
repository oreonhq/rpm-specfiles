%global source0_hash be6d99f40d65341b32b381c004f32885e3dc114b76a95efbc4c5057ea524401e

%define game_name berusky

Summary:        A datafile for Berusky
Name:           berusky-data
Version:        1.7
Release:        27%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source:         http://www.anakreon.cz/download/berusky/tar.gz/%{name}-%{version}.tar.gz
URL:            http://www.anakreon.cz/
BuildArch:      noarch

%description
A datafile for Berusky. Berusky is a 2D logic game based on an ancient 
puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic 
items such as explosives, stones, special gates and so on. 
In addition, up to five bugs can cooperate and be controlled by the player.

This package contains a data for the game, i.e. files with graphics, levels,
game rules and configuration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{game_name}

cp -r GameData %{buildroot}%{_datadir}/%{game_name}
cp -r Graphics %{buildroot}%{_datadir}/%{game_name}
cp -r Levels   %{buildroot}%{_datadir}/%{game_name}
cp README   %{buildroot}%{_datadir}/%{game_name}
cp COPYING  %{buildroot}%{_datadir}/%{game_name}

mkdir -p %{buildroot}/var/games/%{game_name}
install -m 644 berusky.ini %{buildroot}/var/games/%{game_name}

%files
%dir %{_datadir}/%{game_name}
%{_datadir}/%{game_name}/*
%dir /var/games/%{game_name}
/var/games/%{game_name}/*

%changelog
%autochangelog
