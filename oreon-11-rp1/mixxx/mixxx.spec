%global source2_hash df41fe39bed9d16d27a3649d237b68edd2cdb6fc71a82cae5cd746d4e4ef6578
%global source1_hash 4f10e9e5673d948776e47e78273fa4d61408155cb0e210af1538c83222f285d4
%global source0_hash 9cfc9025d50d2511767ee52a07b8854f75c581f0585197d043bc219fcf9f9050
%ifarch %{power64}
%global _lto_cflags %{nil}
%endif
%global libkeyfinder_version 2.2.8
%global libdjinterop_version 0.24.3
%if "%{?gitcommit}" == ""
  %global sources %{version}%{?extraver:-%{extraver}}
%else
  %global sources %{gitcommit}
  %global snapinfo %{?gitcommit:%{?gitcommitdate}git%{?gitcommit:%(c=%{gitcommit}; echo ${c:0:7})}}
%endif
Name:           mixxx
Version:        2.5.6
Release:        1%{?dist}
Summary:        Mixxx is open source software for DJ'ing
License:        LGPL-2.1-or-later AND (BSD-3-Clause OR GPL-3.0-only OR HIDAPI) AND MIT AND GPL-2.0-or-later AND BSD-3-Clause AND MPL-1.1 AND GPL-3.0-or-later
URL:            http://www.mixxx.org
Source0:        https://github.com/%{name}dj/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/mixxxdj/libkeyfinder/archive/refs/tags/%{libkeyfinder_version}.zip#/libkeyfinder-%{libkeyfinder_version}.zip
Source2:        https://github.com/xsco/libdjinterop/archive/refs/tags/%{libdjinterop_version}.tar.gz#/libdjinterop-%{libdjinterop_version}.tar.gz
Patch0:         desktop-file-qpa-platform-xcb.patch
Requires: faad2-libs%{?_isa}
Requires: hicolor-icon-theme
Requires: open-sans-fonts
Requires: qt6-qttranslations
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  faad2-libs
BuildRequires:  fftw-devel
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  gtest-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  hidapi-devel
BuildRequires:  lame-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libchromaprint-devel
BuildRequires:  libebur128-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmp4v2-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libusbx-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lilv-devel
BuildRequires:  ninja-build
BuildRequires:  opus-devel
BuildRequires:  opusfile-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-lite-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qtkeychain-qt6-devel
BuildRequires:  rubberband-devel
BuildRequires:  soundtouch-devel
BuildRequires:  sqlite-devel
BuildRequires:  taglib-devel
BuildRequires:  upower-devel
BuildRequires:  wavpack-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Mixxx is open source software for DJ'ing. You can use
AIFF/FLAC/M4A/MP3/OggVorbis/Opus/WAV/WavPack files, and
other formats as audio input. Playback can be controlled
through the GUI or with external controllers including
MIDI and HID devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{sources}

echo "#pragma once" > src/build.h
%if "%{?extraver}" != ""
  echo "#define BUILD_BRANCH \"%{extraver}\"" >> src/build.h
%endif
%if "%{?snapinfo}" != ""
  echo "#define BUILD_REV \"%{snapinfo}\"" >> src/build.h
%endif

# Copy the source archives from the sources folder into the
# dedicated downloads folder of the build directory.
mkdir -p %{__cmake_builddir}/downloads
cp %{SOURCE1} %{__cmake_builddir}/downloads
cp %{SOURCE2} %{__cmake_builddir}/downloads

%conf
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DOPTIMIZE=portable \
  -DINSTALL_USER_UDEV_RULES=%{!?flatpak:ON}%{?flatpak:OFF} \
  -DWARNINGS_FATAL=OFF \
  -DBATTERY=ON \
  -DBROADCAST=ON \
  -DBULK=ON \
  -DENGINEPRIME=ON \
  -DFAAD=ON \
  -DFFMPEG=ON \
  -DHID=ON \
  -DKEYFINDER=ON \
  -DLOCALECOMPARE=ON \
  -DLILV=ON \
  -DMAD=ON \
  -DMODPLUG=ON \
  -DOPUS=ON \
  -DQTKEYCHAIN=ON \
  -DVINYLCONTROL=ON \
  -DWAVPACK=ON

%build

%cmake_build
%install
%cmake_install
desktop-file-install \
  --vendor "" \
  --dir %{buildroot}%{_datadir}/applications \
  res/linux/org.mixxx.Mixxx.desktop
rm -rv \
  %{buildroot}%{_datadir}/doc/ \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}_macos.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}_ios.svg
%oreon_autofiles main

%check

%ctest
appstreamcli \
  validate \
  --no-net \
  %{buildroot}%{_metainfodir}/org.mixxx.Mixxx.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
