# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2621acaa1c78e4abdb24bdd163230cc577e61276936d6aa6e3180582142f0343
%global source1_hash f4bb97303e5609a9609573955db75fd4cac75ccd18bb1e49180b4996d88660bd
%global source2_hash 976e1d3a51d82b9ff74d96f2d08b6d06cedea99654edc3ee304fc5c50ae0ceb6
%global source3_hash 1934a1b841d7aede4fa0e6d4e518dc2d143125de14ce63d8d2f0868b8804c5b7
%global source4_hash 7f4f6a686caecc300680a75d6e545ecd3625cdb07e0551e491abcf8c31fe4021
%global source5_hash a09ab83735ed1ae4c074cfdfe6edd0ec0d21f73e3c1cb39140cfecad641e1723
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           fluid-soundfont
Version:        3.1
Release:        1%{?dist}
Summary:        Pro-quality GM/GS soundfont
License:        MIT
URL:            http://www.hammersound.com/cgi-bin/soundlink.pl?action=view_category&category=Collections&ListStart=0&ListLength=20
Source0:        http://ftp.de.debian.org/debian/pool/main/f/%{name}/%{name}_%{version}.orig.tar.gz
Source1:        Fluid_R3_Readme.pdf
Source2:        timidity++.cfg
Source3:        fluid3gm.cfg
Source4:        fluid3gs.cfg
Source5:        fluid_altassign.cfg
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  soundfont-utils

%define common_description \
FluidR3 is the third release of Frank Wen's pro-quality GM/GS soundfont.\
The soundfont has lots of excellent samples, including all the GM instruments\
along side with the GS instruments that are recycled and reprogrammed versions\
of the GM presets.

%description
%common_description

%package common
Summary:        Common files for FluidR3 soundfont

%description common
%common_description

This package contains common files shared among all FluidR3 soundfont packages.

%package gm
Summary:        Pro-quality General Midi soundfont
Requires:       %{name}-common = %{version}-%{release}
Provides:       soundfont2
Provides:       soundfont2-default
Conflicts:      timidity++ <= 2.13.2-30.cvs20111110%{?dist}

%description gm
%common_description

This package contains Fluid General Midi (GM) soundfont in soundfont 2.0 (.sf2)
format.

%package gs
Summary:        Pro-quality General Standard Extension soundfont
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-gm = %{version}-%{release}
Provides:       soundfont2

%description gs
%common_description

This package contains instruments belonging to General Midi's General Standard
(GS) Extension in soundfont 2.0 (.sf2) format.

%package lite-patches
Summary:        Pro-quality General Midi soundfont in GUS patch format
Requires:       %{name}-common = %{version}-%{release}
Provides:       timidity++-patches = 5
Obsoletes:      timidity++-patches < 5
Obsoletes:      PersonalCopy-Lite-patches < 5

%description lite-patches
%common_description

This package contains Fluid General Midi (GM) soundfont in Gravis Ultrasound
(GUS) patch (.pat) format.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -
%setup -q
cp -a %{SOURCE1} .

%build
unsf -v -s -m FluidR3_GM.sf2
unsf -v -s -m FluidR3_GS.sf2

for bank in GM-B{8,9,16} Standard{1,2,3,4,5,6,7} Room{1,2,3,4,5,6,7} Power{1,2,3} Jazz{1,2,3,4} Brush{1,2}; do
   sed -i "/$bank/d" FluidR3_GM.cfg
   rm -fr *$bank*
done

cat FluidR3_GM.cfg FluidR3_GS.cfg > FluidR3.cfg

sed -i 's|FluidR3_GM-|%{_datadir}/soundfonts/%{name}-lite-patches/FluidR3_GM-|g' FluidR3.cfg
sed -i 's|FluidR3_GS-|%{_datadir}/soundfonts/%{name}-lite-patches/FluidR3_GS-|g' FluidR3.cfg

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/soundfonts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/sounds/sf2
install -p -m 644 FluidR3_GM.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts
install -p -m 644 FluidR3_GS.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts
ln -s FluidR3_GM.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts/default.sf2
ln -s ../../soundfonts/default.sf2 $RPM_BUILD_ROOT%{_datadir}/sounds/sf2

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 %{SOURCE3} %{SOURCE4} %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/soundfonts

mkdir -p $RPM_BUILD_ROOT%{_datadir}/soundfonts/%{name}-lite-patches
cp -a FluidR3_GM-* $RPM_BUILD_ROOT%{_datadir}/soundfonts/%{name}-lite-patches
cp -a FluidR3_GS-* $RPM_BUILD_ROOT%{_datadir}/soundfonts/%{name}-lite-patches
install -p -m 644 FluidR3.cfg $RPM_BUILD_ROOT%{_sysconfdir}/timidity.cfg

%files common
%doc COPYING README *Readme*
%dir %{_datadir}/soundfonts/

%files gm
%{_sysconfdir}/timidity++.cfg
%{_datadir}/soundfonts/FluidR3_GM.sf2
%{_datadir}/soundfonts/default.sf2
%{_datadir}/soundfonts/fluid3gm.cfg
%{_datadir}/soundfonts/fluid_altassign.cfg
%{_datadir}/sounds/sf2

%files gs
%{_datadir}/soundfonts/FluidR3_GS.sf2
%{_datadir}/soundfonts/fluid3gs.cfg

%files lite-patches
%config %{_sysconfdir}/timidity.cfg
%{_datadir}/soundfonts/%{name}-lite-patches/

%changelog
%autochangelog
