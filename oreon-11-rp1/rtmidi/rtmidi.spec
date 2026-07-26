%global source0_hash 48db0ed58c8c0e207b5d7327a0210b5bcaeb50e26387935d02829239b0f3c2b9

Name:       rtmidi
Version:    5.0.0
Release:    6%{?dist}
Summary:    Library for realtime MIDI input/output (ALSA support)
License:    MIT
URL:        https://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:    https://www.music.mcgill.ca/~gary/rtmidi/release/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  alsa-lib-devel, pkgconfig(jack)
BuildRequires:  autoconf, automake, libtool, /usr/bin/dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc-c++
Obsoletes:  %{name}-jack < 2.0.0

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

# Get rid of the -L/usr/lib in the output of this convenience script
sed -i -E 's/-L[^ "]+//' %{name}-config

%install
make DESTDIR=%{buildroot} install

install --verbose -D -t %{buildroot}%{_bindir} %{name}-config

rm %{buildroot}%{_libdir}/lib%{name}.{a,la}

%ldconfig_scriptlets

%files
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/html
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
