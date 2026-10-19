%global source2_hash baa30a61d8f99f92ab13504efb8903bd19db2cc55624c6de97772073febebf26
%global source1_hash e7f9f0208ffd651cb30fa83863890272929b8a3d194a85ff27358fd33d940ac2
%global source0_hash 35d3cd0979d65664fada7119fdb612eca7c34b61a1623a330caec74bf72626c4
%ifarch %{power64} s390x riscv64
%bcond lua_scripting 0
%else
%bcond lua_scripting 1
%endif
%ifarch x86_64
%bcond vpl 1
%else
%bcond vpl 0
%endif
%bcond x264 0
%ifarch %{x86_64} %{arm64}
%bcond cef 1
%else
%bcond cef 0
%endif
%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif
%global libvlc_soversion 5
%global obswebsocket_version 5.6.3
%global obsbrowser_commit a776dd6a1a0ded4a8a723f2f572f3f8a9707f5a8
%global cef_api_version 13700
Name:           obs-studio
Version:        32.2.2
Release:        1%{?dist}
Summary:        Open Broadcaster Software Studio
License:        GPL-2.0-or-later and MIT and BSD-2-Clause and BSD-3-Clause and BSL-1.0 and LGPL-2.1-or-later and CC0-1.0 and (CC0-1.0 or OpenSSL or Apache-2.0) and LicenseRef-Fedora-Public-Domain and (BSD-3-Clause or GPL-2.0-only)
URL:            https://obsproject.com/
%if 0%{?snapdate}
Source0:        https://github.com/obsproject/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%else
%endif
Source1:        https://github.com/obsproject/obs-websocket/archive/%{obswebsocket_version}/obs-websocket-%{obswebsocket_version}.tar.gz
Source2:        https://github.com/obsproject/obs-browser/archive/%{obsbrowser_commit}/obs-browser-%{obsbrowser_commit}.tar.gz
Patch0101:      0101-frontend-Consider-settings-changed-if-an-output-sett.patch
Patch0102:      0102-frontend-Allow-invalid-recording-encoder-if-quality-.patch
Patch0103:      0103-UI-Add-support-for-OpenH264-as-the-worst-case-fallba.patch
Patch0105:      0105-libobs-opengl-Reject-external-only-modifiers.patch
Patch0106:      0106-fix-shutdown-crash.patch
Patch0107:      0107-linux-v4l2-Fix-spurious-fd-closing.patch
Patch0201:      0201-WIP-Lock-down-Chrome-Runtime-dummy-Browser-Client.patch
Patch0202:      0202-WIP-Lock-down-Chrome-Runtime-Disable-various-setting.patch
Patch0203:      0203-WIP-Lock-down-Chrome-Runtime-Lock-down-URLs-and-comm.patch
Patch0204:      0204-WIP-Enable-Chrome-Runtime.patch
Patch0205:      0205-WIP-Chrome-Runtime-Data-migration.patch
Patch0206:      0206-WIP-Lock-down-Chrome-Runtime-Misc-changes.patch
Patch0250:      0250-Update-to-C-20.patch
Patch1001:      obs-studio-UI-use-fdk-aac-by-default.patch
Patch1003:      obs-studio-fix-incompatible-pointer-type.patch
Patch1004:      obs-studio-fix-build-against-qt-6-10.patch
%if %{with lua_scripting}
%endif
%if %{with vpl}
%endif
%if %{with x264}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       /usr/bin/ffmpeg
Recommends:     openh264%{?_isa}
Requires:      (qt6-qtwayland%{?_isa} if libwayland-client%{?_isa})
Requires:      hicolor-icon-theme
Provides:      bundled(decklink-sdk)
Provides:      bundled(blake2)
Provides:      bundled(json11)
Provides:      bundled(libcaption)
Provides:      bundled(rnnoise)
Provides:      bundled(librtmp)
Provides:      bundled(libnsgif)
Provides:      bundled(intel-mediasdk)
%if ! %{with cef}
Obsoletes:     %{name}-plugin-browser < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  asio-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fdk-aac-free-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  json-devel
BuildRequires:  libGL-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libdatachannel-devel
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libqrcodegencpp-devel
BuildRequires:  librist-devel
BuildRequires:  libuuid-devel
BuildRequires:  libv4l-devel
BuildRequires:  libva-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  luajit-devel
BuildRequires:  mbedtls-devel
BuildRequires:  ninja-build
BuildRequires:  nv-codec-headers
BuildRequires:  pciutils-devel
BuildRequires:  pipewire-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  rnnoise-devel
BuildRequires:  simde-devel
BuildRequires:  speexdsp-devel
BuildRequires:  srt-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
BuildRequires:  uthash-devel
BuildRequires:  vlc-devel
BuildRequires:  wayland-devel
BuildRequires:  websocketpp-devel
# /oreon:deps
%description
Open Broadcaster Software is free and open source
software for video recording and live streaming.

%package libs
Summary: Open Broadcaster Software Studio libraries
%description libs
Library files for Open Broadcaster Software

%package devel
Summary: Open Broadcaster Software Studio header files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: simde-devel
%description devel
Header files for Open Broadcaster Software

%package plugin-browser
Summary:        Open Broadcaster Software Studio - CEF-based browser plugin
BuildRequires:  cef-devel
%global __requires_exclude ^libcef\\.so.*$
%{?_cef_api_requires:%_cef_api_requires %{cef_api_version}}
Requires:       obs-studio%{?_isa} = %{version}-%{release}
Supplements:    obs-studio%{?_isa}
%description plugin-browser
Open Broadcaster Software is free and open source software
for video recording and live streaming.

This package contains the plugin for integrated web-based overlays in
a video stream or recording using the Chromium Embedded Framework (CEF).

%package plugin-vlc-video
Summary:        Open Broadcaster Software Studio - VLC-based video plugin
BuildRequires:  vlc-devel
Requires:       libvlc.so.%{libvlc_soversion}%{?lib64_suffix}
Requires:       obs-studio%{?_isa} = %{version}-%{release}
Supplements:    obs-studio%{?_isa}
%description plugin-vlc-video
Open Broadcaster Software is free and open source software
for video recording and live streaming.

This package contains the plugin for using VLC to embed video
as an overlay in a video stream or recording.

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
sed -e 's|^Cflags: .*|Cflags: -I${includedir} -DHAVE_OBSCONFIG_H|' -i %{buildroot}%{_libdir}/pkgconfig/libobs.pc
mkdir -p %{buildroot}%{_libexecdir}/obs-plugins
find %{buildroot} -name ".keepme" -delete
find %{buildroot} -name ".gitkeep" -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/com.obsproject.Studio.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n obs-studio-libs -f %{oreon_filedir}/obs-studio-libs.list
%files -n obs-studio-devel -f %{oreon_filedir}/obs-studio-devel.list
%files -n obs-studio-plugin-vlc-video -f %{oreon_filedir}/obs-studio-plugin-vlc-video.list

%changelog

%autochangelog
