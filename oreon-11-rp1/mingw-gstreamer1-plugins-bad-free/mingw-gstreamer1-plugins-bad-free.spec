%global source0_hash 56c1593787f8b5550893d59e4ff29e6bcccf34973316fa55e34ce493e04313a2

%{?mingw_package_header}
%bcond_without extras

%global         api_version     1.0

Name:           mingw-gstreamer1-plugins-bad-free
Version:        1.28.1
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 plug-ins "bad"

# main code is LGPL-2.1-or-later AND LGPL-2.0-or-later
# ext/aes/gstaeshelper.h ext/curl/curltask.h and several others are MIT OR LGPL-2.1-or-later
# ext/resindvd is MPL-1.1
# ext/sctp is BSD-2-Clause AND BSD-3-Clause
# ext/sctp/usrsctp/usrsctplib/netinet/sctp_ss_functions.c is BSD-2-Clause-Views
# ext/sctp/usrsctp/usrsctplib/netinet/sctp_userspace.c is BSD-2-Clause AND DOC
# gst/festival/gstfestival.c is MIT-Festival
# gst/freeverb/gstfreeverb.c is LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
# gst/mpegpsmux/mpegpsmux_h264.h is MPL-1.1 OR LGPL-2.0-or-later OR MIT
# gst-libs/gst/codecparsers/dboolhuff.c is BSD-3-Clause WITH AdditionRef-Dart
# sys/amfcode sys/dwrite/libcaption/ sys/qsv/libmfx/ are MIT
# sys/v4l2codecs/linux/media.h plus few other filese in this directory are GPL-2.0-only WITH Linux-syscall-note
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later AND (MIT OR LGPL-2.1-or-later) AND MPL-1.1 AND BSD-2-Clause AND BSD-3-Clause AND BSD-2-Clause-Views AND (BSD-2-Clause AND DOC) AND MIT-Festival AND (LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain) AND (MPL-1.1 OR LGPL-2.0-or-later OR MIT) AND BSD-3-Clause WITH AdditionRef-Dart AND MIT AND GPL-2.0-only WITH Linux-syscall-note
URL:            http://gstreamer.freedesktop.org/
Source:         https://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
# Adapt for directxmath header location
Patch1:         gst-p-bad-directxmath.patch

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  orc-compiler

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-directxmath
BuildRequires:  mingw64-directxmath
BuildRequires:  mingw32-gstreamer1 >= %{version}
BuildRequires:  mingw64-gstreamer1 >= %{version}
BuildRequires:  mingw32-gstreamer1-plugins-base >= %{version}
BuildRequires:  mingw64-gstreamer1-plugins-base >= %{version}
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-curl
BuildRequires:  mingw64-curl
BuildRequires:  mingw32-directx-headers
BuildRequires:  mingw64-directx-headers
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw32-gsm
BuildRequires:  mingw64-gsm
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-librsvg2
BuildRequires:  mingw64-librsvg2
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-nettle
BuildRequires:  mingw64-nettle
BuildRequires:  mingw32-openexr
BuildRequires:  mingw64-openexr
BuildRequires:  mingw32-openal-soft
BuildRequires:  mingw64-openal-soft
BuildRequires:  mingw32-openjpeg2
BuildRequires:  mingw64-openjpeg2
BuildRequires:  mingw32-opus
BuildRequires:  mingw64-opus
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack

# For glib-genmarshal
BuildRequires:  glib2-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.

# Mingw32
%package -n mingw32-gstreamer1-plugins-bad-free
Summary:        %{summary}
Requires:       mingw32-gstreamer1 >= %{version}
Obsoletes:      mingw32-gstreamer1-plugins-bad < 1.14.1-1
Provides:       mingw32-gstreamer1-plugins-bad = 1.14.1-1
Requires:       mingw32-directxmath
Requires:       mingw32-directx-headers

%description -n mingw32-gstreamer1-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.

# Mingw64
%package -n mingw64-gstreamer1-plugins-bad-free
Summary:        %{summary}
Requires:       mingw64-gstreamer1 >= %{version}
Obsoletes:      mingw64-gstreamer1-plugins-bad < 1.14.1-1
Provides:       mingw64-gstreamer1-plugins-bad = 1.14.1-1
Requires:       mingw64-directxmath
Requires:       mingw64-directx-headers

%description -n mingw64-gstreamer1-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gst-plugins-bad-%{version}

%build
#   chromaprint was enabled in the !mingw package in 6eadf04
#   openal, openjpeg, ofa, webp were enabled in the !mingw package in c609b28
#   there are mingw-openjpeg and mingw-webp packages available
#   uvch264 was enabled in the !mingw package in fcee991
#   curl and winks are disabled only in the mingw package
%global _old_mingw32_cflags %{mingw32_cflags}
%global mingw32_cflags %{_old_mingw32_cflags} -msse2
%global _old_mingw64_cflags %{mingw64_cflags}
%global mingw64_cflags %{_old_mingw64_cflags} -msse2
%mingw_meson \
    -Dpackage-name="Fedora Mingw GStreamer-plugins-bad package" \
    -Dpackage-origin="http://download.fedoraproject.org" \
    %{!?with_extras:-D fbdev=disabled -D decklink=disabled } \
    %{!?with_extras:-D assrender=disabled -D bs2b=disabled } \
    %{!?with_extras:-D chromaprint=disabled -D d3dvideosink=disabled } \
    %{!?with_extras:-D directsound=disabled -D dts=disabled } \
    %{!?with_extras:-D fluidsynth=disabled -D openexr=disabled } \
    %{!?with_extras:-D curl=disabled -D curl-ssh2=disabled } \
    %{!?with_extras:-D ttml=disabled -D kate=disabled } \
    %{!?with_extras:-D modplug=disabled -D ofa=disabled } \
    %{!?with_extras:-D vdpau=disabled -D openal=disabled } \
    %{!?with_extras:-D opencv=disabled -D openjpeg=disabled } \
    %{!?with_extras:-D wildmidi=disabled -D zbar=disabled } \
    %{!?with_extras:-D gme=disabled -D lv2=disabled } \
    -D doc=disabled -D magicleap=disabled -D msdk=disabled \
    -D dts=disabled -D faac=disabled -D faad=disabled \
    -D mpeg2enc=disabled -D mplex=disabled \
    -D neon=disabled -D rtmp=disabled -D rtmp2=disabled \
    -D flite=disabled -D sbc=disabled -D opencv=disabled \
    %{!?with_extras:-D spandsp=disabled -D va=disabled } \
    -D voamrwbenc=disabled -D x265=disabled \
    -D dvbsuboverlay=disabled -D dvdspu=disabled -D siren=disabled \
    -D opensles=disabled -D tinyalsa=disabled \
    -D wasapi=enabled -D wasapi2=disabled -D avtp=disabled \
    -D dc1394=disabled -D directfb=disabled -D iqa=disabled \
    -D libde265=disabled -D musepack=disabled -D openni2=disabled \
    -D sctp=disabled -D svthevcenc=disabled -D voaacenc=disabled \
    -D zxing=disabled -D wpe=disabled -D x11=disabled \
    -D openh264=disabled \
    -D examples=disabled -D tests=disabled \
    -D codec2json=disabled

%mingw_ninja

%install
%mingw_ninja_install

# Clean out files that should not be part of the rpm.
rm -f %{buildroot}%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a

%mingw_find_lang gstreamer1-plugins-bad-free --all-name

# Mingw32
%files -n mingw32-gstreamer1-plugins-bad-free -f mingw32-gstreamer1-plugins-bad-free.lang
%license COPYING
%doc README.md
%{mingw32_bindir}/gst-transcoder-1.0.exe
# libraries
%{mingw32_bindir}/libgstadaptivedemux-1.0-0.dll
%{mingw32_bindir}/libgstanalytics-1.0-0.dll
%{mingw32_bindir}/libgstbadaudio-1.0-0.dll
%{mingw32_bindir}/libgstbasecamerabinsrc-1.0-0.dll
%{mingw32_bindir}/libgstcodecs-1.0-0.dll
%{mingw32_bindir}/libgstcodecparsers-1.0-0.dll
%{mingw32_bindir}/libgstcuda-1.0-0.dll
%{mingw32_bindir}/libgstd3d11-1.0-0.dll
%{mingw32_bindir}/libgstd3d12-1.0-0.dll
%{mingw32_bindir}/libgstd3dshader-1.0-0.dll
%{mingw32_bindir}/libgstdxva-1.0-0.dll
%{mingw32_bindir}/libgsthip-0.dll
%{mingw32_bindir}/libgstinsertbin-1.0-0.dll
%{mingw32_bindir}/libgstisoff-1.0-0.dll
%{mingw32_bindir}/libgstmpegts-1.0-0.dll
%{mingw32_bindir}/libgstmse-1.0-0.dll
%{mingw32_bindir}/libgstphotography-1.0-0.dll
%{mingw32_bindir}/libgstplay-1.0-0.dll
%{mingw32_bindir}/libgstplayer-1.0-0.dll
%{mingw32_bindir}/libgstsctp-1.0-0.dll
%{mingw32_bindir}/libgsttranscoder-1.0-0.dll
%{mingw32_bindir}/libgsturidownloader-1.0-0.dll
%{mingw32_bindir}/libgstwebrtc-1.0-0.dll

# bad plugins
%dir %{mingw32_libdir}/gstreamer-%{api_version}
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaccurip.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstadpcmdec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstadpcmenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaes.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaiff.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstanalyticsoverlay.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstasfmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstasio.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiobuffersplit.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiofxbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiolatency.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiomixmatrix.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiovisualizers.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstautoconvert.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstbayer.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstbz2.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcamerabin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstclosedcaption.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcodecalpha.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcoloreffects.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcolormanagement.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcurl.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstd3d.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstd3d11.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstd3d12.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdash.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdebugutilsbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdecklink.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdirectsoundsrc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdtls.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdwrite.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdvbsubenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfaceoverlay.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfestival.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfieldanalysis.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfreeverb.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfrei0r.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgaudieffects.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgdp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgeometrictransform.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgsm.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsthip.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsthls.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstid3tag.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinsertbin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinter.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinterlace.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstipcpipeline.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstivfparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstivtc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjp2kdecimator.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjpegformat.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstlegacyrawparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmediafoundation.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmidi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegpsdemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegpsmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegtsdemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegtsmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmxf.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnetsim.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnvcodec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopenal.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopenexr.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopenjpeg.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopusparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpcapparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpnm.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstproxy.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstremovesilence.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrfbsrc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrist.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrsvg.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtpmanagerbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtponvif.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsdpelem.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsegmentclip.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmooth.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmoothstreaming.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstspeed.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsubenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstswitchbin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttensordecoders.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttimecode.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttranscode.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstttmlsubs.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideofiltersbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideoframe_audiolevel.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideoparsersbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideosignal.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvmnc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwasapi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwebp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwinks.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwinscreencap.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstamfcodec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcodectimestamper.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstqsv.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwin32ipc.dll

# plugin helper library headers
%{mingw32_includedir}/gstreamer-%{api_version}/gst/analytics/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/audio/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/basecamerabinsrc/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/codecparsers/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/hip/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/interfaces/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/insertbin/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/isoff/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/mse/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/mpegts/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/play/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/player/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/sctp/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/transcoder/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/uridownloader/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/webrtc/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/cuda/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/d3d11/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/d3d12/

%{mingw32_libdir}/gstreamer-%{api_version}/include/
%{mingw32_libdir}/libgstadaptivedemux-%{api_version}.dll.a
%{mingw32_libdir}/libgstanalytics-%{api_version}.dll.a
%{mingw32_libdir}/libgstbadaudio-%{api_version}.dll.a
%{mingw32_libdir}/libgstbasecamerabinsrc-%{api_version}.dll.a
%{mingw32_libdir}/libgstcodecs-%{api_version}.dll.a
%{mingw32_libdir}/libgstcodecparsers-%{api_version}.dll.a
%{mingw32_libdir}/libgstd3d11-%{api_version}.dll.a
%{mingw32_libdir}/libgstd3d12-%{api_version}.dll.a
%{mingw32_libdir}/libgstd3dshader-%{api_version}.dll.a
%{mingw32_libdir}/libgstdxva-%{api_version}.dll.a
%{mingw32_libdir}/libgsthip.dll.a
%{mingw32_libdir}/libgstinsertbin-%{api_version}.dll.a
%{mingw32_libdir}/libgstisoff-%{api_version}.dll.a
%{mingw32_libdir}/libgstmpegts-%{api_version}.dll.a
%{mingw32_libdir}/libgstmse-%{api_version}.dll.a
%{mingw32_libdir}/libgstphotography-%{api_version}.dll.a
%{mingw32_libdir}/libgstplay-%{api_version}.dll.a
%{mingw32_libdir}/libgstplayer-%{api_version}.dll.a
%{mingw32_libdir}/libgstsctp-%{api_version}.dll.a
%{mingw32_libdir}/libgsttranscoder-%{api_version}.dll.a
%{mingw32_libdir}/libgsturidownloader-%{api_version}.dll.a
%{mingw32_libdir}/libgstwebrtc-%{api_version}.dll.a
%{mingw32_libdir}/libgstcuda-%{api_version}.dll.a

%{mingw32_libdir}/pkgconfig/gstreamer-analytics-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-bad-audio-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-codecparsers-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-hip-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-hip-gl-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-insertbin-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-mpegts-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-mse-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-photography-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-play-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-player-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-plugins-bad-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-sctp-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-transcoder-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-webrtc-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-cuda-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-d3d11-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-d3d12-%{api_version}.pc

%{mingw32_datadir}/gstreamer-%{api_version}/presets/
%{mingw32_datadir}/gstreamer-%{api_version}/encoding-profiles/

# Mingw64
%files -n mingw64-gstreamer1-plugins-bad-free -f mingw64-gstreamer1-plugins-bad-free.lang
%license COPYING
%doc README.md
%{mingw64_bindir}/gst-transcoder-1.0.exe
# libraries
%{mingw64_bindir}/libgstadaptivedemux-1.0-0.dll
%{mingw64_bindir}/libgstanalytics-1.0-0.dll
%{mingw64_bindir}/libgstbadaudio-1.0-0.dll
%{mingw64_bindir}/libgstbasecamerabinsrc-1.0-0.dll
%{mingw64_bindir}/libgstcodecs-1.0-0.dll
%{mingw64_bindir}/libgstcodecparsers-1.0-0.dll
%{mingw64_bindir}/libgstcuda-1.0-0.dll
%{mingw64_bindir}/libgstd3d11-1.0-0.dll
%{mingw64_bindir}/libgstd3d12-1.0-0.dll
%{mingw64_bindir}/libgstd3dshader-1.0-0.dll
%{mingw64_bindir}/libgstdxva-1.0-0.dll
%{mingw64_bindir}/libgsthip-0.dll
%{mingw64_bindir}/libgstinsertbin-1.0-0.dll
%{mingw64_bindir}/libgstisoff-1.0-0.dll
%{mingw64_bindir}/libgstmpegts-1.0-0.dll
%{mingw64_bindir}/libgstmse-1.0-0.dll
%{mingw64_bindir}/libgstphotography-1.0-0.dll
%{mingw64_bindir}/libgstplay-1.0-0.dll
%{mingw64_bindir}/libgstplayer-1.0-0.dll
%{mingw64_bindir}/libgstsctp-1.0-0.dll
%{mingw64_bindir}/libgsttranscoder-1.0-0.dll
%{mingw64_bindir}/libgsturidownloader-1.0-0.dll
%{mingw64_bindir}/libgstwebrtc-1.0-0.dll

# bad plugins
%dir %{mingw64_libdir}/gstreamer-%{api_version}
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaccurip.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstadpcmdec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstadpcmenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaes.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaiff.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstanalyticsoverlay.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstasfmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstasio.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiobuffersplit.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiofxbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiolatency.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiomixmatrix.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiovisualizers.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstautoconvert.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstbayer.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstbz2.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcamerabin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstclosedcaption.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcodecalpha.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcoloreffects.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcolormanagement.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcurl.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstd3d.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstd3d11.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstd3d12.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdash.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdebugutilsbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdecklink.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdirectsoundsrc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdtls.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdwrite.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdvbsubenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfaceoverlay.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfestival.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfieldanalysis.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfreeverb.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfrei0r.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgaudieffects.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgdp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgeometrictransform.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgsm.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsthip.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsthls.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstid3tag.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinsertbin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinter.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinterlace.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstipcpipeline.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstivfparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstivtc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjp2kdecimator.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjpegformat.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstlegacyrawparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmediafoundation.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmidi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegpsdemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegpsmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegtsdemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegtsmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmxf.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnetsim.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnvcodec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopenal.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopenexr.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopenjpeg.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopusparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpcapparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpnm.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstproxy.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstremovesilence.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrfbsrc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrist.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrsvg.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtpmanagerbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtponvif.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsdpelem.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsegmentclip.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmooth.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmoothstreaming.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstspeed.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsubenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstswitchbin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttensordecoders.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttimecode.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttranscode.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstttmlsubs.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideofiltersbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideoframe_audiolevel.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideoparsersbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideosignal.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvmnc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwasapi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwebp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwinks.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwinscreencap.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstamfcodec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcodectimestamper.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstqsv.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwin32ipc.dll

# plugin helper library headers
%{mingw64_includedir}/gstreamer-%{api_version}/gst/analytics/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/audio/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/basecamerabinsrc/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/codecparsers/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/hip/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/interfaces/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/insertbin/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/isoff/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/mse/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/mpegts/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/play/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/player/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/sctp/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/transcoder/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/uridownloader/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/webrtc/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/cuda/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/d3d11/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/d3d12/

%{mingw64_libdir}/gstreamer-%{api_version}/include/
%{mingw64_libdir}/libgstadaptivedemux-%{api_version}.dll.a
%{mingw64_libdir}/libgstanalytics-%{api_version}.dll.a
%{mingw64_libdir}/libgstbadaudio-%{api_version}.dll.a
%{mingw64_libdir}/libgstbasecamerabinsrc-%{api_version}.dll.a
%{mingw64_libdir}/libgstcodecs-%{api_version}.dll.a
%{mingw64_libdir}/libgstcodecparsers-%{api_version}.dll.a
%{mingw64_libdir}/libgstd3d11-%{api_version}.dll.a
%{mingw64_libdir}/libgstd3d12-%{api_version}.dll.a
%{mingw64_libdir}/libgstd3dshader-%{api_version}.dll.a
%{mingw64_libdir}/libgstdxva-%{api_version}.dll.a
%{mingw64_libdir}/libgsthip.dll.a
%{mingw64_libdir}/libgstinsertbin-%{api_version}.dll.a
%{mingw64_libdir}/libgstisoff-%{api_version}.dll.a
%{mingw64_libdir}/libgstmpegts-%{api_version}.dll.a
%{mingw64_libdir}/libgstmse-%{api_version}.dll.a
%{mingw64_libdir}/libgstphotography-%{api_version}.dll.a
%{mingw64_libdir}/libgstplay-%{api_version}.dll.a
%{mingw64_libdir}/libgstplayer-%{api_version}.dll.a
%{mingw64_libdir}/libgstsctp-%{api_version}.dll.a
%{mingw64_libdir}/libgsttranscoder-%{api_version}.dll.a
%{mingw64_libdir}/libgsturidownloader-%{api_version}.dll.a
%{mingw64_libdir}/libgstwebrtc-%{api_version}.dll.a
%{mingw64_libdir}/libgstcuda-%{api_version}.dll.a

%{mingw64_libdir}/pkgconfig/gstreamer-analytics-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-bad-audio-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-codecparsers-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-hip-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-hip-gl-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-insertbin-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-mpegts-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-mse-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-photography-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-play-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-player-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-plugins-bad-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-sctp-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-transcoder-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-webrtc-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-cuda-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-d3d11-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-d3d12-%{api_version}.pc

%{mingw64_datadir}/gstreamer-%{api_version}/presets/
%{mingw64_datadir}/gstreamer-%{api_version}/encoding-profiles/

%changelog
%autochangelog
