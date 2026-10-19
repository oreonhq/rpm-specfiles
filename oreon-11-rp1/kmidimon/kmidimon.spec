%global source0_hash eb3a40fa974c6fc3b6942065d46ed9189cf6350b3a56bef178c6aea4509b1205
%global _appid net.sourceforge.kmidimon
Name:           kmidimon
Version:        1.4.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
Summary:        Drumstick MIDI monitor
URL:            https://kmidimon.sourceforge.net
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(drumstick-alsa)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pandoc
# /oreon:deps
%description
Drumstick MIDI Monitor monitors events coming from MIDI external ports or
applications via the ALSA sequencer, and from SMF (Standard MIDI files) or
WRK (Cakewalk/Sonar) files. It is especially useful if you want to debug MIDI
software or your MIDI setup. It features a nice graphical user interface,
customizable event filters and sequencer parameters, support for MIDI and ALSA
messages, and saving the recorded event list to a SMF or text file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-man --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{_appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{_appid}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
