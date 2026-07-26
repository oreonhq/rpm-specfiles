%global source0_hash e86f9f6f1f9fb0b8b67578b52364e35f84390b3e50f17ab983cf35431b41cb59

Name:       fapg
Version:    0.45
Release:    %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
Summary:    Fast Audio Playlist Generator
URL:        http://royale.zerezo.com/fapg/
Source:     http://royale.zerezo.com/fapg/%{name}-%{version}.tar.gz
BuildRequires: uriparser-devel
BuildRequires: gcc
BuildRequires: make

%description
FAPG means Fast Audio Playlist Generator.
It is a tool to generate list of audio files (Wav, MP3, Ogg, etc)
in various formats (M3U, PLS, HTML, etc).
It is very useful if you have a large amount of audio files 
and you want to quickly and frequently build a playlist.

It is coded in C to be as fast as possible, and does not use 
any specific audio library (like ID3Lib).
This allow you to deploy it faster and easier, and to have 
better performances since the less informations are loaded.
In the other hand, this tool is not (yet) compatible with 
all the known formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
