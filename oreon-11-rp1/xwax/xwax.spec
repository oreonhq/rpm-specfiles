%global source0_hash 589144364d0fea2cc7cbbc21ded25fd376c4c71819a126b8f5864e76eaebcdf3
Name:           xwax
Version:        1.10
Release:        1%{?dist}
Summary:        Open source vinyl emulation software for Linux
License:        GPL-2.0-only
URL:            https://www.xwax.org
Source0:        https://xwax.org/releases/%{name}-%{version}.tar.gz
Requires: sox cdparanoia
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  make
# /oreon:deps
%description
xwax is open-source vinyl emulation software for Linux. 
It allows DJs and turntablists to playback digital audio files 
(MP3, Ogg Vorbis, FLAC, AAC and more), controlled using a normal
pair of turntables via timecoded vinyls.

It's designed for both beat mixing and scratch mixing. Needle drops, pitch 
changes, scratching, spinbacks and rewinds are all supported, and feel just
like the audio is pressed onto the vinyl itself.

The focus is on an accurate vinyl feel which is efficient, stable and fast.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags} ALSA=yes JACK=yes PREFIX=%{_prefix} EXECDIR=%{_libexecdir}/%{name}
%install
make ALSA=yes JACK=yes install PREFIX=%{buildroot}/%{_prefix} EXECDIR=%{buildroot}/%{_libexecdir}/%{name} DOCDIR=/tmp
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
