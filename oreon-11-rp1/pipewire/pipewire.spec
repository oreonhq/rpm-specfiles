%global source0_hash dbc3624cf71215c26a22fc98f6f71f7b8599f5f6b415eab4a5c90ca96c170c7c
%global majorversion 1
%global minorversion 6
%global microversion 9
%global apiversion   0.3
%global spaversion   0.2
%global soversion    0
%global libversion   %{soversion}.%(bash -c '((intversion = (%{minorversion} * 100) + %{microversion})); echo ${intversion}').0
%global ms_version   0.4.2
%global baserelease 1
%global _hardened_build 1
%global multilib_archs x86_64 %{ix86} ppc64 ppc s390x s390 sparc64 sparcv9 ppc64le
%bcond_without alsa
%bcond_without vulkan
%bcond_without pulse
%bcond_without jack
%bcond_without jackserver_plugin
%bcond_without libmysofa
%bcond_without lv2
%bcond_without roc
%ifarch s390x
%bcond_with ffado
%bcond_with onnx
%elifarch %{ix86}
%bcond_without ffado
%bcond_with onnx
%else
%bcond_without ffado
%bcond_without onnx
%endif
%bcond_without libcamera_plugin
%bcond_without v4l2
Name:           pipewire
Summary:        Media Sharing Server
Version:        %{majorversion}.%{minorversion}.%{microversion}
Release:        1%{?dist}
License:        MIT
URL:            https://pipewire.org/
%if 0%{?snapdate}
Source0:        https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/%{version}/pipewire-%{version}.tar.gz
%else
%endif
Source1:        pipewire.sysusers
%ifnarch s390x
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       systemd
Requires:       rtkit
Requires:       pipewire-session-manager
Suggests:       wireplumber
Recommends:     pipewire-plugin-libcamera
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  avahi-devel
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libcamera-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libdrm-devel
BuildRequires:  libebur128-devel
BuildRequires:  libffado-devel
BuildRequires:  liblc3-devel
BuildRequires:  libmysofa-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libunwind-devel
BuildRequires:  libusb1-devel
BuildRequires:  libuv-devel
BuildRequires:  libv4l-devel
BuildRequires:  lilv-devel
BuildRequires:  meson
BuildRequires:  ncurses-devel
BuildRequires:  onnxruntime-devel
BuildRequires:  openfec-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-net-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(ldacBT-abr)
BuildRequires:  pkgconfig(ldacBT-enc)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(webrtc-audio-processing-2)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python-docutils
BuildRequires:  readline-devel
BuildRequires:  roc-toolkit-devel
BuildRequires:  sbc-devel
BuildRequires:  sox-devel
BuildRequires:  spandsp-devel
BuildRequires:  speexdsp-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
PipeWire is a multimedia server for Linux and other Unix like operating
systems.

%package libs
Summary:        Libraries for PipeWire clients
License:        MIT AND GPL-2.0-or-later AND BSD-2-Clause AND LGPL-2.0-or-later
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-libpulse < %{version}-%{release}
%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PipeWire media server.

%package gstreamer
Summary:        GStreamer elements for PipeWire
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description gstreamer
This package contains GStreamer elements to interface with a
PipeWire media server.

%package devel
Summary:        Headers and libraries for PipeWire client development
License:        MIT
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Headers and libraries for developing applications that can communicate with
a PipeWire media server.

%package doc
Summary:        PipeWire media server documentation
License:        MIT
%description doc
This package contains documentation for the PipeWire media server.

%package utils
Summary:        PipeWire media server utilities
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description utils
This package contains command line utilities for the PipeWire media server.

%if %{with alsa}
%package alsa
Summary:        PipeWire media server ALSA support
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description alsa
This package contains an ALSA plugin for the PipeWire media server.
%endif

%if %{with jack}
%package jack-audio-connection-kit-libs
Summary:        PipeWire JACK implementation libraries
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-jack-audio-connection-kit%{?_isa} = %{version}-%{release}
Conflicts:      %{name}-libjack < 0.3.13-6
Conflicts:      %{name}-jack-audio-connection-kit < 0.3.13-6
Obsoletes:      %{name}-libjack < 0.3.19-2
Provides:       %{name}-libjack = %{version}-%{release}
Provides:       %{name}-libjack%{?_isa} = %{version}-%{release}
%description jack-audio-connection-kit-libs
This package provides a JACK implementation libraries based on PipeWire

%package jack-audio-connection-kit
Summary:        PipeWire JACK implementation
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-jack-audio-connection-kit-libs%{?_isa} = %{version}-%{release}
%description jack-audio-connection-kit
This package provides a JACK implementation based on PipeWire

%package jack-audio-connection-kit-devel
Summary:        Development files for %{name}-jack-audio-connection-kit
License:        MIT
Requires:       %{name}-jack-audio-connection-kit-libs%{?_isa} = %{version}-%{release}
Conflicts:      jack-audio-connection-kit-devel
Enhances:       %{name}-jack-audio-connection-kit-libs
%description jack-audio-connection-kit-devel
This package provides development files for building JACK applications
using PipeWire's JACK library.
%endif

%if %{with jackserver_plugin}
%package plugin-jack
Summary:        PipeWire media server JACK support
License:        MIT
BuildRequires:  jack-audio-connection-kit-devel
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-jack-audio-connection-kit-libs = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       jack-audio-connection-kit
%description plugin-jack
This package contains the PipeWire spa plugin to connect to a JACK server.
%endif

%if %{with libcamera_plugin}
%package plugin-libcamera
Summary:        PipeWire media server libcamera support
License:        MIT
BuildRequires:  libcamera-devel
BuildRequires:  libdrm-devel
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libcamera
Requires:       libdrm
%description plugin-libcamera
This package contains the PipeWire spa plugin to access cameras through libcamera.
%endif

%if %{with vulkan}
%package plugin-vulkan
Summary:        PipeWire media server vulkan support
License:        MIT
BuildRequires:  pkgconfig(vulkan)
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description plugin-vulkan
This package contains the PipeWire spa plugin for vulkan.
%endif

%if %{with pulse}
%package pulseaudio
Summary:        PipeWire PulseAudio implementation
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Conflicts:      pulseaudio
Conflicts:      %{name}-libpulse < 0.3.13-6
Conflicts:      %{name}-pulseaudio < 0.3.13-6
Provides:       pulseaudio-daemon
Conflicts:      pulseaudio-daemon
Provides:       pulseaudio-module-bluetooth
Provides:       pulseaudio-module-jack
%description pulseaudio
This package provides a PulseAudio implementation based on PipeWire
%endif

%if %{with v4l2}
%package v4l2
Summary:        PipeWire media server v4l2 LD_PRELOAD support
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description v4l2
This package contains an LD_PRELOAD library that redirects v4l2 applications to
PipeWire.
%endif

%package module-x11
Summary:        PipeWire media server x11 support
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description module-x11
This package contains X11 bell support for PipeWire.

%if %{with ffado}
%package module-ffado
Summary:        PipeWire media server ffado support
License:        MIT AND GPL-2.0-only OR GPL-3.0-only
BuildRequires:  libffado-devel
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description module-ffado
This package contains the FFADO support for PipeWire.
%endif

%if %{with roc}
%package module-roc
Summary:        PipeWire media server ROC support
License:        MIT AND MPL-2.0 AND LGPL-2.1-or-later AND CECILL-C
BuildRequires:  roc-toolkit-devel
BuildRequires:  libunwind-devel
BuildRequires:  openfec-devel
BuildRequires:  sox-devel
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description module-roc
This package contains the ROC support for PipeWire.
%endif

%if %{with libmysofa}
%package module-filter-chain-sofa
Summary:        PipeWire media server sofa filter-chain support
License:        MIT AND BSD-3-Clause
BuildRequires:  libmysofa-devel
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description module-filter-chain-sofa
This package contains the mysofa support for PipeWire filter-chain.
%endif

%if %{with lv2}
%package module-filter-chain-lv2
Summary:        PipeWire media server lv2 filter-chain support
License:        MIT
BuildRequires:  lilv-devel
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description module-filter-chain-lv2
This package contains the mysofa support for PipeWire filter-chain.
%endif

%if %{with onnx}
%package module-filter-chain-onnx
Summary:        PipeWire media server ONNX filter-chain support
License:        MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
BuildRequires:  onnxruntime-devel
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description module-filter-chain-onnx
This package contains the ONNX support for PipeWire filter-chain.
%endif

%package config-rates
Summary:        PipeWire media server multirate configuration
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description config-rates
This package contains the configuration files to support multiple
sample rates.

%package config-upmix
Summary:        PipeWire media server upmixing configuration
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description config-upmix
This package contains the configuration files to support upmixing.

%package config-raop
Summary:        PipeWire configuration enabling the raop module
License:        MIT
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description config-raop
This package contains the configuration file to enable the RAOP module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 %{?snapdate:-n %{name}-%{gitcommit}}

%if %{with media-session}
mkdir subprojects/packagefiles
cp %{SOURCE1} subprojects/packagefiles/
%endif

%build

%meson \
    -D docs=enabled -D man=enabled -D gstreamer=enabled -D libsystemd=enabled	\
    -D systemd-user-service=enabled 						\
    -D sdl2=disabled 								\
    -D audiotestsrc=disabled -D videotestsrc=disabled				\
    -D volume=disabled -D bluez5-codec-aptx=disabled 		  		\
    -D bluez5-codec-lc3plus=disabled -D bluez5-codec-lc3=enabled		\
    -D bluez5-codec-ldac-dec=disabled 						\
%ifarch s390x
    -D bluez5-codec-ldac=disabled						\
%endif
    -D session-managers=[] 							\
    -D rtprio-server=60 -D rtprio-client=55 -D rlimits-rtprio=70		\
    -D snap=disabled								\
    %{!?with_jack:-D pipewire-jack=disabled} 					\
    %{!?with_jackserver_plugin:-D jack=disabled} 				\
    %{!?with_libcamera_plugin:-D libcamera=disabled} 				\
    %{?with_jack:-D jack-devel=true} 						\
    %{!?with_alsa:-D pipewire-alsa=disabled}					\
    %{?with_vulkan:-D vulkan=enabled}						\
    %{!?with_libmysofa:-D libmysofa=disabled}					\
    %{!?with_lv2:-D lv2=disabled}						\
    %{!?with_onnx:-D onnxruntime=disabled}					\
    %{!?with_roc:-D roc=disabled}						\
    %{!?with_ffado:-D libffado=disabled}					\
    %{nil}
%meson_build
%install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/pipewire.conf
%meson_install
install -d -m 0755 %{buildroot}%{_datadir}/pipewire/pipewire.conf.d/
install -d -m 0755 %{buildroot}%{_datadir}/pipewire/client.conf.d/
%if %{with jack}
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo %{_libdir}/pipewire-%{apiversion}/jack/ > %{buildroot}%{_sysconfdir}/ld.so.conf.d/pipewire-jack-%{_arch}.conf
%else
rm %{buildroot}%{_datadir}/pipewire/jack.conf
%endif
%if %{with alsa}
mkdir -p %{buildroot}%{_sysconfdir}/alsa/conf.d/
cp %{buildroot}%{_datadir}/alsa/alsa.conf.d/50-pipewire.conf \
        %{buildroot}%{_sysconfdir}/alsa/conf.d/50-pipewire.conf
cp %{buildroot}%{_datadir}/alsa/alsa.conf.d/99-pipewire-default.conf \
        %{buildroot}%{_sysconfdir}/alsa/conf.d/99-pipewire-default.conf
%endif
%if ! %{with pulse}
rm %{buildroot}%{_bindir}/pipewire-pulse
rm %{buildroot}%{_userunitdir}/pipewire-pulse.*
rm %{buildroot}%{_datadir}/pipewire/pipewire-pulse.conf
%endif
%if %{with pulse}
install -d -m 0755 %{buildroot}%{_datadir}/pipewire/pipewire-pulse.conf.d/
ln -s ../pipewire-pulse.conf.avail/20-upmix.conf \
		%{buildroot}%{_datadir}/pipewire/pipewire-pulse.conf.d/20-upmix.conf
%endif
ln -s ../pipewire.conf.avail/10-rates.conf \
		%{buildroot}%{_datadir}/pipewire/pipewire.conf.d/10-rates.conf
ln -s ../pipewire.conf.avail/20-upmix.conf \
		%{buildroot}%{_datadir}/pipewire/pipewire.conf.d/20-upmix.conf
ln -s ../client.conf.avail/20-upmix.conf \
		%{buildroot}%{_datadir}/pipewire/client.conf.d/20-upmix.conf
ln -s ../pipewire.conf.avail/50-raop.conf \
		%{buildroot}%{_datadir}/pipewire/pipewire.conf.d/50-raop.conf
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test || TESTS_ERROR=$?
if [ "${TESTS_ERROR}" != "" ]; then
echo "test failed"
%{!?tests_nonfatal:exit $TESTS_ERROR}
fi
%post

%systemd_user_post pipewire.service
%systemd_user_post pipewire.socket
%triggerun -- %{name} < 0.3.6-2

systemctl --no-reload preset --global pipewire.socket >/dev/null 2>&1 || :
%if %{with pulse}
%post pulseaudio

%systemd_user_post pipewire-pulse.service
%systemd_user_post pipewire-pulse.socket
%endif
%files -f %{oreon_filedir}/main.list
%files -n pipewire-libs -f %{oreon_filedir}/pipewire-libs.list
%files -n pipewire-gstreamer -f %{oreon_filedir}/pipewire-gstreamer.list
%files -n pipewire-devel -f %{oreon_filedir}/pipewire-devel.list
%files -n pipewire-doc -f %{oreon_filedir}/pipewire-doc.list
%files -n pipewire-utils -f %{oreon_filedir}/pipewire-utils.list
%files -n pipewire-alsa -f %{oreon_filedir}/pipewire-alsa.list
%files -n pipewire-jack-audio-connection-kit-libs -f %{oreon_filedir}/pipewire-jack-audio-connection-kit-libs.list
%files -n pipewire-jack-audio-connection-kit -f %{oreon_filedir}/pipewire-jack-audio-connection-kit.list
%files -n pipewire-jack-audio-connection-kit-devel -f %{oreon_filedir}/pipewire-jack-audio-connection-kit-devel.list
%files -n pipewire-plugin-jack -f %{oreon_filedir}/pipewire-plugin-jack.list
%files -n pipewire-plugin-libcamera -f %{oreon_filedir}/pipewire-plugin-libcamera.list
%files -n pipewire-plugin-vulkan -f %{oreon_filedir}/pipewire-plugin-vulkan.list
%files -n pipewire-pulseaudio -f %{oreon_filedir}/pipewire-pulseaudio.list
%files -n pipewire-v4l2 -f %{oreon_filedir}/pipewire-v4l2.list
%files -n pipewire-module-x11 -f %{oreon_filedir}/pipewire-module-x11.list
%files -n pipewire-module-ffado -f %{oreon_filedir}/pipewire-module-ffado.list
%files -n pipewire-module-roc -f %{oreon_filedir}/pipewire-module-roc.list
%files -n pipewire-module-filter-chain-sofa -f %{oreon_filedir}/pipewire-module-filter-chain-sofa.list
%files -n pipewire-module-filter-chain-lv2 -f %{oreon_filedir}/pipewire-module-filter-chain-lv2.list
%files -n pipewire-module-filter-chain-onnx -f %{oreon_filedir}/pipewire-module-filter-chain-onnx.list
%files -n pipewire-config-rates -f %{oreon_filedir}/pipewire-config-rates.list
%files -n pipewire-config-upmix -f %{oreon_filedir}/pipewire-config-upmix.list
%files -n pipewire-config-raop -f %{oreon_filedir}/pipewire-config-raop.list

%changelog

%autochangelog
