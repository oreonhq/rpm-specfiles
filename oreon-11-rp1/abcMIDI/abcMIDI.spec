%global source0_hash 1a3a48f0f23561b77a50d81d6a834aae7536fd13c632024e34199208e14f4ba5

Name:           abcMIDI
Version:        2025.02.16
Release:        5%{?dist}
Summary:        ABC to/from MIDI conversion utilities

Group:          Applications/Multimedia
License:        GPL-2.0-or-later
URL:            https://ifdo.ca/~seymour/runabc/top.html
Source0:        https://github.com/sshlien/abcmidi/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		abcMIDI-gnu23.patch

BuildRequires:  gcc dos2unix
BuildRequires: make

%description 
The abcMIDI package contains four programs: abc2midi to convert ABC
music notation to MIDI, midi2abc to convert MIDI files to (a first
approximation to) the corresponding ABC, abc2abc to reformat and/or
transpose ABC files, and yaps to typeset ABC files as PostScript.

For a description of the ABC syntax, please see the ABC userguide
which is a part of the abcm2ps.

A mirror github repo is at https://github.com/sdgathman/abcmidi

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n abcmidi-%{version}
#find . -type f | xargs dos2unix
%patch -P 0 -p 1 -b .gnu23
# make license easier to find in files
mv doc/gpl.txt doc/LICENSE

%build
%configure
sed -i Makefile -e 's/^CC = gcc/CC = gcc --std=gnu17/'
%{make_build}

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 abc2midi %{buildroot}%{_bindir}
install -p -m 755 abcmatch %{buildroot}%{_bindir}
install -p -m 755 midi2abc %{buildroot}%{_bindir}
install -p -m 755 midicopy %{buildroot}%{_bindir}
install -p -m 755 midistats %{buildroot}%{_bindir}
install -p -m 755 abc2abc %{buildroot}%{_bindir}
install -p -m 755 mftext %{buildroot}%{_bindir}
install -p -m 755 yaps %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 doc/abc2abc.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/abc2midi.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/mftext.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/midi2abc.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/midicopy.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/midistats.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/yaps.1 %{buildroot}%{_mandir}/man1

%files
%license doc/LICENSE
%doc doc/programming VERSION doc/*.txt doc/AUTHORS doc/CHANGES
%{_mandir}/man*/*
%{_bindir}/*

%changelog
%autochangelog
