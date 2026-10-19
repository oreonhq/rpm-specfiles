%global source5_hash 75fad230ba2b9953cb4007e573df298fa9bd5ee865aafcd1228efd400d60b68d
%global source4_hash 961df327d8a756304d1b0a67316eebdb1111d13d559f0d3415114ec0eb30abd1
%global source0_hash ee91d291e45cc84f45e84493ce9847ab9c2e78e2bd3307143e1571fc27357207
%undefine _hardened_build
%undefine _cmake_shared_libs
%define _gcc_lto_cflags -fno-lto
%global bundled_libs Bochs_disasm cpp-optparse expr FatFs FreeSurround glslang imgui implot mbedtls rangeset soundtouch tinygltf
%global bochs_version 2.6.6
%global FatFs_version 0.14b
%global imgui_version 1.70
%global implot_version 0.16
%global mbedtls_version 2.28.10
%global soundtouch_version 2.3.2
%global tinygltf_version 2.9.5
%ifarch x86_64 aarch64
%global enablejit 1
%endif
Name:           dolphin-emu
Version:        2606a
Release:        1%{?dist}
Summary:        GameCube / Wii / Triforce Emulator
Url:            https://dolphin-emu.org/
License:        GPL-2.0-or-later AND MIT AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND GPL-3.0-or-later AND Zlib
Source0:        https://github.com/%{name}/dolphin/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Source4:        https://github.com/epezent/implot/archive/refs/tags/v%{implot_version}.tar.gz#/implot-%{implot_version}.tar.gz
Source5:        https://github.com/syoyo/tinygltf/archive/refs/tags/v%{tinygltf_version}.tar.gz#/tinygltf-%{tinygltf_version}.tar.gz
Patch0:         0001-Update-mbedtls-to-2.28.10.patch
Patch1:         0002-mbedtls-CVE-2025-52496-fix.patch
Patch2:         0003-mbedtls-CVE-2025-48965-fix.patch
Patch3:         0004-mbedtls-CVE-2025-47917-fix.patch
Patch10:        dolphin-emu-fix-build-against-qt-6-10.patch
Provides:       bundled(cpp-argparse)
Provides:       bundled(expr)
Provides:       bundled(FatFs) = %{FatFs_version}
Provides:       bundled(FreeSurround)
Provides:       bundled(imgui) = %{imgui_version}
Provides:       bundled(rangeset)
Provides:       bundled(implot) = %{implot_version}
Provides:       bundled(tinygltf) = %{tinygltf_version}
Provides:       bundled(soundtouch) = %{soundtouch_version}
Provides:       bundled(glslang)
Provides:       bundled(bochs) = %{bochs_version}
Provides:       bundled(mbedtls) = %{mbedtls_version}
ExclusiveArch:  x86_64 aarch64
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/env
BuildRequires:  SDL3-devel
BuildRequires:  SFML-devel
BuildRequires:  VulkanMemoryAllocator-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  cubeb-devel
BuildRequires:  desktop-file-utils
BuildRequires:  enet-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glslang-devel
BuildRequires:  gtest-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  hidapi-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libao-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libevdev-devel
BuildRequires:  libpng-devel
BuildRequires:  libspng-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  minizip-ng-devel
BuildRequires:  openal-soft-devel
BuildRequires:  picojson-static
BuildRequires:  portaudio-devel
BuildRequires:  pugixml-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  systemd-devel
BuildRequires:  vulkan-headers
BuildRequires:  xxhash-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-ng-devel
# /oreon:deps
%description
Dolphin is a Gamecube, Wii and Triforce (the arcade machine based on the
Gamecube) emulator, which supports full HD video with several enhancements such
as compatibility with all PC controllers, turbo speed, networked multi player,
and more.
Most games run perfectly or with minor bugs.

%package nogui
Summary:        Dolphin Emulator without a graphical user interface
Requires:       %{name}-data = %{version}-%{release}
%description nogui
Dolphin Emulator without a graphical user interface.

%package tool
Summary:        Dolphin Emulator CLI utility
%description tool
This package provides "dolphin-tool", which is a CLI-based utility for
functions such as managing disc images.

%package data
Summary:        Dolphin Emulator data files
BuildArch:      noarch
%description data
This package provides the data files for dolphin-emu.

####################################################

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dolphin-%{version}

# Extract bundled git submodules:
gzip -dc %{SOURCE4} | tar -C Externals/implot/implot --strip-components=1 -xof -
gzip -dc %{SOURCE5} | tar -C Externals/tinygltf/tinygltf --strip-components=1 -xof -

#Allow building with cmake macro
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

#Use system zlib (upstream doesn't like this for performance reasons):
sed -i 's/add_subdirectory(\(.*zlib\)/dolphin_find_optional_system_library_pkgconfig(ZLIB zlib-ng ZLIB::ZLIB \1/' CMakeLists.txt
sed -i 's/ZLIB::ZLIB/ZLIB::ZLIB z/' Source/Core/*/CMakeLists.txt

#Font license, drop the install directory into thie file
echo "%{_datadir}/%{name}/Sys/GC:" > font-licenses.txt
cat Data/Sys/GC/font-licenses.txt >> font-licenses.txt

###Remove Bundled:
cd Externals
#Keep what we need...
for d in *; do
    if ! echo " %{bundled_libs} " | grep " $d "; then
        rm -rf "$d"
    fi
done
#Copy in system picojson
mkdir picojson
#In master, picojson has build option "PICOJSON_NOEXCEPT", but for now:
sed "s/throw std::.*;/std::abort();/g" /usr/include/picojson.h > \
    picojson/picojson.h

%build

%cmake \
       -DUSE_SYSTEM_LIBS=ON \
       -DXXHASH_FOUND=ON \
       -DUSE_MGBA=OFF \
       -DUSE_SYSTEM_MBEDTLS=OFF \
       %{?!enablejit:-DENABLE_GENERIC=ON} \
       -DENABLE_ANALYTICS=OFF \
       -DENCODE_FRAMEDUMPS=OFF \
       -DUSE_DISCORD_PRESENCE=OFF \
       -DUSE_RETRO_ACHIEVEMENTS=OFF
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 Data/51-usb-device.rules %{buildroot}%{_udevrulesdir}/51-dolphin-usb-device.rules
mv %{buildroot}/%{_bindir}/%{name} %{buildroot}/%{_bindir}/%{name}-x11
echo -e '#!/usr/bin/bash\nQT_QPA_PLATFORM=xcb %{name}-x11 "$@"' \
  > %{buildroot}/%{_bindir}/%{name}
sed -i "s/^Exec=.*/Exec=dolphin-emu/g" \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
ln -s %{name}.6 %{buildroot}/%{_mandir}/man6/%{name}-x11.6
install -p -D -m 0644 %{SOURCE1} \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%cmake_build --target unittests
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n dolphin-emu-nogui -f %{oreon_filedir}/dolphin-emu-nogui.list
%files -n dolphin-emu-tool -f %{oreon_filedir}/dolphin-emu-tool.list
%files -n dolphin-emu-data -f %{oreon_filedir}/dolphin-emu-data.list

%changelog

%autochangelog
