%global source0_hash 4bf0edd975996622bcc0615191e6daf79391119b5fb4920156c693c05d1ae3dc

%global soversion 10

Name:           libopenshot-audio
Version:        0.5.0
Release:        2%{?dist}
Summary:        Audio library used by OpenShot

License:        GPL-3.0-or-later
URL:            http://openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Disabling libopenshot-audio due to libopenshot exclusion, see rfbz #5528
ExcludeArch:    ppc64le

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  alsa-lib-devel
BuildRequires:  zlib-devel

# This is a modified version of JUCE
Provides:       bundled(JUCE) = 5.4.3
# JUCE has modified versions of these
Provides:       bundled(flac) = 1.3.1
Provides:       bundled(libvorbis) = 1.3.2

%description
OpenShot Audio Library (libopenshot-audio) is an open-source
project based on JUCE, and enables high-quality audio editing
and playback for libopenshot.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        demo
Summary:        Program for demonstrating %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    demo
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS README.md
%{_libdir}/%{name}.so.%{soversion}
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/cmake/OpenShotAudio/

%files demo
%{_bindir}/openshot-audio-demo
%{_mandir}/man1/openshot-audio-demo.1*

%changelog
%autochangelog
