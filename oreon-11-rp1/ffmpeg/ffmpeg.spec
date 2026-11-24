# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8c3850283eb25fa026482078a04051e0be17347b09ef81a0849bec15a96e002e
%global source1_hash d617fd94ea354dadd2a8bb16243d37c44e1e9729b06b6ad58fe30bfb0fa943f2
%global source2_hash fd543a75d3bba61b759ca25b135e6f91b34aa37ae6987316e5c636bf3c78ae8d
%global source20_hash 84ee7d0501f5c9d501f9518f5f9d2458f529ae519b51df0bd9751c66dfaa03b6
%global source21_hash ad0d40f82a257aac9c00a49154a566b6773ef5fdfe580d59b6b0b0192aadf858
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond all_codecs 0

%if 0%{?oreon}
%bcond bootstrap 0
%else
%bcond bootstrap 0
%endif

%global pkg_suffix -free

%bcond freeworld_lavc 0

%if %{with freeworld_lavc}
%global with_all_codecs 1
%global pkg_suffix %{nil}
%global basepkg_suffix -free
%endif

%ifarch %{ix86} %{arm}
%bcond lto 0
%global _pkg_extra_ldflags "-Wl,-z,notext"
%else
%bcond lto 1
%endif

%if 0%{?oreon}
%bcond vpl 0
%ifarch x86_64
%bcond vmaf 1
%else
%bcond vmaf 0
%endif
%else
%ifarch x86_64
%bcond vpl 1
%bcond vmaf 1
%else
%bcond vpl 0
%bcond vmaf 0
%endif
%endif

%ifarch s390 s390x riscv64
%bcond dc1394 0
%bcond ffnvcodec 0
%else
%bcond dc1394 1
%bcond ffnvcodec 1
%endif

%if 0%{?rhel}
%bcond chromaprint 0
%bcond flite 0
%else
%bcond chromaprint %{?with_bootstrap:0}%{!?with_bootstrap:1}
%bcond flite 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 9
%bcond lcms2 0
%bcond placebo 0
%else
%bcond lcms2 1
%bcond placebo 1
%endif

%bcond evc_main 0

%if %{with all_codecs}
%bcond rtmp 1
%bcond vvc 1
%bcond x264 1
%bcond x265 1
%else
%bcond rtmp 0
%bcond vvc 0
%bcond x264 0
%bcond x265 0
%endif

%if %{without lto}
%global _lto_cflags %{nil}
%endif

%global build_type_safety_c 2

%global av_codec_soversion 63
%global av_device_soversion 63
%global av_filter_soversion 12
%global av_format_soversion 63
%global av_util_soversion 61
%global swresample_soversion 7
%global swscale_soversion 10

Name:           ffmpeg
%global pkg_name %{name}%{?pkg_suffix}

Version:        9.0.2
Release:        1%{?dist}
Summary:        A complete solution to record, convert and stream audio and video
License:        GPL-3.0-or-later
URL:            https://ffmpeg.org/
Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz
Source1:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz.asc
Source2:        ffmpeg.keyring
Source20:       enable_decoders
Source21:       enable_encoders

Patch1:         ffmpeg-codec-choice.patch
Patch2:         ffmpeg-allow-fdk-aac-free.patch
Patch3:         ffmpeg-allow-decklink.patch
Patch4:         ffmpeg-vapoursynth-lib-rename.patch
Patch5:         https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/883e8a6336b2651f7be79a6a9aa5f3cc22937948.patch#/ffmpeg-openh264-flush-callback.patch
Patch6:         https://code.ffmpeg.org/FFmpeg/FFmpeg/pulls/24968.patch#/ffmpeg-fix-streamcopy-pts.patch
Patch7:         https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/a7502e5ff39ef53d475b9ee7dd6d4aeb48f047e6.patch#/ffmpeg-openapv1.1.patch

Patch1002:      ffmpeg-chromium.patch

Requires:       libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavdevice%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavfilter%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libswscale%{?pkg_suffix}%{_isa} = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  AMF-devel
BuildRequires:  decklink-static
BuildRequires:  fdk-aac-free-devel
%if %{with flite}
BuildRequires:  flite-devel >= 2.2
%endif
BuildRequires:  game-music-emu-devel
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  glslc
BuildRequires:  gsm-devel
BuildRequires:  ladspa-devel
BuildRequires:  lame-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libklvanc-devel
BuildRequires:  libmysofa-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  perl(Pod::Man)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(aribb24) >= 1.0.3
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
%if 0%{?fedora} > 44
BuildRequires:  nv-codec-headers13.0
%else
BuildRequires:  pkgconfig(ffnvcodec)
%endif
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(frei0r)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libilbc)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lc3) >= 1.1.0
%if %{with lcms2}
BuildRequires:  pkgconfig(lcms2) >= 2.13
%endif
BuildRequires:  pkgconfig(libaribcaption) >= 1.1.1
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
%if %{with chromaprint}
BuildRequires:  pkgconfig(libchromaprint)
%endif
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libjxl) >= 0.7.0
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libopenmpt)
%if %{with placebo}
BuildRequires:  pkgconfig(libplacebo) >= 4.192.0
%endif
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(librabbitmq)
BuildRequires:  pkgconfig(librist)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(oapv)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opencore-amrnb)
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(srt)
BuildRequires:  pkgconfig(SvtAv1Enc) >= 0.9.0
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vapoursynth) >= 79
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vidstab)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vo-amrwbenc)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(vulkan) >= 1.3.255
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2)
BuildRequires:  texinfo
BuildRequires:  xvidcore-devel

%if %{with dc1394}
BuildRequires:  pkgconfig(libavc1394)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libiec61883)
%endif
%if %{with rtmp}
BuildRequires:  librtmp-devel
%endif
%if %{with vpl}
BuildRequires:  pkgconfig(vpl) >= 2.6
%endif
%if %{with evc_main}
BuildRequires:  pkgconfig(xevd)
BuildRequires:  pkgconfig(xeve)
%else
BuildRequires:  pkgconfig(xevdb)
BuildRequires:  pkgconfig(xeveb)
%endif
%if %{with x264}
BuildRequires:  pkgconfig(x264)
%endif
%if %{with x265}
BuildRequires:  pkgconfig(x265)
%endif
%if %{with vmaf}
BuildRequires:  pkgconfig(libvmaf)
%endif

%description
FFmpeg is a leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created. It supports the most obscure ancient formats up to the
cutting edge. No matter if they were designed by some standards committee, the
community or a corporation.

%if %{without all_codecs}
This build of ffmpeg is limited in the number of codecs supported.
%endif

%dnl --------------------------------------------------------------------------------

%if ! %{with freeworld_lavc}

%if "x%{?pkg_suffix}" != "x"
%package -n     %{pkg_name}
Summary:        A complete solution to record, convert and stream audio and video
Requires:       libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavdevice%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavfilter%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libswscale%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n %{pkg_name}
FFmpeg is a leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created. It supports the most obscure ancient formats up to the
cutting edge. No matter if they were designed by some standards committee, the
community or a corporation.

%if %{without all_codecs}
This build of ffmpeg is limited in the number of codecs supported.
%endif

%endif

%files -n %{pkg_name}
%doc CREDITS README.md
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_mandir}/man1/ff*.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ffprobe.xsd
%{_datadir}/%{name}/libvpx-*.ffpreset

%dnl --------------------------------------------------------------------------------

%package -n     %{pkg_name}-devel
Summary:        Development package for %{name}
Requires:       libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavdevice%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavfilter%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswscale%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       pkgconfig

%description -n %{pkg_name}-devel
FFmpeg is a leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created. It supports the most obscure ancient formats up to the
cutting edge. No matter if they were designed by some standards committee, the
community or a corporation.

%files -n %{pkg_name}-devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%doc _doc/examples

%dnl --------------------------------------------------------------------------------

%package -n libavcodec%{?pkg_suffix}
Summary:        FFmpeg codec library
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Suggests:       openh264%{_isa}
Conflicts:      libavcodec-freeworld%{_isa} < %{version}

%description -n libavcodec%{?pkg_suffix}
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.

%if %{without all_codecs}
This build of ffmpeg is limited in the number of codecs supported.
%endif

%files -n libavcodec%{?pkg_suffix}
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavcodec.so.%{av_codec_soversion}{,.*}

%dnl --------------------------------------------------------------------------------

%package -n libavcodec%{?pkg_suffix}-devel
Summary:        Development files for FFmpeg's codec library
Requires:       libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libavcodec%{?pkg_suffix}-devel
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.

This subpackage contains the headers for FFmpeg libavcodec.

%files -n libavcodec%{?pkg_suffix}-devel
%{_includedir}/%{name}/libavcodec
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/libavcodec.so
%{_mandir}/man3/libavcodec.3*

%dnl --------------------------------------------------------------------------------

%package -n libavdevice%{?pkg_suffix}
Summary:        FFmpeg device library
Requires:       libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavfilter%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libavdevice%{?pkg_suffix}
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

%files -n libavdevice%{?pkg_suffix}
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavdevice.so.%{av_device_soversion}{,.*}

%dnl --------------------------------------------------------------------------------

%package -n libavdevice%{?pkg_suffix}-devel
Summary:        Development files for FFmpeg's device library
Requires:       libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavfilter%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswscale%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavdevice%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libavdevice%{?pkg_suffix}-devel
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

This subpackage contains the headers for FFmpeg libavdevice.

%files -n libavdevice%{?pkg_suffix}-devel
%{_includedir}/%{name}/libavdevice
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/libavdevice.so
%{_mandir}/man3/libavdevice.3*

%dnl --------------------------------------------------------------------------------

%package -n libavfilter%{?pkg_suffix}
Summary:        FFmpeg audio and video filtering library
Requires:       libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libswscale%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libavfilter%{?pkg_suffix}
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

%files -n libavfilter%{?pkg_suffix}
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavfilter.so.%{av_filter_soversion}{,.*}

%dnl --------------------------------------------------------------------------------

%package -n libavfilter%{?pkg_suffix}-devel
Summary:        Development files for FFmpeg's audio/video filter library
Requires:       libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswscale%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavfilter%{?pkg_suffix} = %{version}-%{release}
Requires:       pkgconfig

%description -n libavfilter%{?pkg_suffix}-devel
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

This subpackage contains the headers for FFmpeg libavfilter.

%files -n libavfilter%{?pkg_suffix}-devel
%{_includedir}/%{name}/libavfilter
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/libavfilter.so
%{_mandir}/man3/libavfilter.3*

%dnl --------------------------------------------------------------------------------

%package -n libavformat%{?pkg_suffix}
Summary:        FFmpeg's stream format library
Requires:       libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libavformat%{?pkg_suffix}
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.

%if %{without all_codecs}
This build of ffmpeg is limited in the number of codecs supported.
%endif

%files -n libavformat%{?pkg_suffix}
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavformat.so.%{av_format_soversion}{,.*}

%dnl --------------------------------------------------------------------------------

%package -n libavformat%{?pkg_suffix}-devel
Summary:        Development files for FFmpeg's stream format library
Requires:       libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libavformat%{?pkg_suffix}-devel
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.

This subpackage contains the headers for FFmpeg libavformat.

%files -n libavformat%{?pkg_suffix}-devel
%{_includedir}/%{name}/libavformat
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/libavformat.so
%{_mandir}/man3/libavformat.3*

%dnl --------------------------------------------------------------------------------

%package -n libavutil%{?pkg_suffix}
Summary:        FFmpeg's utility library
Group:          System/Libraries
Obsoletes:      libpostproc%{?pkg_suffix} < 8.0

%description -n libavutil%{?pkg_suffix}
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

%files -n libavutil%{?pkg_suffix}
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavutil.so.%{av_util_soversion}{,.*}

%dnl --------------------------------------------------------------------------------

%package -n libavutil%{?pkg_suffix}-devel
Summary:        Development files for FFmpeg's utility library
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:       pkgconfig
Obsoletes:      libpostproc%{?pkg_suffix}-devel < 8.0

%description -n libavutil%{?pkg_suffix}-devel
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

This subpackage contains the headers for FFmpeg libavutil.

%files -n libavutil%{?pkg_suffix}-devel
%{_includedir}/%{name}/libavutil
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/libavutil.so
%{_mandir}/man3/libavutil.3*

%dnl --------------------------------------------------------------------------------

%package -n libswresample%{?pkg_suffix}
Summary:        FFmpeg software resampling library
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libswresample%{?pkg_suffix}
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

%files -n libswresample%{?pkg_suffix}
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libswresample.so.%{swresample_soversion}{,.*}

%dnl --------------------------------------------------------------------------------

%package -n libswresample%{?pkg_suffix}-devel
Summary:        Development files for the FFmpeg software resampling library
Requires:       libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libswresample%{?pkg_suffix}-devel
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

This subpackage contains the headers for FFmpeg libswresample.

%files -n libswresample%{?pkg_suffix}-devel
%{_includedir}/%{name}/libswresample
%{_libdir}/pkgconfig/libswresample.pc
%{_libdir}/libswresample.so
%{_mandir}/man3/libswresample.3*

%dnl --------------------------------------------------------------------------------

%package -n libswscale%{?pkg_suffix}
Summary:        FFmpeg image scaling and colorspace/pixel conversion library
Requires:       libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libswscale%{?pkg_suffix}
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

%files -n libswscale%{?pkg_suffix}
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libswscale.so.%{swscale_soversion}{,.*}

%dnl --------------------------------------------------------------------------------

%package -n libswscale%{?pkg_suffix}-devel
Summary:        Development files for FFmpeg's image scaling and colorspace library
Provides:       libswscale%{?pkg_suffix}-devel = %{version}-%{release}
Conflicts:      libswscale%{?pkg_suffix}-devel < %{version}-%{release}
Requires:       libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:       libswscale%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libswscale%{?pkg_suffix}-devel
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

This subpackage contains the headers for FFmpeg libswscale.

%files -n libswscale%{?pkg_suffix}-devel
%{_includedir}/%{name}/libswscale
%{_libdir}/pkgconfig/libswscale.pc
%{_libdir}/libswscale.so
%{_mandir}/man3/libswscale.3*

%endif

%dnl --------------------------------------------------------------------------------

%if %{with freeworld_lavc}
%package -n libavcodec-freeworld
Summary:        FFmpeg codec library - freeworld overlay
Requires:       libavutil%{?basepkg_suffix}%{_isa} >= %{version}-%{release}
Requires:       libswresample%{?basepkg_suffix}%{_isa} >= %{version}-%{release}
Supplements:    libavcodec%{?basepkg_suffix}%{_isa} >= %{version}-%{release}
Requires:       openh264%{_isa}
Conflicts:      libavcodec-free%{_isa} < %{version}

%description -n libavcodec-freeworld
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.

This build includes the full range of codecs offered by ffmpeg.

%files -n libavcodec-freeworld
%{_sysconfdir}/ld.so.conf.d/%{name}-%{_lib}.conf
%{_libdir}/%{name}/libavcodec.so.%{av_codec_soversion}{,.*}

%{!?ldconfig:%global ldconfig /sbin/ldconfig}
%ldconfig_scriptlets -n libavcodec-freeworld

%endif

%dnl --------------------------------------------------------------------------------

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source20_hash}  %{SOURCE20}' | sha256sum -c -
echo '%{source21_hash}  %{SOURCE21}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -S git_am
install -m 0644 %{SOURCE20} enable_decoders
install -m 0644 %{SOURCE21} enable_encoders
sed -i "s|check_host_cflags -O3|check_host_cflags %{optflags}|" configure
install -m0755 -d _doc/examples
cp -a doc/examples/{*.c,Makefile,README} _doc/examples/

%conf
%set_build_flags

./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --docdir=%{_docdir}/%{name} \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --arch=%{_target_cpu} \
    --optflags="%{build_cflags}" \
    --extra-cflags="-I%{_includedir}/decklink" \
    --extra-cxxflags="-I%{_includedir}/decklink" \
    --extra-ldflags="%{build_ldflags}" \
    --disable-htmlpages \
    --disable-static \
    --disable-stripping \
    --enable-pic \
    --enable-shared \
    --enable-gpl \
    --enable-version3 \
    --enable-amf \
    --enable-avcodec \
    --enable-avdevice \
    --enable-avfilter \
    --enable-avformat \
    --enable-alsa \
    --enable-bzlib \
%if %{with chromaprint}
    --enable-chromaprint \
%else
    --disable-chromaprint \
%endif
    --disable-cuda-nvcc \
%if %{with ffnvcodec}
    --enable-cuvid \
%endif
    --enable-decklink \
    --enable-frei0r \
    --enable-gcrypt \
    --enable-gmp \
    --enable-gnutls \
    --enable-gray \
    --enable-iconv \
    --enable-ladspa \
%if %{with lcms2}
    --enable-lcms2 \
%endif
    --enable-libaom \
    --enable-libaribb24 \
    --enable-libaribcaption \
    --enable-libass \
    --enable-libbluray \
    --enable-libbs2b \
    --enable-libcaca \
    --enable-libcdio \
    --enable-libcodec2 \
    --enable-libdav1d \
    --disable-libdavs2 \
%if %{with dc1394}
    --enable-libdc1394 \
%endif
    --enable-libdvdnav \
    --enable-libdvdread \
    --enable-libfdk-aac \
%if %{with flite}
    --enable-libflite \
%endif
    --enable-libfontconfig \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgme \
    --enable-libharfbuzz \
    --enable-libgsm \
%if %{with dc1394}
    --enable-libiec61883 \
%endif
    --enable-libilbc \
    --enable-libjack \
    --enable-libjxl \
    --enable-libklvanc \
    --disable-liblensfun \
    --disable-liblcevc-dec \
    --enable-liblc3 \
    --enable-libmodplug \
    --enable-libmp3lame \
    --enable-libmysofa \
    --disable-libnpp \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --disable-libopencv \
    --enable-liboapv \
    --enable-libopenh264 \
    --enable-libopenjpeg \
    --enable-libopenmpt \
    --enable-libopus \
%if %{with placebo}
    --enable-libplacebo \
%endif
    --enable-libpulse \
    --enable-libqrencode \
    --disable-libquirc \
    --enable-librabbitmq \
    --enable-librav1e \
    --enable-librist \
    --enable-librsvg \
%if %{with librtmp}
    --enable-librtmp \
%endif
    --enable-librubberband \
    --disable-libshine \
    --enable-libsmbclient \
    --enable-libsnappy \
    --enable-libsvtav1 \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libsrt \
    --enable-libssh \
    --disable-libtensorflow \
    --enable-libtesseract \
    --enable-libtheora \
    --disable-libtorch \
    --disable-libuavs3d \
    --enable-libtwolame \
    --enable-libv4l2 \
    --enable-libvidstab \
%if %{with vmaf}
    --enable-libvmaf \
%endif
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
%if %{with vpl}
    --enable-libvpl \
%endif
    --enable-libvpx \
    --enable-libwebp \
%if %{with x264}
    --enable-libx264 \
%endif
%if %{with x265}
    --enable-libx265 \
%endif
    --disable-libxavs2 \
    --disable-libxavs \
    --enable-libxcb \
    --enable-libxcb-shape \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
%if %{with evc_main}
    --enable-libxeve \
    --enable-libxevd \
%else
    --enable-libxeveb \
    --enable-libxevdb \
%endif
    --enable-libxml2 \
    --enable-libxvid \
    --enable-libzimg \
    --enable-libzmq \
    --enable-libzvbi \
%if %{with lto}
    --enable-lto \
%endif
    --enable-lv2 \
    --enable-lzma \
    --enable-manpages \
%if %{with ffnvcodec}
    --enable-nvdec \
    --enable-nvenc \
%endif
    --enable-openal \
    --disable-openssl \
    --enable-pthreads \
    --enable-sdl2 \
    --enable-shared \
    --enable-swresample \
    --enable-swscale \
    --enable-v4l2-m2m \
    --enable-vaapi \
    --enable-vapoursynth \
    --enable-vdpau \
    --enable-vulkan \
    --enable-xlib \
    --enable-zlib \
%if %{without all_codecs}
    --enable-muxers \
    --enable-demuxers \
    --enable-hwaccels \
    --disable-encoders \
    --disable-decoders \
    --disable-decoder="h264,hevc,vc1,vvc" \
    --enable-encoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <enable_encoders)" \
    --enable-decoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <enable_decoders)" \
%endif
%ifarch %{power64}
%ifarch ppc64
    --cpu=g5 \
%endif
%ifarch ppc64p7
    --cpu=power7 \
%endif
%ifarch ppc64le
    --cpu=power8 \
%endif
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%endif
%ifarch armv7hl armv7hnl
    --cpu=armv7-a \
    --enable-vfpv3 \
    --enable-thumb \
%endif
%ifarch armv7hl
    --disable-neon \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%endif
    || cat ffbuild/config.log

cat config.h
cat config_components.h

%if %{without all_codecs}
for i in H264 HEVC HEVC_RKMPP VC1 VVC; do
    grep -q "#define CONFIG_${i}_DECODER 0" config_components.h
done

for i in LIBX264 LIBX264RGB LIBX265; do
    grep -q "#define CONFIG_${i}_ENCODER 0" config_components.h
done
for i in H264 HEVC; do
    for j in MF VIDEOTOOLBOX; do
        grep -q "#define CONFIG_${i}_${j}_ENCODER 0" config_components.h
    done
done
%endif

%build
%set_build_flags

%make_build V=1
%make_build documentation V=1
%make_build alltools V=1

%install
%make_install V=1

rm -rf %{buildroot}%{_datadir}/%{name}/examples

%if %{with freeworld_lavc}
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
mkdir -p %{buildroot}%{_libdir}/%{name}
echo -e "%{_libdir}/%{name}\n" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_lib}.conf
cp -pa %{buildroot}%{_libdir}/libavcodec.so.%{av_codec_soversion}{,.*} %{buildroot}%{_libdir}/%{name}
rm -f %{buildroot}%{_libdir}/*.*
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_datadir}
%endif

%changelog
%autochangelog
