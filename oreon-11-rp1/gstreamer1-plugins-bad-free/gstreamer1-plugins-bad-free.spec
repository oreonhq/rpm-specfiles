# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 a0ab17dddd4c029ecd7a423c30badd5a3c7599ea42707016d1d57545f5723ccf
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global         majorminor 1.0
%global         _gobject_introspection  1.31.1

# AOM plugin needs libaom in the compose. Fedora carries it; on RHEL default
# off so slim installer trees do not hard-require libaom for libgstaom.so.
%if 0%{?rhel}
%bcond_with aom
%else
%bcond_without aom
%endif
%bcond extras %{defined fedora}
%bcond opencv %{defined fedora}
%bcond openh264 %{defined fedora}
%bcond svtav1 %{defined fedora}
# requires new webrtc-audio-processing-1/-2
%bcond webrtc %[ %{defined fedora} || 0%{?rhel} >= 10 ]
%bcond webrtc1 %[ %{with webrtc} && ! (0%{?fedora} >= 44 || 0%{?rhel} >= 11) ]
# The 1394 stack is not built on s390x
# libldac is not built on s390x, see rhbz#1677491
%ifnarch s390x
%bcond dc1394 %{defined fedora}
%bcond ldac %{defined fedora}
%endif
%ifnarch %{ix86} riscv64 s390x
%bcond onnx %{defined fedora}
%endif
# VPL runtimes (intel-mediasdk/intel-vpl-gpu-rt) are x86_64 only
%ifarch x86_64
%bcond vpl %{defined fedora}
%endif

Name:           gstreamer1-plugins-bad-free
Version:        1.26.7
Release:        10%{?dist}
Summary:        GStreamer streaming media framework "bad" plugins

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
%if 0%{?gitrel}
# Git snapshot workflow disabled (use release tarball).
Source0:        gst-plugins-bad-%{version}.tar.xz
%else
Source:         https://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
%endif

# https://gitlab.freedesktop.org/gstreamer/gstreamer/-/merge_requests/5622
Patch0:          openh264-add-license-file.patch

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc-c++
%ifarch x86_64
# work around https://bugzilla.redhat.com/show_bug.cgi?id=2352531
BuildRequires:  libatomic
%endif
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gobject-introspection-devel >= %{_gobject_introspection}

BuildRequires:  bzip2-devel
BuildRequires:  exempi-devel
BuildRequires:  glslc
BuildRequires:  gsm-devel
BuildRequires:  pkgconfig(bluez) >= 5.0
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lc3)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsrtp2)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(orc-0.4)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(vulkan)
%if %{with aom}
BuildRequires:  pkgconfig(aom)
%endif
%if %{with dc1394}
BuildRequires:  pkgconfig(libdc1394-2)
%endif
%if %{with ldac}
BuildRequires:  pkgconfig(ldacBT-enc)
%endif
%if %{with onnx}
BuildRequires:  pkgconfig(libonnxruntime) >= 1.16.1
%endif
%if %{with opencv}
BuildRequires:  pkgconfig(opencv4)
%endif
%if %{with openh264}
BuildRequires:  pkgconfig(openh264)
%endif
%if %{with svtav1}
BuildRequires:  pkgconfig(SvtAv1Enc)
%endif
%if %{with vpl}
BuildRequires:  pkgconfig(vpl) >= 2.2
%endif
%if %{with webrtc}
%if %{with webrtc1}
BuildRequires:  pkgconfig(webrtc-audio-coding-1)
BuildRequires:  pkgconfig(webrtc-audio-processing-1)
%else
BuildRequires:  pkgconfig(webrtc-audio-processing-2)
%endif
%endif
%if %{with extras}
BuildRequires:  faad2-devel
BuildRequires:  flite-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  ladspa-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  pkgconfig(avtp)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdca)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(microdns)
BuildRequires:  pkgconfig(mjpegtools) >= 2.0.0
BuildRequires:  pkgconfig(nice)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(spandsp) >= 0.0.6
BuildRequires:  pkgconfig(srt)
BuildRequires:  pkgconfig(vo-amrwbenc)
BuildRequires:  pkgconfig(wildmidi)
BuildRequires:  pkgconfig(zbar)
BuildRequires:  pkgconfig(zvbi-0.2)
BuildRequires:  pkgconfig(zxing)
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       gstreamer1-vaapi = %{version}-%{release}
Obsoletes:      gstreamer1-vaapi < 1.26.10-3

# mpeg2enc, mplex used to be shipped in -freeworld
Conflicts: gstreamer1-plugins-bad-freeworld < 1:1.26.3-3
# Plugins get moved around from time to time
Conflicts: %{name}-extras < %{version}-%{release}

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code
is not of good enough quality.


%if %{with extras}
%package extras
Summary:         Extra GStreamer "bad" plugins (less often used "bad" plugins)
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description extras
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-extras) contains
extra "bad" plugins for sources (mythtv), sinks (fbdev) and
effects (pitch) which are not used very much and require additional
libraries to be installed.


%package zbar
Summary:         GStreamer "bad" plugins zbar plugin
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description zbar
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-zbar) contains the zbar
plugin which allows decode bar codes.


%package fluidsynth
Summary:         GStreamer "bad" plugins fluidsynth plugin
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        soundfont2-default

%description fluidsynth
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-fluidsynth) contains the fluidsynth
plugin which allows playback of midi files.


%package lv2
Summary:         GStreamer "bad" plugins LV2 plugin
Requires:        %{name}%{?_isa} = %{version}-%{release}
Conflicts:       %{name}-extras < 1.26.2-2

%description lv2
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-lv2) contains the lv2 plugin which allows using
LV2 audio plugins (which need to be installed separately).


%package wildmidi
Summary:         GStreamer "bad" plugins wildmidi plugin
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description wildmidi
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-wildmidi) contains the wildmidi
plugin which allows playback of midi files.
%endif


%if %{with opencv}
%package opencv
Summary:         GStreamer "bad" plugins OpenCV plugins
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        opencv-data

%description opencv
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-opencv) contains the OpenCV plugins.
%endif


%if %{with openh264}
%package -n gstreamer1-plugin-openh264
Summary:        GStreamer OpenH264 plugin
License:        LGPL-2.0-or-later AND BSD-2-Clause
# Prefer actual openh264 library over the noopenh264 stub
Suggests:       openh264%{_isa}

%description -n gstreamer1-plugin-openh264
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the OpenH264 plugin.
%endif


%package libs
Summary:        Runtime libraries for the GStreamer media framework "bad" plug-ins
Requires:       openal-soft%{?_isa}
Requires:       librsvg2%{?_isa}
Requires:       liblc3%{?_isa}
Requires:       libnice%{?_isa}
%if %{with aom}
Requires:       libaom%{?_isa}
%endif
%if %{with extras}
Requires:       faad2%{?_isa}
%endif
%if %{with vpl}
Requires:       libvpl%{?_isa}
%endif
%if %{with webrtc}
%if %{with webrtc1}
Requires:       webrtc-audio-processing1%{?_isa}
%else
Requires:       webrtc-audio-processing%{?_isa}
%endif
%endif

%description libs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the runtime libraries for plugins that
aren't tested well enough, or the code is not of good enough quality.


%package devel
Summary:        Development files for the GStreamer media framework "bad" plug-ins
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gstreamer1-plugins-base-devel

%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins that
aren't tested well enough, or the code is not of good enough quality.


%prep
%oreon_verify_sources
%autosetup -n gst-plugins-bad-%{version} -p3

%build
%meson \
    -D package-name="Fedora GStreamer-plugins-bad package" \
    -D package-origin="http://download.fedoraproject.org" \
    -D gpl=enabled \
    -D doc=disabled \
    -D tests=disabled \
%if %{without aom}
    -D aom=disabled \
%endif
%if %{without dc1394}
    -D dc1394=disabled \
%endif
%if %{without ldac}
    -D ldac=disabled \
%endif
%if %{without onnx}
    -D onnx=disabled \
%endif
%if %{without opencv}
    -D opencv=disabled \
%endif
%if %{without openh264}
    -D openh264=disabled \
%endif
%if %{without svtav1}
    -D svtav1=disabled \
%endif
%if %{without vpl}
    -D msdk=disabled \
    -D qsv=disabled \
%endif
%if %{without webrtc1}
    -D isac=disabled \
%endif
%if %{without webrtc}
    -D webrtcdsp=disabled \
%endif
%if %{without extras}
    -D assrender=disabled \
    -D avtp=disabled \
    -D bs2b=disabled \
    -D chromaprint=disabled \
    -D curl=disabled -D curl-ssh2=disabled \
    -D d3dvideosink=disabled \
    -D decklink=disabled \
    -D directsound=disabled \
    -D dts=disabled \
    -D faad=disabled \
    -D fbdev=disabled \
    -D flite=disabled \
    -D fluidsynth=disabled \
    -D gme=disabled \
    -D ladspa=disabled \
    -D ldac=disabled \
    -D lv2=disabled \
    -D microdns=disabled \
    -D modplug=disabled \
    -D mpeg2enc=disabled \
    -D mplex=disabled \
    -D musepack=disabled \
    -D openal=disabled \
    -D openexr=disabled \
    -D openmpt=disabled \
    -D qroverlay=disabled \
    -D spandsp=disabled \
    -D srt=disabled \
    -D teletext=disabled \
    -D ttml=disabled \
    -D voamrwbenc=disabled \
    -D webrtc=disabled \
    -D wildmidi=disabled \
    -D zbar=disabled \
    -D zxing=disabled \
%endif
    -D aja=disabled \
    -D androidmedia=disabled \
    -D amfcodec=disabled \
    -D cuda-nvmm=disabled \
    -D directfb=disabled \
    -D directshow=disabled \
    -D faac=disabled \
    -D gs=disabled \
    -D iqa=disabled \
    -D lcevcdecoder=disabled \
    -D lcevcencoder=disabled \
    -D libde265=disabled \
    -D magicleap=disabled \
    -D neon=disabled \
    -D nvcomp=disabled \
    -D nvdswrapper=disabled \
    -D openaptx=disabled \
    -D openni2=disabled \
    -D opensles=disabled \
    -D qt6d3d11=disabled \
    -D rtmp=disabled \
    -D svthevcenc=disabled \
    -D svtjpegxs=disabled \
    -D tinyalsa=disabled \
    -D voaacenc=disabled \
    -D wasapi=disabled -D wasapi2=disabled \
    -D wpe=disabled \
    -D x11=disabled \
    -D x265=disabled \
    %{nil}

%meson_build

%install
%meson_install

%if %{with opencv}
# no pkgconfig file or GIR, nothing aside from the plugin uses the library
rm -f $RPM_BUILD_ROOT%{_includedir}/gstreamer-%{majorminor}/gst/opencv/*
rm -f $RPM_BUILD_ROOT%{_libdir}/libgstopencv-%{majorminor}.so
%endif

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/gstreamer-bad-free.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 Richard Hughes <richard@hughsie.com> -->
<component type="codec">
  <id>gstreamer-bad-free</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - Extra</name>
  <summary>Multimedia playback for AIFF, DVB, GSM, MIDI, MXF and Opus</summary>
  <description>
    <p>
      This addon includes several additional codecs that are missing
      something - perhaps a good code review, some documentation, a set of
      tests, a real live maintainer, or some actual wide use.
      However, they might be good enough to play your media files.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <keywords>
    <keyword>AIFF</keyword>
    <keyword>DVB</keyword>
    <keyword>GSM</keyword>
    <keyword>MIDI</keyword>
    <keyword>MXF</keyword>
    <keyword>Opus</keyword>
  </keywords>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%if %{with openh264}
cat > $RPM_BUILD_ROOT%{_metainfodir}/gstreamer-openh264.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2015 Kalev Lember <klember@redhat.com> -->
<component type="codec">
  <id>gstreamer-openh264</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - H.264</name>
  <summary>Multimedia playback for H.264</summary>
  <description>
    <p>
      This addon includes a codec for H.264 playback and encoding.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
%endif

%find_lang gst-plugins-bad-%{majorminor}

%ldconfig_scriptlets

%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING
%doc README.md README.static-linking RELEASE

%{_metainfodir}/gstreamer-bad-free.metainfo.xml
%{_bindir}/gst-transcoder-%{majorminor}

# presets
%dir %{_datadir}/gstreamer-%{majorminor}/
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstFreeverb.prs
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/device/
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/device/dvd.gep
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/avi.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/flv.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/mkv.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/mp3.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/mp4.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/oga.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/ogv.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/ts.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/webm.gep
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/online-services/
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/online-services/youtube.gep

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiolatency.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixmatrix.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstcodecalpha.so
%{_libdir}/gstreamer-%{majorminor}/libgstcodectimestamper.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstdash.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{majorminor}/libgstlegacyrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%{_libdir}/gstreamer-%{majorminor}/libgstipcpipeline.so
%{_libdir}/gstreamer-%{majorminor}/libgstinter.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstivfparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstivtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstproxy.so
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrist.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp2.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanagerbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstswitchbin.so
%{_libdir}/gstreamer-%{majorminor}/libgsttensordecoders.so
%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so
%{_libdir}/gstreamer-%{majorminor}/libgsttranscode.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
%{_libdir}/gstreamer-%{majorminor}/libgstinsertbin.so
%{_libdir}/gstreamer-%{majorminor}/libgstmse.so
%{_libdir}/gstreamer-%{majorminor}/libgstunixfd.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so

# System (Linux) specific plugins
%{_libdir}/gstreamer-%{majorminor}/libgstbluez.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%endif
%if %{with vpl}
%{_libdir}/gstreamer-%{majorminor}/libgstmsdk.so
%{_libdir}/gstreamer-%{majorminor}/libgstqsv.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvcgadget.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
%{_libdir}/gstreamer-%{majorminor}/libgstv4l2codecs.so

# Plugins with external dependencies

%{_libdir}/gstreamer-%{majorminor}/libgstaes.so
%{_libdir}/gstreamer-%{majorminor}/libgstanalyticsoverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstclosedcaption.so
%{_libdir}/gstreamer-%{majorminor}/libgstcodec2json.so
%{_libdir}/gstreamer-%{majorminor}/libgstcolormanagement.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
%{_libdir}/gstreamer-%{majorminor}/libgstfdkaac.so
%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstgtkwayland.so
%{_libdir}/gstreamer-%{majorminor}/libgstkms.so
%{_libdir}/gstreamer-%{majorminor}/libgstlc3.so
%{_libdir}/gstreamer-%{majorminor}/libgstnvcodec.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstsbc.so
%{_libdir}/gstreamer-%{majorminor}/libgstsctp.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstva.so
%{_libdir}/gstreamer-%{majorminor}/libgstvulkan.so
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebp.so
%if %{with aom}
%{_libdir}/gstreamer-%{majorminor}/libgstaom.so
%endif
%if %{with svtav1}
%{_libdir}/gstreamer-%{majorminor}/libgstsvtav1.so
%endif
%if %{with webrtc1}
%{_libdir}/gstreamer-%{majorminor}/libgstisac.so
%endif
%if %{with webrtc}
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtcdsp.so
%endif
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtc.so
%endif

#debugging plugin
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so


%if %{with extras}
%files extras
# presets
%{_datadir}/gstreamer-%{majorminor}/presets/GstVoAmrwbEnc.prs

# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so
%{_libdir}/gstreamer-%{majorminor}/libgstavtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstbs2b.so
%{_libdir}/gstreamer-%{majorminor}/libgstchromaprint.so
%if %{with dc1394}
%{_libdir}/gstreamer-%{majorminor}/libgstdc1394.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstflite.so
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%if %{with ldac}
%{_libdir}/gstreamer-%{majorminor}/libgstldac.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstmicrodns.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%if %{with onnx}
%{_libdir}/gstreamer-%{majorminor}/libgstonnx.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenmpt.so
%{_libdir}/gstreamer-%{majorminor}/libgstqroverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstspandsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrt.so
%{_libdir}/gstreamer-%{majorminor}/libgstteletext.so
%{_libdir}/gstreamer-%{majorminor}/libgstvoamrwbenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstzxing.so

%files lv2
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstlv2.so

%files zbar
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstzbar.so

%files fluidsynth
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstfluidsynthmidi.so

%files wildmidi
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so
%endif

%if %{with opencv}
%files opencv
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/libgstopencv-%{majorminor}.so.0{,.*}
%endif

%if %{with openh264}
%files -n gstreamer1-plugin-openh264
%license COPYING
%license ext/openh264/LICENSE
%{_metainfodir}/gstreamer-openh264.metainfo.xml
%{_libdir}/gstreamer-1.0/libgstopenh264.so
%endif

%files libs
%license COPYING
%{_libdir}/libgstanalytics-%{majorminor}.so.0{,.*}
%{_libdir}/libgstadaptivedemux-%{majorminor}.so.0{,.*}
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.0{,.*}
%{_libdir}/libgstbadaudio-%{majorminor}.so.0{,.*}
%{_libdir}/libgstcodecparsers-%{majorminor}.so.0{,.*}
%{_libdir}/libgstcodecs-%{majorminor}.so.0{,.*}
%{_libdir}/libgstcuda-%{majorminor}.so.0{,.*}
%{_libdir}/libgstdxva-%{majorminor}.so.0{,.*}
%{_libdir}/libgstinsertbin-%{majorminor}.so.0{,.*}
%{_libdir}/libgstisoff-%{majorminor}.so.0{,.*}
%{_libdir}/libgstmpegts-%{majorminor}.so.0{,.*}
%{_libdir}/libgstmse-%{majorminor}.so.0{,.*}
%{_libdir}/libgstplay-%{majorminor}.so.0{,.*}
%{_libdir}/libgstplayer-%{majorminor}.so.0{,.*}
%{_libdir}/libgstphotography-%{majorminor}.so.0{,.*}
%{_libdir}/libgstsctp-%{majorminor}.so.0{,.*}
%{_libdir}/libgsttranscoder-%{majorminor}.so.0{,.*}
%{_libdir}/libgsturidownloader-%{majorminor}.so.0{,.*}
%{_libdir}/libgstvulkan-%{majorminor}.so.0{,.*}
%{_libdir}/libgstva-%{majorminor}.so.0{,.*}
%{_libdir}/libgstwebrtc-%{majorminor}.so.0{,.*}
%if %{with extras}
%{_libdir}/libgstwebrtcnice-%{majorminor}.so.0{,.*}
%endif
%{_libdir}/libgstwayland-%{majorminor}.so.0{,.*}

# libgstcodecparsers remains; GstCodecParsers-*.typelib/.gir not built since upstream dropped GI there (1.26+)
%{_libdir}/girepository-1.0/CudaGst-1.0.typelib
%{_libdir}/girepository-1.0/GstAnalytics-1.0.typelib
%{_libdir}/girepository-1.0/GstBadAudio-1.0.typelib
%{_libdir}/girepository-1.0/GstCodecs-1.0.typelib
%{_libdir}/girepository-1.0/GstCuda-1.0.typelib
%{_libdir}/girepository-1.0/GstDxva-1.0.typelib
%{_libdir}/girepository-1.0/GstInsertBin-1.0.typelib
%{_libdir}/girepository-1.0/GstMpegts-1.0.typelib
%{_libdir}/girepository-1.0/GstMse-1.0.typelib
%{_libdir}/girepository-1.0/GstPlay-1.0.typelib
%{_libdir}/girepository-1.0/GstPlayer-1.0.typelib
%{_libdir}/girepository-1.0/GstTranscoder-1.0.typelib
%{_libdir}/girepository-1.0/GstVa-1.0.typelib
%{_libdir}/girepository-1.0/GstVulkan-1.0.typelib
%{_libdir}/girepository-1.0/GstVulkanWayland-1.0.typelib
%{_libdir}/girepository-1.0/GstWebRTC-1.0.typelib

%files devel
%if 0
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-plugins-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-libs-%{majorminor}
%endif

%{_datadir}/gir-1.0/CudaGst-%{majorminor}.gir
%{_datadir}/gir-1.0/GstAnalytics-%{majorminor}.gir
%{_datadir}/gir-1.0/GstBadAudio-%{majorminor}.gir
%{_datadir}/gir-1.0/GstCodecs-%{majorminor}.gir
%{_datadir}/gir-1.0/GstCuda-%{majorminor}.gir
%{_datadir}/gir-1.0/GstDxva-%{majorminor}.gir
%{_datadir}/gir-1.0/GstInsertBin-%{majorminor}.gir
%{_datadir}/gir-1.0/GstMpegts-%{majorminor}.gir
%{_datadir}/gir-1.0/GstMse-%{majorminor}.gir
%{_datadir}/gir-1.0/GstPlay-%{majorminor}.gir
%{_datadir}/gir-1.0/GstPlayer-%{majorminor}.gir
%{_datadir}/gir-1.0/GstTranscoder-%{majorminor}.gir
%{_datadir}/gir-1.0/GstVa-%{majorminor}.gir
%{_datadir}/gir-1.0/GstVulkan-%{majorminor}.gir
%{_datadir}/gir-1.0/GstVulkanWayland-%{majorminor}.gir
%{_datadir}/gir-1.0/GstWebRTC-%{majorminor}.gir

%{_libdir}/libgstanalytics-%{majorminor}.so
%{_libdir}/libgstadaptivedemux-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
%{_libdir}/libgstbadaudio-%{majorminor}.so
%{_libdir}/libgstcuda-%{majorminor}.so
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstcodecs-%{majorminor}.so
%{_libdir}/libgstdxva-%{majorminor}.so
%{_libdir}/libgstinsertbin-%{majorminor}.so
%{_libdir}/libgstisoff-%{majorminor}.so
%{_libdir}/libgstmpegts-%{majorminor}.so
%{_libdir}/libgstmse-%{majorminor}.so
%{_libdir}/libgstplay-%{majorminor}.so
%{_libdir}/libgstplayer-%{majorminor}.so
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgstsctp-%{majorminor}.so
%{_libdir}/libgsttranscoder-%{majorminor}.so
%{_libdir}/libgsturidownloader-%{majorminor}.so
%{_libdir}/libgstvulkan-%{majorminor}.so
%{_libdir}/libgstva-%{majorminor}.so
%{_libdir}/libgstwebrtc-%{majorminor}.so
%if %{with extras}
%{_libdir}/libgstwebrtcnice-%{majorminor}.so
%endif
%{_libdir}/libgstwayland-%{majorminor}.so

%{_includedir}/gstreamer-%{majorminor}/gst/audio
%{_includedir}/gstreamer-%{majorminor}/gst/analytics
%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc
%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers
%{_includedir}/gstreamer-%{majorminor}/gst/cuda/
%{_includedir}/gstreamer-%{majorminor}/gst/insertbin
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{majorminor}/gst/isoff/
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts
%{_includedir}/gstreamer-%{majorminor}/gst/mse/
%{_includedir}/gstreamer-%{majorminor}/gst/play
%{_includedir}/gstreamer-%{majorminor}/gst/player
%{_includedir}/gstreamer-%{majorminor}/gst/sctp
%{_includedir}/gstreamer-%{majorminor}/gst/transcoder
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader
%{_includedir}/gstreamer-%{majorminor}/gst/va/
%{_includedir}/gstreamer-%{majorminor}/gst/vulkan/
%{_includedir}/gstreamer-%{majorminor}/gst/wayland/
%{_includedir}/gstreamer-%{majorminor}/gst/webrtc/

# pkg-config files
%{_libdir}/pkgconfig/gstreamer-analytics-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-bad-audio-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-cuda-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mse-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-photography-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-play-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-player-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-sctp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-transcoder-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-va-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-wayland-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-wayland-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-webrtc-%{majorminor}.pc
%if %{with extras}
%{_libdir}/pkgconfig/gstreamer-webrtc-nice-%{majorminor}.pc
%endif


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.1-2
- Remove commented git snapshot lines that expanded macros in comments

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.1-1
- Prepare for Oreon 11 (RP1)
