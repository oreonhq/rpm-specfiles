%global source0_hash 9bed8fa143182818650361f49257755bf891f143161066aaa7bca8c6cce9f632

Name:           xwax
Version:        1.9
Release:        8%{?dist}
Summary:        Open source vinyl emulation software for Linux
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://www.xwax.org
Source0:        https://xwax.org/releases/%{name}-%{version}.tar.gz

BuildRequires: alsa-lib-devel
BuildRequires: make
BuildRequires: gcc
BuildRequires: SDL-devel SDL_ttf-devel jack-audio-connection-kit-devel
Requires: sox cdparanoia

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

%autosetup

%build
%configure
make %{?_smp_mflags} ALSA=yes JACK=yes PREFIX=%{_prefix} EXECDIR=%{_libexecdir}/%{name}

# Note even though xwax is a GUI application I don't think it deserves a .desktop file because the program
# is entirely controlled through keyboard and it's options are only adjustable on the command line
# Options depend on the hardware that the user has available and can't be known ahead of time.

%install
make ALSA=yes JACK=yes install PREFIX=%{buildroot}/%{_prefix} EXECDIR=%{buildroot}/%{_libexecdir}/%{name} DOCDIR=/tmp

%files
%{_bindir}/xwax
%{_libexecdir}/xwax/
%doc CHANGES COPYING README
%doc %{_mandir}/man1/xwax.1.gz

%changelog
%autochangelog
