%global source0_hash f1b8849d09267fff3c1f5122097d90fec261291f51b1e075f37fad8f1b7d9f92

Name:           aldo
Version:        0.7.7
Release:        19%{?dist}
Summary:        A morse tutor

License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://aldo.nongnu.org/

Source0:        http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libao-devel
BuildRequires: make

%description
Aldo is a morse code learning tool released under GPL, which provides
four type of training methods:

   1. Classic exercise : Identify random characters played in morse code.
   2. Koch method : Two morse characters will be played at full speed
      (20wpm) until you'll be able to identify at least 90 percent of
      them. After that, one more character will be added, and so on.
   3. Read from file : Identify the morse code generated from a file.
   4. Callsign exercise : Identify random callsigns played in morse code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README THANKS
%license COPYING
%{_bindir}/*
%{_mandir}/man?/*

%changelog
%autochangelog
