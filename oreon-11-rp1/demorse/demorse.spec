%global source0_hash cc4f962afb3fc4b4f65cc7ce362147022bf993bc2e85e349d7b6b4656a06c43c
Name:		demorse
Version:	1.2
Release:        28%{?dist}
Summary:        Command line tool for decoding Morse code signals
License:	GPL-2.0-or-later
URL:		http://www.qsl.net/5b4az/pages/morse.html
Source0:        http://www.qsl.net/5b4az/pkg/morse/%{name}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
demorse is a non-interactive command line tool for decoding Morse code signals
into text. demorse detects the "dihs" and "dahs" that make a Morse code
character via the computer's sound card, which can be connected to a radio
receiver tuned to a CW Morse code transmission or to a tone generator.

The input signal is processed by a Goertzel tone detector which produces "mark"
or "space" (signal/no signal) outputs and the resulting stream of Morse code
"elements" is decoded into an ASCII character for printing to the screen.
Currently demorse is a non- interactive command line tool for the console and
decoded Morse signals are sent to stdout.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
