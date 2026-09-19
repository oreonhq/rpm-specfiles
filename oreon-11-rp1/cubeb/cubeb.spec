%global source0_hash 920dbba4a3e1624b07aa813c8b8dc9339aeb10e0676958d250f5bedc8a22db31

%global commit 48689ae7a73caeb747953f9ed664dc71d2f918d8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20230517
%global fgittag %{gitdate}.git%{shortcommit}

Name:           cubeb
Version:        0.2
Release:        20%{?fgittag:.%{fgittag}}%{?dist}
Summary:        A cross platform audio library

#cubeb is ISC, sanitizers-cmake is MIT
#excluding the following files which are BSD 3-clause:
#/src/speex/arch.h
#/src/speex/fixed_generic.h
#/src/speex/resample.c
#/src/speex/resample_neon.h
#/src/speex/resample_sse.h
#/src/speex/speex_resampler.h
#/src/speex/stack_alloc.h
# Automatically converted from old format: ISC and BSD and MIT - review is highly recommended.
License:        ISC AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/mozilla/cubeb
Source0:        https://github.com/mozilla/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel

#Taken from the mozilla blog:
#https://blog.mozilla.org/webrtc/firefoxs-audio-backend/
#Which is licensed CC-BY-SA 3.0
%description
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%package devel
Summary:        A cross platform audio library
Provides:       %{name}-static = %{version}-%{release}

%description devel
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
#Clean up Android files
rm -rf src/android

#Clean up the README.md, we don't need building information:
sed -i -e "/^\[!/d" -e "/INSTALL.md/d" README.md

%build
%cmake . -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=ON -DUSE_SANITIZERS=OFF
%cmake_build

%install
%cmake_install

%check
#Run only the tests known to work in mock/chroot:
%ctest -R "(record|resampler|duplex|triple_buffer|ring_array|utils|ring_buffer|device_changed_callback)"

%files devel
%doc README.md
%license LICENSE
%{_libdir}/libcubeb.a
%{_bindir}/%{name}-test
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_docdir}/%{name}

%changelog
%autochangelog
