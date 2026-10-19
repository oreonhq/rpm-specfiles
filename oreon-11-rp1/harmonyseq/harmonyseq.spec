%global source0_hash d03f81d564fe7408eeb6290a6f8690138c9e3255d4104c21b5e9d0a008539c15
Name:           harmonyseq
Summary:        MIDI sequencer designed for live performances
Version:        0.17
Release:        1%{?dist}
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://harmonyseq.wordpress.com/
%global forgeurl https://github.com/rafalcieslak/harmonySEQ
Source0:        %{forgeurl}/archive/v%{version}/harmonySEQ-%{version}.tar.gz
Patch:          harmonyseq-0.17-missing-include.patch
Patch:          harmonyseq-0.17-pr-8-metadata-improvements.patch
Patch:          %{forgeurl}/pull/12.patch
ExcludeArch:    %{ix86}
Requires:       shared-mime-info
Provides:       harmonyseq-doc = %{version}-%{release}
Conflicts:      harmonyseq-doc = 0.17-1
Obsoletes:      harmonyseq-doc < 0.17-1
%global app_id org.cielak.harmonyseq
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  appstream
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hardlink
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(liblo)
# /oreon:deps
%description
A MIDI software sequencer designed for live performances and jams.

harmonySEQ operates a number of synchronized sequencers, each with its own
pattern, repeating looped melodies of different length, duration and MIDI
channel.

Main features include:

  • support for complex polyrhythms
  • multi-pattern configuration for each sequencer
  • customizable action triggers - exceptionally useful for live performances
  • chord management system which allows to easily organize melodies that sound
    great together
  • support for sequencing MIDI control messages
  • an easy-to-use yet powerful interface, with a rich piano-roll pattern
    editor

As for now harmonySEQ works on Linux only. It uses ALSA (asound) library, and
GTKmm for graphical interface.

No official user documentation exists at the moment, but you can refer to UI
tooltips - nearly everything has a detailed explanation.

More information can be found on the project’s (dated) website:
https://harmonyseq.wordpress.com

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n harmonySEQ-%{version} -p1

%conf
# We need the preprocessor macro RELEASE set so that src/main.cpp looks for
# resoures in the installation path (DATA_PATH). Normally this is set with
# -DCMAKE_BUILD_TYPE=Release, but this also asks to strip debugging symbols,
# which we do not want. Setting -DCMAKE_BUILD_TYPE=RelWithDebInfo does not set
# the preprocessor macro. Instead, we set it manually:
CFLAGS="${CFLAGS} -DRELEASE"
CXXFLAGS="${CXXFLAGS} -DRELEASE"

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -GNinja

%build

%cmake_build
%install
%cmake_install
rm -rvf '%{buildroot}%{_datadir}/icons/gnome/192x192'
hardlink -c -v '%{buildroot}%{_datadir}/harmonySEQ'
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
appstreamcli validate --no-net --explain \
    %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
