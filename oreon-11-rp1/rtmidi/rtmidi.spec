%global source0_hash 48db0ed58c8c0e207b5d7327a0210b5bcaeb50e26387935d02829239b0f3c2b9
Name:       rtmidi
Version:    6.0.0
Release:        1%{?dist}
Summary:        Library for realtime MIDI input/output (ALSA support)
License:    MIT
URL:        https://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:        https://www.music.mcgill.ca/~gary/rtmidi/release/%{name}-%{version}.tar.gz
Obsoletes:  %{name}-jack < 2.0.0
# oreon:deps
BuildRequires:  /usr/bin/dos2unix
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(jack)
# /oreon:deps
%description
RtMidi is a set of C++ classes (RtMidiIn and RtMidiOut) that provides a common 
API (Application Programming Interface) for realtime MIDI input/output across 
Linux (ALSA & Jack), Macintosh OS X, Windows (Multimedia Library), and SGI 
operating systems. RtMidi significantly simplifies the process of interacting 
with computer MIDI hardware and software. It was designed with the following 
goals:
* object oriented C++ design
* simple, common API across all supported platforms
* only two header files and one source file for easy inclusion in programming 
  projects
* MIDI device enumeration

%package devel
Summary:    Development headers and libraries for rtmidi
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   alsa-lib-devel, pkgconfig(jack)
%description devel
Development headers and libraries for rtmidi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i.orig -e 's/\/lib/\/%{_lib}/' Makefile.in rtmidi.pc.in
# fix end of line
dos2unix doc/release.txt doc/doxygen/tutorial.txt

%build

%configure --docdir=%{_docdir}/%{name}-devel --with-jack --with-alsa
make %{?_smp_mflags} AM_DEFAULT_VERBOSITY=1
sed -i -E 's/-L[^ "]+//' %{name}-config
%install
make DESTDIR=%{buildroot} install
install --verbose -D -t %{buildroot}%{_bindir} %{name}-config
rm %{buildroot}%{_libdir}/lib%{name}.{a,la}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rtmidi-devel -f %{oreon_filedir}/rtmidi-devel.list

%changelog

%autochangelog
