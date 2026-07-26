%global source0_hash 879b1bc476c9b93e77ee280a84fc1157e7cc47d43ed9c8398d88a8ac5f35c034

# This is the correct folder for firewalld service files, even on x86_64
# It is not used for shared objects
%global fw_services %{_prefix}/lib/firewalld/services

# Use if gtk2 is not available
%bcond_without gui

%if %{with gui}
%global make_subfolder hdhomerun_config_gui
%else
%global make_subfolder libhdhomerun
%endif

Name:           hdhomerun
Version:        20250506
Release:        3%{?dist}
Summary:        Silicon Dust HDHomeRun configuration utility

License:        LGPL-2.1-or-later
URL:            http://www.silicondust.com/
Source0:        http://download.silicondust.com/hdhomerun/libhdhomerun_%{version}.tgz
Source1:        http://download.silicondust.com/hdhomerun/hdhomerun_config_gui_%{version}.tgz
Source2:        hdhomerun_config_gui.desktop
Source3:        %{name}.xml

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed

%if %{with gui}
BuildRequires:  gtk2-devel
BuildRequires:  libicns-utils
BuildRequires:  desktop-file-utils
%endif

%description
The configuration and firmware upgrade utility for Silicon Dust's
networked HDTV dual-tuner HDHomeRun device.

%package devel
Summary: Developer tools for the hdhomerun library
Requires: hdhomerun%{?_isa} = %{version}-%{release}

%description devel
The hdhumerun-devel package provides developer tools for the hdhomerun library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -a 1

# Fix up linefeeds, drop execute bit and don't strip binaries
#sed -i 's/\r//' libhdhomerun/*
sed -i -e '/$(STRIP).*/d' -e 's/C\(PP\)\?FLAGS .=/C\1FLAGS ?=/' libhdhomerun/Makefile

# Convert files to utf8
for f in libhdhomerun/*; do
  /usr/bin/iconv -f iso-8859-1 -t utf-8 --output $f.new $f && mv $f.new $f
done

%build
pushd %{make_subfolder}
%{?with_gui:%configure}
%{?without_gui:%{set_build_flags}}
%make_build
popd

cat << __EOF__ > README.firmware
The HDHomeRun Firmwares are not redistributable, but the latest versions of
both the US ATSC and European DVB-T firmwares can always be obtained from
the Silicon Dust web site:

https://www.silicondust.com/support/linux/

__EOF__

%if %{with gui}
pushd %{make_subfolder}/OSX
icns2png -x hdhr.icns
popd
%endif

%install
%if %{with gui}
%make_install -C %{make_subfolder}

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}

for size in 16x16 32x32 128x128 256x256 512x512; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    install -m0755 hdhomerun_config_gui/OSX/hdhr_${size}x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/hdhr.png
done

%else
# SiliconDust puts the install target for libhdhomerun in
# hdhomerun_config_gui, so we do it manually when not including the gui
mkdir -p %{buildroot}%{_libdir}
install -m0755 libhdhomerun/libhdhomerun.so %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_bindir}/
 install -m0755 libhdhomerun/hdhomerun_config %{buildroot}%{_bindir}/
%endif

mkdir include
cp -a libhdhomerun/*.h include
sed -r 's|(^#include +["])(.*)(["] *$)|#include <hdhomerun/\2>|' \
    libhdhomerun/hdhomerun.h > include/hdhomerun.h
mkdir -p %{buildroot}%{_includedir}/hdhomerun
install -p include/*.h %{buildroot}%{_includedir}/hdhomerun/

# Install firewalld config
mkdir -p %{buildroot}%{fw_services}
install -pm 0644 %{SOURCE3} %{buildroot}%{fw_services}/

%files
%license libhdhomerun/LICENSE
%doc libhdhomerun/README.md README.firmware

# lib and cli are LGPLv3
%{_libdir}/libhdhomerun.so
%{_bindir}/hdhomerun_config
%{fw_services}/%{name}.xml

%if %{with gui}
%license hdhomerun_config_gui/COPYING
%doc hdhomerun_config_gui/AUTHORS hdhomerun_config_gui/README

# gui is GPLv3
%{_bindir}/hdhomerun_config_gui
%{_datadir}/applications/hdhomerun_config_gui.desktop
%{_datadir}/icons/hicolor/*/apps/hdhr.png
%endif

%files devel
%dir %{_includedir}/hdhomerun
%{_includedir}/hdhomerun/*.h

%changelog
%autochangelog
