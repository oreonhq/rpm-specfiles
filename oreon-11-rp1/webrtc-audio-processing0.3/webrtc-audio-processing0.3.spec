%global source0_hash a0fdd938fd85272d67e81572c5a4d9e200a0c104753cb3c209ded175ce3c5dbf

Name:           webrtc-audio-processing0.3
Version:        0.3.1
Release:        16%{?dist}
Summary:        Library for echo cancellation

License:        BSD-3-Clause
URL:            http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:        http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/webrtc-audio-processing-%{version}.tar.xz

## upstream patches

Patch100:         webrtc-fix-typedefs-on-other-arches.patch
# bz#1336466, https://bugs.freedesktop.org/show_bug.cgi?id=95738
Patch104:         webrtc-audio-processing-0.2-big-endian.patch

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: gcc gcc-c++

%description
%{name} is a library derived from Google WebRTC project that 
provides echo cancellation functionality. This library is used by for example
PulseAudio to provide echo cancellation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n webrtc-audio-processing-%{version}

%build
# for patch1
autoreconf -vif

%configure \
%ifarch %{arm} aarch64
  --enable-neon=no \
%endif
  --disable-silent-rules \
  --disable-static

%make_build

%install
%make_install

# remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc NEWS AUTHORS README.md
%license COPYING
%{_libdir}/libwebrtc_audio_processing.so.1*

%files devel
%{_libdir}/libwebrtc_audio_processing.so
%{_libdir}/pkgconfig/webrtc-audio-processing.pc
%{_includedir}/webrtc_audio_processing/

%changelog
%autochangelog
