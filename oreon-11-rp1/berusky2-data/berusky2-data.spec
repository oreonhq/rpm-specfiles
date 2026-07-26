%global source0_hash none

%global game_name berusky2

Summary:        A datafile for Berusky
Name:           berusky2-data
Version:        0.12
Release:        16%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source:         http://downloads.sourceforge.net/%{game_name}/%{name}-%{version}.tar.xz
URL:            http://www.anakreon.cz/en/Berusky2.htm
BuildArch:      noarch

%description
This package contains the game data for %{game_name}, i.e. files with graphics,
levels, game rules and configuration.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/%{game_name}

mv bitmap \
   data \
   game \
   game_data \
   items \
   materials \
   out \
   textures \
   music \
   sound \
   %{buildroot}%{_datadir}/%{game_name}

%files
%{_datadir}/%{game_name}

%changelog
%autochangelog
