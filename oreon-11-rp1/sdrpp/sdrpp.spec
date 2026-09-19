%global source0_hash c0ff6378e41d2bf16a4b6e791dacfc360ad226bfc59971c91c408a07e2a1a6ca

%global commit aa2b4b1c5814cc2f832898a9e4a1bdfc38e7ac8d
%global gittag 1.2.1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           sdrpp
Version:        1.2.1
Release:        6%{?dist}
Summary:        SDRPlusPlus bloat-free SDR receiver software

# Automatically converted from old format: GPLv3 and MIT and WTFPL and Public Domain - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-MIT AND WTFPL AND LicenseRef-Callaway-Public-Domain
URL:            https://github.com/AlexandreRouma/SDRPlusPlus/
Source0:        https://github.com/AlexandreRouma/SDRPlusPlus/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:        org.sdrpp.SDRPlusPlus.metainfo.xml

# Changes to top-level and core CMakeLists.txt to complete the above changes.
# Set soname on libsdrpp_core.so
# Install libsdrpp_core.so in _libdir
Patch1:         cmake-top.patch
# Ensure libraries come from pkgconfig
Patch2:         add-libraries.patch
# Move the config file to libdir
#Patch3:         configfile-libdir.patch
# std::runtime_error requires <stdexcept>
# https://github.com/AlexandreRouma/SDRPlusPlus/issues/970
Patch5:         sdrpp-stdexcept.patch
# Do not use hardcoded paths in desktop file
Patch6:         desktop-file.patch

ExcludeArch:    i686

BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  fftw-devel glew-devel volk-devel glfw-devel
BuildRequires:  portaudio-devel libiio-devel rtaudio-devel
BuildRequires:  spdlog-devel fmt-devel
# Need to BR -static packages for header-only libraries for tracking, per
BuildRequires:  rapidjson-devel rapidjson-static
BuildRequires:  json-devel json-static
BuildRequires:  libcorrect-devel
BuildRequires:  libzstd-devel
BuildRequires:  uhd-devel
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021
# CVE-2021-42715
# CVE-2021-42716
# CVE-2022-28041
# CVE-2023-43898
# CVE-2023-45661
# CVE-2023-45662
# CVE-2023-45663
# CVE-2023-45664
# CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-devel >= 2.28^20231011gitbeebb24-12
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel stb_image_resize-static
BuildRequires:  stb_truetype-devel stb_truetype-static
BuildRequires:  SoapySDR-devel hackrf-devel rtl-sdr-devel
BuildRequires:  libcorrect-devel codec2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires: google-roboto-fonts

# Bundled libraries
# https://github.com/AlexandreRouma/SDRPlusPlus/issues/292
# https://github.com/ocornut/imgui
# MIT License
Provides: bundled(imgui) = 1.83
# imgui itself bundles stb_rect_pack and stb_textedit with changes that do not
# match upstream stb so we can't remove it in favor of library code. It is essentially
# a private fork of upstream stb.  stb_truetype matches upstream now, so that was unbundled.
#
# https://github.com/samhocevar/portable-file-dialogs
# WTFPL License
Provides: bundled(portable-file-dialogs) = 0.1.0
#
# https://github.com/discord/discord-rpc
# MIT License
# Note: this library is deprecated by upstream in favor of Discord's GameSDK. Therefore
# this should not be packaged into Fedora separately.
Provides: bundled(discord-rpc) = 3.4.0
# A local copy of libsddc is present in sddc_source but is not built.
# A local copy of libcorrect is present in falcon9_decoder but is not built.
# A local copy of nlohmann-json is present in the source and is deleted prior to building.
# A local copy of stb_image and stb_image_resize is present in the source and is deleted prior to building.
# A local copy of rapidjson is present in the source and is deleted prior to building.
# A local copy of spdlog is present in the source and is deleted prior to building.

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
# For compatibility with CMake 4.0
export CMAKE_POLICY_VERSION_MINIMUM=3.5

# Not building Falcon9 decoder as it requires ffplay which is in rpmfusion
# Not building hardware support which does not have libraries in Fedora
# Building for new PortAudio
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

# Install desktop icon
install -D -p -m644 root/res/icons/sdrpp.png \
  %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

# Install AppStream metainfo file
install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/org.sdrpp.SDRPlusPlus.metainfo.xml

%check
# upstream has no tests for ctest except in unbuilt libsddc
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.sdrpp.SDRPlusPlus.metainfo.xml

%files
%license license misc_modules/discord_integration/discord-rpc/LICENSE
%doc readme.md contributing.md
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/lib%{name}_core.so.%{version}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_bindir}/%{name}
%{_metainfodir}/*

%changelog
%autochangelog
