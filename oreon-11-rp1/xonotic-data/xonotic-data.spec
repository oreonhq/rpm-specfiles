%global source0_hash none

%global datadate 20230620

Summary: Game data for the Xonotic first person shooter
Name: xonotic-data
Version: 0.8.6
Release: 7%{?dist}
License: GPL-2.0-or-later
URL: http://www.xonotic.org/
# Source is custom, obtained with :
# wget http://dl.xonotic.org/xonotic-%{version}.zip
# unzip xonotic-%{version}.zip
# mkdir xonotic-data-%{version}/
# mv Xonotic/data/ Xonotic/Docs/* \
#    Xonotic/GPL* Xonotic/COPYING Xonotic/key_0.d0pk xonotic-data-%{version}/
# tar -cJf xonotic-data-%{version}.tar.xz xonotic-data-%{version}/
Source0: %{name}-%{version}.tar.xz
BuildArch: noarch

%description
Xonotic is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

Data (textures, maps, sounds and models) required to play xonotic.

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-data.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-maps.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-music.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-nexcompat.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/font-xolonium-%{datadate}.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/font-unifont-%{datadate}.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p key_0.d0pk %{buildroot}%{_datadir}/xonotic/

%files
%doc GPL* COPYING
%{_datadir}/xonotic/

%changelog
%autochangelog
