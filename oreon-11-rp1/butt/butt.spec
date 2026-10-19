%global source0_hash d7b3a8bbbe011c337cf93c6a683071210cc39e0277f77482f94532becf126760
%global rdnn de.danielnoethen.butt
Name:           butt
Version:        1.47.0
Release:        1%{?dist}
Summary:        Broadcast using this tool
License:        GPL-2.0-or-later AND BSD-2-Clause AND MIT
URL:            https://danielnoethen.de/butt/
Source0:        https://danielnoethen.de/%{name}//release/%{version}/%{name}-%{version}.tar.gz
Patch0:         butt-headers.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  fdk-aac-free-devel
BuildRequires:  flac-devel
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  lame-devel
BuildRequires:  libX11-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libogg-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
# /oreon:deps
%description
butt (broadcast using this tool) is an easy to use, multi OS streaming tool.
It supports ShoutCast and IceCast and runs on Linux, MacOS and Windows.  The
main purpose of butt is to stream live audio data from your computers Mic or
Line input to an Shoutcast or Icecast server. Recording is also possible.  It
is NOT intended to be a server by itself or automatically stream a set of audio
files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ifv
%configure
%make_build
%install
%make_install
install -Dpm 0644 usr/share/applications/butt.desktop %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
for size in 16 22 24 32 48 64 96 128 256 512; do
    path=icons/hicolor/${size}x${size}/apps/butt.png
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done
install -Dpm 0644 usr/share/icons/hicolor/scalable/apps/butt.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/butt.svg
for size in 16 32; do
    path=pixmaps/butt$size.xpm
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done
install -Dpm 0644 usr/share/metainfo/%{rdnn}.metainfo.xml %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
