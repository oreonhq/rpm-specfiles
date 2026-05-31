%global source0_hash 3dda3c9ab1e287f15028c010a66ab7145fa855dfa62763538f341e70b4d10abd

Name:           soundtouch
Version:        2.4.0
Release:        3%{?dist}
Summary:        Audio Processing library for changing Tempo, Pitch and Playback Rates
License:        LGPL-2.1-or-later
URL:            http://www.surina.net/soundtouch/

Source0:        https://codeberg.org/soundtouch/soundtouch/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
SoundTouch is a LGPL-licensed open-source audio processing library for
changing the Tempo, Pitch and Playback Rates of audio streams or
files. The SoundTouch library is suited for application developers
writing sound processing tools that require tempo/pitch control
functionality, or just for playing around with the sound effects.

The SoundTouch library source kit includes an example utility
SoundStretch which allows processing .wav audio files from a
command-line interface.


%package devel
Summary:  Libraries, includes, etc to develop soundtouch applications
Requires: soundtouch = %{version}-%{release}
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop soundtouch applications.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}


%build
%cmake
%cmake_build


%install
%cmake_install

# pkgconfig compat links for compat with older (API compatible) releases
# dunno why upstream keeps changing the pkgconfig name
# Update 2016-02-13: now looks like that is soundtouch.pc without version
ln -s soundtouch.pc %{buildroot}%{_libdir}/pkgconfig/libSoundTouch.pc
ln -s soundtouch.pc %{buildroot}%{_libdir}/pkgconfig/soundtouch-1.0.pc

## soundtouch installs an autoheader generated header file which could very
## well conflict with other autoheader generated header files, so we override
## this with our own version which contains only the bare minimum:
#echo '#define FLOAT_SAMPLES 1' \
#  > %%{buildroot}%%{_includedir}/soundtouch/soundtouch_config.h


%files
%doc README.html
%license COPYING.TXT
%{_bindir}/soundstretch
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_libdir}/cmake/SoundTouch


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.0-3
- Prepare for Oreon 11 (RP1)
