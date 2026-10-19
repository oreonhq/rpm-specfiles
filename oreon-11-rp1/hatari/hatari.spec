%global source0_hash b7dc09ebffc1b77da6837d37b116bc5a9b2fd46affff1021124101e3f6e76bc5
Summary:        An Atari ST/STE/TT/Falcon emulator suitable for playing games
Name: hatari
Version: 2.6.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://www.hatari-emu.org/
Source0:        https://framagit.org/%{name}/releases/-/raw/main/v%{version}/%{name}-%{version}.tar.bz2
Source1: %{name}.appdata.xml
Requires: hicolor-icon-theme
Requires: unzip
Requires: mtools
Requires: dosfstools
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  capstone-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  portaudio-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  readline-devel
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
# /oreon:deps
%package ui
Summary: External user interface for Hatari
Requires: %{name} = %{version}-%{release}
Requires: python3
Requires: python3-gobject
Requires: gtk3
Requires: hicolor-icon-theme
%description
Hatari is an emulator for the Atari ST, STE, TT and Falcon computers.

The Atari ST was a 16/32 bit computer system which was first released 
by Atari in 1985. Using the Motorola 68000 CPU, it was a very popular 
computer having quite a lot of CPU power at that time.

Unlike most other open source ST emulators which try to give you a good
environment for running GEM applications, Hatari tries to emulate the hardware
as close as possible so that it is able to run most of the old Atari games
and demos.  Because of this, it may be somewhat slower than less accurate
emulators.

%description ui
Hatari UI is an out-of-process user interface for the Hatari emulator and its 
built-in debugger which can (optionally) embed the Hatari emulator window. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DCMAKE_BUILD_TYPE:STRING=None \
  -DDOCDIR:PATH=%{_pkgdocdir} \
  -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
install -d -m 755 %{buildroot}%{_mandir}/fr/man1
install -p -m 644 doc/fr/hatari.1 %{buildroot}%{_mandir}/fr/man1
install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/hatariui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n hatari-ui -f %{oreon_filedir}/hatari-ui.list

%changelog

%autochangelog
