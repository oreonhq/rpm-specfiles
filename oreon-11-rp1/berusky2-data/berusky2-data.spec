%global source0_hash c69ea72cf3c242f1c75913b0753ffcf801631f5c594685aa7e51edd5186707fe
%global game_name berusky2
Summary:        A datafile for Berusky
Name:           berusky2-data
Version:        0.12
Release:        16%{?dist}
License:        GPL-2.0-or-later
Source0:        http://downloads.sourceforge.net/%{game_name}/%{name}-%{version}.tar.xz
URL:            http://www.anakreon.cz/en/Berusky2.htm
BuildArch:      noarch
# oreon:deps

# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
