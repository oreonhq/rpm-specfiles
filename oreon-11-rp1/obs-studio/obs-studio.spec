%global source0_hash baa30a61d8f99f92ab13504efb8903bd19db2cc55624c6de97772073febebf26

%ifarch %{power64} s390x riscv64
# LuaJIT is not available for POWER and IBM Z
%bcond lua_scripting 0
%else
%bcond lua_scripting 1
%endif

%ifarch x86_64
# VPL/QSV is only available on x86_64
%bcond vpl 1
%else
%bcond vpl 0
%endif

# x264 is not in Fedora
%bcond x264 0

%if ! (0%{?fedora} >= 42)
# CEF is only available in F42+
%bcond cef 0
%else
%ifarch %{x86_64} %{arm64}
# CEF is only available on x86_64 and aarch64
%bcond cef 1
%else
%bcond cef 0
%endif
%endif

%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif
%global libvlc_soversion 5

%global obswebsocket_version 5.6.3
%global obsbrowser_commit a776dd6a1a0ded4a8a723f2f572f3f8a9707f5a8

# Upstream does not declare this yet. Arbitrarily pick 137.0 since it works
# and it works around a CEF versioning teething issue:
# https://github.com/chromiumembedded/cef/issues/3959
%global cef_api_version 13700

#global commit ad859a3f66daac0d30eebcc9b07b0c2004fb6040
#global snapdate 202303261743
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})

Name:           obs-studio
Version:        32.0.4
Release:        4%{?dist}
Summary:        Open Broadcaster Software Studio

# OBS itself is GPL-2.0-or-later, while various plugin dependencies are of various other licenses
# The licenses for those dependencies are captured with the bundled provides statements
License:        GPL-2.0-or-later and MIT and BSD-2-Clause and BSD-3-Clause and BSL-1.0 and LGPL-2.1-or-later and CC0-1.0 and (CC0-1.0 or OpenSSL or Apache-2.0) and LicenseRef-Fedora-Public-Domain and (BSD-3-Clause or GPL-2.0-only)
URL:            https://obsproject.com/
%if 0%{?snapdate}
Source0:        https://github.com/obsproject/obs-studio/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:        https://github.com/obsproject/obs-studio/archive/%{version}/%{name}-%{version}.tar.gz
%endif
Source1:        https://github.com/obsproject/obs-websocket/archive/%{obswebsocket_version}/obs-websocket-%{obswebsocket_version}.tar.gz
Source2:        https://github.com/obsproject/obs-browser/archive/%{obsbrowser_commit}/obs-browser-%{obsbrowser_commit}.tar.gz

# Backports from upstream

# Proposed upstream
## From: https://github.com/obsproject/obs-studio/pull/12326
Patch0101:      0101-frontend-Consider-settings-changed-if-an-output-sett.patch
Patch0102:      0102-frontend-Allow-invalid-recording-encoder-if-quality-.patch
## From: https://github.com/obsproject/obs-studio/pull/8529
Patch0103:      0103-UI-Add-support-for-OpenH264-as-the-worst-case-fallba.patch
## From: https://github.com/obsproject/obs-studio/pull/12507
Patch0105:      0105-libobs-opengl-Reject-external-only-modifiers.patch
## From: https://github.com/obsproject/obs-studio/pull/12951
Patch0106:      0106-fix-shutdown-crash.patch
## From: https://github.com/obsproject/obs-studio/pull/13198
Patch0107:      0107-linux-v4l2-Fix-spurious-fd-closing.patch

# WIP code to improve new CEF support (based on upstream dev tree)
## From: https://github.com/asahilina/obs-browser/tree/lockdown
Patch0201:      0201-WIP-Lock-down-Chrome-Runtime-dummy-Browser-Client.patch
Patch0202:      0202-WIP-Lock-down-Chrome-Runtime-Disable-various-setting.patch
Patch0203:      0203-WIP-Lock-down-Chrome-Runtime-Lock-down-URLs-and-comm.patch
Patch0204:      0204-WIP-Enable-Chrome-Runtime.patch
Patch0205:      0205-WIP-Chrome-Runtime-Data-migration.patch
Patch0206:      0206-WIP-Lock-down-Chrome-Runtime-Misc-changes.patch
## From: https://github.com/obsproject/obs-browser/pull/517
Patch0250:      0250-Update-to-C-20.patch

# Downstream Fedora patches
## Use fdk-aac by default
Patch1001:      obs-studio-UI-use-fdk-aac-by-default.patch
## Fix error: passing argument 4 of ‘query_dmabuf_modifiers’ from
##            incompatible pointer type [-Wincompatible-pointer-types]
Patch1003:      obs-studio-fix-incompatible-pointer-type.patch
Patch1004:      obs-studio-fix-build-against-qt-6-10.patch

BuildRequires:  gcc
BuildRequires:  cmake >= 3.22
BuildRequires:  ninja-build
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

BuildRequires:  alsa-lib-devel
BuildRequires:  asio-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdk-aac-free-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  jansson-devel >= 2.5
BuildRequires:  json-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdatachannel-devel >= 0.20
BuildRequires:  libdrm-devel
BuildRequires:  libGL-devel
BuildRequires:  libglvnd-devel
BuildRequires:  librist-devel
BuildRequires:  srt-devel
BuildRequires:  libuuid-devel
BuildRequires:  libv4l-devel
BuildRequires:  libva-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxkbcommon-devel
%if %{with lua_scripting}
BuildRequires:  luajit-devel
%endif
BuildRequires:  mbedtls-devel
BuildRequires:  nv-codec-headers
%if %{with vpl}
BuildRequires:  libvpl-devel
%endif
BuildRequires:  pciutils-devel
BuildRequires:  pipewire-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  libqrcodegencpp-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  rnnoise-devel
BuildRequires:  simde-devel
BuildRequires:  speexdsp-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
BuildRequires:  uthash-devel
BuildRequires:  wayland-devel
BuildRequires:  websocketpp-devel
%if %{with x264}
BuildRequires:  x264-devel
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Ensure that we have the full ffmpeg suite installed
Requires:       /usr/bin/ffmpeg
# Try to ensure openh264 is installed
## Note, we can do this because openh264 is provided in a default-enabled
## third party repository provided by Cisco.
Recommends:     openh264%{?_isa}

# Ensure QtWayland is installed when libwayland-client is installed
Requires:      (qt6-qtwayland%{?_isa} if libwayland-client%{?_isa})
# For icon folder heirarchy
Requires:      hicolor-icon-theme

# These are modified sources that can't be easily unbundled
## License: BSL-1.0
Provides:      bundled(decklink-sdk)
## License: CC0-1.0 or OpenSSL or Apache-2.0
Provides:      bundled(blake2)
## License: MIT
Provides:      bundled(json11)
## License: MIT
Provides:      bundled(libcaption)
## License: BSD-3-Clause
Provides:      bundled(rnnoise)
## License: LGPL-2.1-or-later and LicenseRef-Fedora-Public-Domain
Provides:      bundled(librtmp)
## License: MIT
Provides:      bundled(libnsgif)
## License: MIT
## Windows only dependency
## Support for Linux will also unbundle it
## Cf. https://github.com/obsproject/obs-studio/pull/8327
Provides:      bundled(intel-mediasdk)

%if ! %{with cef}
# When the plugin is not available, obsolete it
Obsoletes:     %{name}-plugin-browser < %{version}-%{release}
%endif

%description
Open Broadcaster Software is free and open source
software for video recording and live streaming.

%files
%doc README.rst
%license frontend/data/license/gplv2.txt
%license COPYING
%{_bindir}/obs
%{_bindir}/obs-ffmpeg-mux
%ifarch %{x86_64}
%{_bindir}/obs-nvenc-test
%endif
%{_datadir}/metainfo/com.obsproject.Studio.metainfo.xml
%{_datadir}/applications/com.obsproject.Studio.desktop
%{_datadir}/icons/hicolor/*/apps/com.obsproject.Studio.*
%{_datadir}/obs/
%exclude %{_datadir}/obs/obs-plugins/vlc-video/
%if %{with cef}
%exclude %{_datadir}/obs/obs-plugins/obs-browser*
%endif

# --------------------------------------------------------------------------

%package libs
Summary: Open Broadcaster Software Studio libraries

%description libs
Library files for Open Broadcaster Software

%files libs
%license COPYING
%license .fedora-rpm/licenses/*
%dir %{_libexecdir}/obs-plugins
%{_libdir}/obs-plugins/
%if %{with cef}
%exclude %{_libdir}/obs-plugins/obs-browser*
%endif
%exclude %{_libdir}/obs-plugins/vlc-video.so
%{_libdir}/obs-scripting/
# unversioned so files packaged for third-party plugins (cf. rfbz#5999)
%{_libdir}/*.so
%{_libdir}/*.so.*

# --------------------------------------------------------------------------

%package devel
Summary: Open Broadcaster Software Studio header files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: simde-devel

%description devel
Header files for Open Broadcaster Software

%files devel
%{_libdir}/cmake/libobs/
%{_libdir}/cmake/obs-frontend-api/
%{_libdir}/cmake/obs-websocket-api/
%{_libdir}/pkgconfig/libobs.pc
%{_libdir}/pkgconfig/obs-frontend-api.pc
%{_includedir}/obs/

# --------------------------------------------------------------------------

%if %{with cef}
%package plugin-browser
Summary:        Open Broadcaster Software Studio - CEF-based browser plugin
BuildRequires:  cef-devel

# Filter out bogus libcef.so requires as this is handled manually
# with an explicit dependency
%global __requires_exclude ^libcef\\.so.*$

# Require the correct CEF API support
%{?_cef_api_requires:%_cef_api_requires %{cef_api_version}}
Requires:       obs-studio%{?_isa} = %{version}-%{release}
Supplements:    obs-studio%{?_isa}

%description plugin-browser
Open Broadcaster Software is free and open source software
for video recording and live streaming.

This package contains the plugin for integrated web-based overlays in
a video stream or recording using the Chromium Embedded Framework (CEF).

%files plugin-browser
%{_libdir}/obs-plugins/obs-browser*
%{_datadir}/obs/obs-plugins/obs-browser*
%endif

# --------------------------------------------------------------------------

%package plugin-vlc-video
Summary:        Open Broadcaster Software Studio - VLC-based video plugin
BuildRequires:  vlc-devel
# We dlopen() libvlc
Requires:       libvlc.so.%{libvlc_soversion}%{?lib64_suffix}
Requires:       obs-studio%{?_isa} = %{version}-%{release}
Supplements:    obs-studio%{?_isa}

%description plugin-vlc-video
Open Broadcaster Software is free and open source software
for video recording and live streaming.

This package contains the plugin for using VLC to embed video
as an overlay in a video stream or recording.

%files plugin-vlc-video
%{_libdir}/obs-plugins/vlc-video.so
%{_datadir}/obs/obs-plugins/vlc-video/

# --------------------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{?snapdate:%{commit}}%{!?snapdate:%{version}}
# Prepare plugins/obs-websocket
tar -xf %{SOURCE1} -C plugins/obs-websocket --strip-components=1
tar -xf %{SOURCE2} -C plugins/obs-browser --strip-components=1
%autopatch -p1 -M 199
cd plugins/obs-browser
%autopatch -p1 -m 200 -M 999
cd ../..
%autopatch -p1 -m 1000

# This is provided by cef-devel systemwide
rm cmake/finders/FindCEF.cmake

# Fix obs-browser rpath setting
sed -e 's,INSTALL_RPATH ".*",INSTALL_RPATH "%{_libdir}/cef/",' -i plugins/obs-browser/cmake/os-linux.cmake

%if ! %{with x264}
# disable x264 plugin
mv plugins/obs-x264/CMakeLists.txt plugins/obs-x264/CMakeLists.txt.disabled
touch plugins/obs-x264/CMakeLists.txt
%endif

%if ! %{with vpl}
# disable unusable qsv plugin
mv plugins/obs-qsv11/CMakeLists.txt plugins/obs-qsv11/CMakeLists.txt.disabled
touch plugins/obs-qsv11/CMakeLists.txt
%endif

# Removing unused third-party deps
rm -rf deps/w32-pthreads
rm -rf deps/ipc-util
rm -rf deps/jansson

# Remove unneeded EGL/KHR files
rm -rf deps/glad/include/{EGL,KHR}
sed -e 's|include/EGL/eglplatform.h||g' -i deps/glad/CMakeLists.txt

# Collect license files
mkdir -p .fedora-rpm/licenses/deps
mkdir -p .fedora-rpm/licenses/plugins
cp plugins/obs-filters/rnnoise/COPYING .fedora-rpm/licenses/deps/rnnoise-COPYING
cp plugins/obs-websocket/LICENSE .fedora-rpm/licenses/plugins/obs-websocket-LICENSE
cp plugins/obs-outputs/librtmp/COPYING .fedora-rpm/licenses/deps/librtmp-COPYING
cp deps/json11/LICENSE.txt .fedora-rpm/licenses/deps/json11-LICENSE.txt
cp deps/libcaption/LICENSE.txt .fedora-rpm/licenses/deps/libcaption-LICENSE.txt
cp plugins/obs-qsv11/QSV11-License-Clarification-Email.txt .fedora-rpm/licenses/plugins/QSV11-License-Clarification-Email.txt
cp deps/blake2/LICENSE.blake2 .fedora-rpm/licenses/deps/
cp libobs/graphics/libnsgif/LICENSE.libnsgif .fedora-rpm/licenses/deps/
cp plugins/decklink/LICENSE.decklink-sdk .fedora-rpm/licenses/deps
cp plugins/obs-qsv11/obs-qsv11-LICENSE.txt .fedora-rpm/licenses/plugins/

%conf
# libcef_wrapper needs to be built static
%undefine _cmake_shared_libs
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DOBS_VERSION_OVERRIDE=%{version} \
       -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
       -DUNIX_STRUCTURE=1 -GNinja \
%if ! %{with cef}
       -DENABLE_BROWSER=OFF \
%else
       -DENABLE_BROWSER=ON \
       -DCEF_API_VERSION=%{cef_api_version} \
%endif
       -DENABLE_JACK=ON \
       -DENABLE_LIBFDK=ON \
       -DENABLE_AJA=OFF \
%if ! %{with lua_scripting}
       -DENABLE_SCRIPTING_LUA=OFF \
%endif
       -DOpenGL_GL_PREFERENCE=GLVND

%build
%cmake_build

%install
%cmake_install

# Work around broken libobs.pc file...
# Cf. https://github.com/obsproject/obs-studio/issues/7972
sed -e 's|^Cflags: .*|Cflags: -I${includedir} -DHAVE_OBSCONFIG_H|' -i %{buildroot}%{_libdir}/pkgconfig/libobs.pc

# Create libexecdir for obs-plugins
mkdir -p %{buildroot}%{_libexecdir}/obs-plugins

# Delete useless files
find %{buildroot} -name ".keepme" -delete
find %{buildroot} -name ".gitkeep" -delete

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.obsproject.Studio.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%changelog
%autochangelog
