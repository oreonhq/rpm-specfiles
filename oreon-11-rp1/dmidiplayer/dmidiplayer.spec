%global source0_hash 37f2812739b5a722f4a2ed033d2f18b3b74320db34e00c44c86bd6b060b9def6
%global appid   net.sourceforge.dmidiplayer
Name:           dmidiplayer
Version:        1.7.5
Release:        1%{?dist}
Summary:        Drumstick MIDI Player
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://dmidiplayer.sourceforge.io/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(drumstick-file)
BuildRequires:  cmake(drumstick-rt)
BuildRequires:  cmake(drumstick-widgets)
BuildRequires:  cmake(uchardet)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pandoc
# /oreon:deps
%description
This application is a multiplatform MIDI file player. It reads .MID (Standard
MIDI Files), .KAR (Karaoke), .RMI (RIFF MIDI), and .WRK (Cakewalk) file formats,
and outputs MIDI events to hardware MIDI ports and also software synths.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp examples/README.md LICENSE.examples

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
