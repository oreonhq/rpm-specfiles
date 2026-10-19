%global source0_hash 0e7020ba46c0af14e95bffb0c5bcd34c729e993644207547910b3d1f2d063862
%global build_type_safety_c 2
Name:    soundtracker
Version: 1.0.5
Release:        1%{?dist}
Summary:        Sound module composer/player
License:   GPL-2.0-or-later
URL:       http://www.soundtracker.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:    soundtracker-1.0.2.1-else.patch
Patch1:    soundtracker-1.0.5-gcc15.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libxml2-devel
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
Soundtracker is a module tracker for the X Window System similar to
the DOS program `FastTracker'. Soundtracker is based on the XM file
format. The user interface makes use of GTK2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build

%configure
%make_build
%install
%make_install
%find_lang soundtracker
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
