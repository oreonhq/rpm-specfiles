%global source0_hash 4f10e9e5673d948776e47e78273fa4d61408155cb0e210af1538c83222f285d4

# Disable LTO for ppc64
%ifarch %{power64}
%global _lto_cflags %{nil}
%endif

# Optional: Package version suffix for pre-releases, e.g. "beta" or "rc"
#global extraver beta

# Optional: Only used for untagged snapshot versions
#global gitcommit d225a5112166e9224e0c61cdc413b9145d009c06 
# Format: <yyyymmdd>
#global gitcommitdate 20240214

# Additional sources
%global libkeyfinder_version 2.2.8

# Additional sources
%global libdjinterop_version 0.24.3

%if "%{?gitcommit}" == ""
  # (Pre-)Releases
  %global sources %{version}%{?extraver:-%{extraver}}
%else
  # Snapshots
  %global sources %{gitcommit}
  %global snapinfo %{?gitcommit:%{?gitcommitdate}git%{?gitcommit:%(c=%{gitcommit}; echo ${c:0:7})}}
%endif

Name:           mixxx
Version:        2.5.4
Release:        4%{?dist}
Summary:        Mixxx is open source software for DJ'ing
# main sources are under GPL-2.0-or-later, except:
# lib/fidlib LGPL-2.1
# lib/hidapi BSD-3-Clause OR GPL-3.0-only OR HIDAPI
# lib/kaitai MIT
# lib/libshout-idjc LGPL-2.0-or-later
# lib/mp3guessenc-0.27.4 LGPL-2.1-or-later
# lib/portaudio MIT
# lib/qm-dsp GPL-2.0-or-later, except:
# lib/qm-dsp/ext/kissfft BSD-3-Clause
# lib/qm-dsp/maths/Polyfit.h MPL-1.1
# lib/replaygain LGPL-2.1-or-later
# lib/reverb GPL-3.0-or-later
# lib/rigtorp/SPSCQueue MIT
# lib/xwax GPL-3.0-or-latet
# Note: bundled fonts are not installed on Linux
License:        LGPL-2.1-or-later AND (BSD-3-Clause OR GPL-3.0-only OR HIDAPI) AND MIT AND GPL-2.0-or-later AND BSD-3-Clause AND MPL-1.1 AND GPL-3.0-or-later
URL:            http://www.mixxx.org
Source0:        https://github.com/mixxxdj/%{name}/archive/%{sources}/%{name}-%{sources}.tar.gz
# Append the actual downloaded file name with a preceding slash '/'
# as a fragment identifier to the URL to populate SOURCE<n> correctly
Source1:        https://github.com/mixxxdj/libkeyfinder/archive/refs/tags/%{libkeyfinder_version}.zip#/libkeyfinder-%{libkeyfinder_version}.zip
Source2:        https://github.com/xsco/libdjinterop/archive/refs/tags/%{libdjinterop_version}.tar.gz#/libdjinterop-%{libdjinterop_version}.tar.gz
Patch0:         desktop-file-qpa-platform-xcb.patch

# Build Tools
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
BuildRequires:  protobuf-compiler
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  google-benchmark-devel

# Build Requirements
# The runtime libraries of FAAD2 are needed during the build for testing
BuildRequires:  faad2-libs
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  flac-devel
BuildRequires:  hidapi-devel
BuildRequires:  lame-devel
BuildRequires:  libebur128-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libchromaprint-devel
BuildRequires:  fftw-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmp4v2-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libusbx-devel
BuildRequires:  lilv-devel
BuildRequires:  libvorbis-devel
BuildRequires:  opus-devel
BuildRequires:  opusfile-devel
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qtkeychain-qt6-devel
BuildRequires:  rubberband-devel
BuildRequires:  soundtouch-devel
BuildRequires:  sqlite-devel
BuildRequires:  taglib-devel
BuildRequires:  upower-devel
BuildRequires:  wavpack-devel
BuildRequires:  zlib-devel

# Runtime Requirements
Requires: faad2-libs%{?_isa}
Requires: hicolor-icon-theme
Requires: open-sans-fonts
Requires: qt6-qttranslations

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
# Install build artifacts
%cmake_install

# Install desktop launcher
desktop-file-install \
  --vendor "" \
  --dir %{buildroot}%{_datadir}/applications \
  res/linux/org.mixxx.Mixxx.desktop

# Delete unpackaged/unused files and directories
rm -rv \
  %{buildroot}%{_datadir}/doc/ \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}_macos.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}_ios.svg

%check
%ctest

# Validate AppStream data
appstreamcli \
  validate \
  --no-net \
  %{buildroot}%{_metainfodir}/org.mixxx.Mixxx.metainfo.xml

%files
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.mixxx.Mixxx.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/org.mixxx.Mixxx.metainfo.xml
%if %{undefined flatpak}
%dir %{_udevrulesdir}
%{_udevrulesdir}/69-%{name}-usb-uaccess.rules
%endif

%changelog
%autochangelog
