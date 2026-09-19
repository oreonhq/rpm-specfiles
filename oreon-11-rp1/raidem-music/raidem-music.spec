%global source0_hash none

Name:           raidem-music
Version:        1.0
Release:        33%{?dist}
Summary:        Background music for the game raidem
# Automatically converted from old format: CC-BY - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY
URL:            http://www.dilvie.com/
Source0:        http://www.dilvie.com/music/dilvie_-_the_dragonfly.ogg
# transcoded from: http://www.dilvie.com/music/dilvie_-_up_in_ashes.mp3
Source1:        dilvie_-_up_in_ashes.ogg
Source2:	http://www.dilvie.com/music/dilvie_-_half_baked.ogg
Source3:        http://www.dilvie.com/music/dilvie_-_east_of_the_sun.ogg
Source4:        license.txt
Buildarch:      noarch
Requires:       raidem >= 0.3.1

%description
Music created by Eric Hamilton (dilvie) for the game Raid'em

%prep
%setup -q -c -T
cp %{SOURCE4} .

%build
# nothing todo content only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/menu
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/raidem/music/menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level1
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level2
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level2
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level3
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level3

%files
%doc license.txt
%{_datadir}/raidem/music

%changelog
%autochangelog
