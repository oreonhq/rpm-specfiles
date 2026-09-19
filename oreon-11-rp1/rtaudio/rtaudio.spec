%global source0_hash 42d29cc2b5fa378ba3a978faeb1885a0075acf0fecb5ee50f0d76f6c7d8ab28c

Name:           rtaudio
Version:        6.0.1
Release:        4%{?dist}
Summary:        Real-time Audio I/O Library

License:        MIT
URL:            http://www.music.mcgill.ca/~gary/rtaudio/
Source0:        https://www.music.mcgill.ca/~gary/%{name}/release/%{name}-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel

%description
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:

  * object-oriented C++ design
  * simple, common API across all supported platforms
  * allow simultaneous multi-api support
  * support dynamic connection of devices
  * provide extensive audio device parameter control
  * allow audio device capability probing
  * automatic internal conversion for data format, channel number compensation,
    (de)interleaving, and byte-swapping

%package devel
Summary:        Real-time Audio I/O Library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:

  * object-oriented C++ design
  * simple, common API across all supported platforms
  * allow simultaneous multi-api support
  * support dynamic connection of devices
  * provide extensive audio device parameter control
  * allow audio device capability probing
  * automatic internal conversion for data format, channel number compensation,
    (de)interleaving, and byte-swapping

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Fix encoding issues
for file in tests/teststops.cpp; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
export CFLAGS="%optflags -fPIC"
%configure --with-jack --with-alsa --with-pulse --enable-shared --disable-static --verbose
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%license doc/doxygen/license.txt
%doc README.md doc/release.txt
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/html doc/images
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
