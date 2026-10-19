%global source0_hash c0ff6378e41d2bf16a4b6e791dacfc360ad226bfc59971c91c408a07e2a1a6ca
%global commit aa2b4b1c5814cc2f832898a9e4a1bdfc38e7ac8d
%global gittag 1.2.1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           sdrpp
Version:        1.2.1
Release:        6%{?dist}
Summary:        SDRPlusPlus bloat-free SDR receiver software
License:        GPL-3.0-only AND LicenseRef-Callaway-MIT AND WTFPL AND LicenseRef-Callaway-Public-Domain
URL:            https://github.com/AlexandreRouma/SDRPlusPlus/
Source0:        https://github.com/AlexandreRouma/SDRPlusPlus/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:        org.sdrpp.SDRPlusPlus.metainfo.xml
Patch1:         cmake-top.patch
Patch2:         add-libraries.patch
Patch5:         sdrpp-stdexcept.patch
Patch6:         desktop-file.patch
ExcludeArch:    i686
Requires: google-roboto-fonts
Provides: bundled(imgui) = 1.83
Provides: bundled(portable-file-dialogs) = 0.1.0
Provides: bundled(discord-rpc) = 3.4.0
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  codec2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glfw-devel
BuildRequires:  hackrf-devel
BuildRequires:  json-devel
BuildRequires:  json-static
BuildRequires:  libappstream-glib
BuildRequires:  libcorrect-devel
BuildRequires:  libiio-devel
BuildRequires:  libzstd-devel
BuildRequires:  portaudio-devel
BuildRequires:  rapidjson-devel
BuildRequires:  rapidjson-static
BuildRequires:  rtaudio-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  spdlog-devel
BuildRequires:  stb_image-devel
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel
BuildRequires:  stb_image_resize-static
BuildRequires:  stb_truetype-devel
BuildRequires:  stb_truetype-static
BuildRequires:  uhd-devel
BuildRequires:  volk-devel
# /oreon:deps
%description
SDR++ is a cross-platform and open source SDR software
with the aim of being bloat free and simple to use.

Features
- Wide hardware support (both through SoapySDR and dedicated modules)
- SIMD accelerated DSP
- Full waterfall update when possible. Makes browsing signals
  easier and more pleasant

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n SDRPlusPlus-%{commit}
# Install plugins to _lib
grep -rl 'lib/sdrpp/plugins' . | xargs sed -i -e 's:lib/sdrpp/plugins:%{_lib}/sdrpp/plugins:g'
# Delete local copy of spdlog. We're using the system library copy.
rm -rf core/src/spdlog
# Remove rapidjson in favor of system library
rm -rf misc_modules/discord_integration/discord-rpc/include/rapidjson
sed -i -e 's:#include "rapidjson/\(.*\)":#include <rapidjson/\1>:' misc_modules/discord_integration/discord-rpc/src/serialization.h
# Replace use of local nlohmann-json with library version
rm core/src/json.hpp
grep -l -r '#include <json.hpp>' . | xargs sed -i -e 's:#include <json.hpp>:#include <nlohmann/json.hpp>:'
# Replace use of local stb_image and stb_image_resize with library version
rm core/src/imgui/stb_image_resize.h
rm core/src/imgui/stb_image.h
sed -i -e 's:#include <imgui/stb_image.h>:#include <stb/stb_image.h>:' core/src/gui/icons.cpp
sed -i -e 's:#include <stb_image.h>:#include <stb/stb_image.h>:' \
    -e 's:#include <stb_image_resize.h>:#include <stb/stb_image_resize.h>:' core/src/core.cpp
# replace use of local stb_truetype with library version
sed -i -e 's:#include "imstb_truetype.h":#include<stb/stb_truetype.h>:' core/src/imgui/imgui_draw.cpp

# remove local libcorrect copy
rm -rf core/libcorrect/

# Use system-provided roboto font
sed -i -e 's:resDir + "/fonts/Roboto-Medium.ttf":"%{_datadir}/fonts/google-roboto/Roboto-Medium.ttf":'   core/src/gui/style.cpp

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DOPT_BUILD_AIRSPY_SOURCE=OFF \
       -DOPT_BUILD_AIRSPYHF_SOURCE=OFF \
       -DOPT_BUILD_BLADERF_SOURCE=OFF \
       -DOPT_BUILD_PLUTOSDR_SOURCE=OFF \
       -DOPT_BUILD_NEW_PORTAUDIO_SINK=ON \
       -DOPT_BUILD_M17_DECODER=ON \
	   -DUSE_INTERNAL_LIBCORRECT=OFF \
	   -DOPT_BUILD_SOAPY_SOURCE=ON \
	   -DOPT_BUILD_USRP_SOURCE=ON \
       -DBUILD_SHARED_LIBS=0
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_libdir}/libsdrpp_core.so
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
install -D -p -m644 root/res/icons/sdrpp.png \
  %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/org.sdrpp.SDRPlusPlus.metainfo.xml
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.sdrpp.SDRPlusPlus.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
