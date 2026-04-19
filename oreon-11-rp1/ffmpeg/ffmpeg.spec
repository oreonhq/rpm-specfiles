# Red Hat %%optflags default -flto breaks final link of libavcodec/libswscale .so
# (R_X86_64_PC32 against undefined symbol e.g. pd_1 in .ltrans object).
%global _lto_cflags %{nil}

# Match Fedora dist-git layout (ffmpeg-free / libav*-free) for dependency closure.
%global pkg_suffix -free

# SONAME majors for FFmpeg %{version} (update on rebase if configure fails on %files)
%global lavu_major   60
%global lavc_major   62
%global lavf_major   62
%global lavfi_major  11
%global lavd_major   62
%global lsws_major   9
%global lswr_major   6

Name:            ffmpeg
Version:         8.1
Release:         5%{?dist}
Summary:         Digital VCR and streaming server
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:             https://ffmpeg.org/

Source0:         https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz

BuildRequires:   gcc
BuildRequires:   gcc-c++
BuildRequires:   make
BuildRequires:   perl
BuildRequires:   pkgconfig
BuildRequires:   zlib-devel
BuildRequires:   bzip2-devel
BuildRequires:   xz-devel
BuildRequires:   gnutls-devel
BuildRequires:   lame-devel
BuildRequires:   libvpx-devel
BuildRequires:   opus-devel
BuildRequires:   libvorbis-devel
BuildRequires:   alsa-lib-devel
%ifarch %{ix86} x86_64
BuildRequires:   nasm
%endif

%description
FFmpeg is a complete and free Internet live audio and video broadcasting
solution for Linux. It also includes a digital VCR and webcam support.

This build enables common free codecs (VPx, Opus, Vorbis, MP3 via LAME)
and HTTPS via GnuTLS. ffplay is disabled to avoid a SDL2 dependency.

Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libswscale%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavfilter%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavdevice%{?pkg_suffix}%{_isa} = %{version}-%{release}
Provides:        ffmpeg-free = %{version}-%{release}
Obsoletes:       ffmpeg-libs < %{version}-%{release}
Provides:        ffmpeg-libs = %{version}-%{release}

%package -n libavutil%{?pkg_suffix}
Summary:         FFmpeg utility library
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later

%description -n libavutil%{?pkg_suffix}
The libavutil library is a utility library to aid portable multimedia
programming.

%package -n libavutil%{?pkg_suffix}-devel
Summary:         Development files for libavutil
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        pkgconfig

%description -n libavutil%{?pkg_suffix}-devel
Headers and pkg-config files for developing with libavutil.

%package -n libswresample%{?pkg_suffix}
Summary:         FFmpeg audio resampling library
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libswresample%{?pkg_suffix}
The libswresample library performs highly optimized audio resampling, rematrixing
and sample format conversion.

%package -n libswresample%{?pkg_suffix}-devel
Summary:         Development files for libswresample
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        pkgconfig

%description -n libswresample%{?pkg_suffix}-devel
Headers and pkg-config files for developing with libswresample.

%package -n libswscale%{?pkg_suffix}
Summary:         FFmpeg image scaling and colorspace library
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libswscale%{?pkg_suffix}
The libswscale library performs highly optimized image scaling and colorspace
conversion.

%package -n libswscale%{?pkg_suffix}-devel
Summary:         Development files for libswscale
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswscale%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        pkgconfig

%description -n libswscale%{?pkg_suffix}-devel
Headers and pkg-config files for developing with libswscale.

%package -n libavcodec%{?pkg_suffix}
Summary:         FFmpeg codec library
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libvpx%{_isa}

%description -n libavcodec%{?pkg_suffix}
The libavcodec library provides a generic encoding and decoding framework.

%package -n libavcodec%{?pkg_suffix}-devel
Summary:         Development files for libavcodec
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        pkgconfig

%description -n libavcodec%{?pkg_suffix}-devel
Headers and pkg-config files for developing with libavcodec.

%package -n libavformat%{?pkg_suffix}
Summary:         FFmpeg container format library
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libavformat%{?pkg_suffix}
The libavformat library provides a generic framework for muxing and demuxing.

%package -n libavformat%{?pkg_suffix}-devel
Summary:         Development files for libavformat
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        pkgconfig

%description -n libavformat%{?pkg_suffix}-devel
Headers and pkg-config files for developing with libavformat.

%package -n libavfilter%{?pkg_suffix}
Summary:         FFmpeg audio and video filtering library
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libswscale%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libavfilter%{?pkg_suffix}
The libavfilter library provides a generic audio and video filtering framework.

%package -n libavfilter%{?pkg_suffix}-devel
Summary:         Development files for libavfilter
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavformat%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswscale%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavfilter%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        pkgconfig

%description -n libavfilter%{?pkg_suffix}-devel
Headers and pkg-config files for developing with libavfilter.

%package -n libavdevice%{?pkg_suffix}
Summary:         FFmpeg device handling library
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavcodec%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavfilter%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavformat%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        libavutil%{?pkg_suffix}%{_isa} = %{version}-%{release}

%description -n libavdevice%{?pkg_suffix}
The libavdevice library provides a framework for grabbing from and rendering to
multimedia devices.

%package -n libavdevice%{?pkg_suffix}-devel
Summary:         Development files for libavdevice
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavfilter%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavformat%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavdevice%{?pkg_suffix}%{_isa} = %{version}-%{release}
Requires:        pkgconfig

%description -n libavdevice%{?pkg_suffix}-devel
Headers and pkg-config files for developing with libavdevice.

%package devel
Summary:         Meta-package pulling all FFmpeg development libraries
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        libavutil%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswresample%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libswscale%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavcodec%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavformat%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavfilter%{?pkg_suffix}-devel = %{version}-%{release}
Requires:        libavdevice%{?pkg_suffix}-devel = %{version}-%{release}
Provides:        ffmpeg-free-devel = %{version}-%{release}

%description devel
Convenience meta-package that installs headers and pkg-config files for every
FFmpeg library built in this stack (Fedora-style split).

%package doc
Summary:         FFmpeg presets, ffprobe schema, and upstream C examples
BuildArch:       noarch
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires:        %{name} = %{version}-%{release}

%description doc
libvpx .ffpreset files, ffprobe.xsd, and the upstream C example tree under
%{_datadir}/ffmpeg/examples.

%prep
%setup -q -n ffmpeg-%{version}

%build
export CFLAGS="%{build_cflags}"
export CXXFLAGS="%{build_cxxflags}"
export LDFLAGS="%{build_ldflags}"

./configure \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --libdir=%{_libdir} \
  --shlibdir=%{_libdir} \
  --incdir=%{_includedir} \
  --datadir=%{_datadir}/ffmpeg \
  --mandir=%{_mandir} \
  --docdir=%{_docdir}/%{name} \
  --disable-static \
  --enable-shared \
  --enable-gpl \
  --enable-version3 \
  --disable-debug \
  --disable-stripping \
  --disable-htmlpages \
  --disable-podpages \
  --disable-txtpages \
  --enable-pic \
  --disable-ffplay \
  --enable-zlib \
  --enable-bzlib \
  --enable-lzma \
  --enable-gnutls \
  --enable-alsa \
  --enable-libvorbis \
  --enable-libopus \
  --enable-libvpx \
  --enable-libmp3lame \
  --extra-cflags="%{build_cflags}" \
  --extra-ldflags="%{build_ldflags}"

%make_build V=1

%install
%make_install

find %{buildroot} -name '*.la' -delete

rm -rf %{buildroot}%{_docdir}/%{name}
install -d %{buildroot}%{_docdir}/%{name}
install -pm644 README.md %{buildroot}%{_docdir}/%{name}/

install -d %{buildroot}%{_licensedir}/%{name}
install -pm644 COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv2.1 COPYING.LGPLv3 LICENSE.md \
    %{buildroot}%{_licensedir}/%{name}/

%files
%license %{_licensedir}/%{name}/*
%doc %{_docdir}/%{name}/README.md
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
%{_mandir}/man1/ffmpeg*.1*
%{_mandir}/man1/ffprobe*.1*

%files -n libavutil%{?pkg_suffix}
%license %{_licensedir}/%{name}/*
%{_libdir}/libavutil.so.%{lavu_major}*

%ldconfig_scriptlets -n libavutil%{?pkg_suffix}

%files -n libavutil%{?pkg_suffix}-devel
%{_includedir}/libavutil
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/libavutil.so
%{_mandir}/man3/libavutil*.3.gz

%files -n libswresample%{?pkg_suffix}
%license %{_licensedir}/%{name}/*
%{_libdir}/libswresample.so.%{lswr_major}*

%ldconfig_scriptlets -n libswresample%{?pkg_suffix}

%files -n libswresample%{?pkg_suffix}-devel
%{_includedir}/libswresample
%{_libdir}/pkgconfig/libswresample.pc
%{_libdir}/libswresample.so
%{_mandir}/man3/libswresample*.3.gz

%files -n libswscale%{?pkg_suffix}
%license %{_licensedir}/%{name}/*
%{_libdir}/libswscale.so.%{lsws_major}*

%ldconfig_scriptlets -n libswscale%{?pkg_suffix}

%files -n libswscale%{?pkg_suffix}-devel
%{_includedir}/libswscale
%{_libdir}/pkgconfig/libswscale.pc
%{_libdir}/libswscale.so
%{_mandir}/man3/libswscale*.3.gz

%files -n libavcodec%{?pkg_suffix}
%license %{_licensedir}/%{name}/*
%{_libdir}/libavcodec.so.%{lavc_major}*

%ldconfig_scriptlets -n libavcodec%{?pkg_suffix}

%files -n libavcodec%{?pkg_suffix}-devel
%{_includedir}/libavcodec
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/libavcodec.so
%{_mandir}/man3/libavcodec*.3.gz

%files -n libavformat%{?pkg_suffix}
%license %{_licensedir}/%{name}/*
%{_libdir}/libavformat.so.%{lavf_major}*

%ldconfig_scriptlets -n libavformat%{?pkg_suffix}

%files -n libavformat%{?pkg_suffix}-devel
%{_includedir}/libavformat
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/libavformat.so
%{_mandir}/man3/libavformat*.3.gz

%files -n libavfilter%{?pkg_suffix}
%license %{_licensedir}/%{name}/*
%{_libdir}/libavfilter.so.%{lavfi_major}*

%ldconfig_scriptlets -n libavfilter%{?pkg_suffix}

%files -n libavfilter%{?pkg_suffix}-devel
%{_includedir}/libavfilter
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/libavfilter.so
%{_mandir}/man3/libavfilter*.3.gz

%files -n libavdevice%{?pkg_suffix}
%license %{_licensedir}/%{name}/*
%{_libdir}/libavdevice.so.%{lavd_major}*

%ldconfig_scriptlets -n libavdevice%{?pkg_suffix}

%files -n libavdevice%{?pkg_suffix}-devel
%{_includedir}/libavdevice
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/libavdevice.so
%{_mandir}/man3/libavdevice*.3.gz

%files devel
%doc README.md

%files doc
%{_datadir}/ffmpeg/

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.1-3
- Package extra man1 pages, man3 API pages in devel, ffmpeg-doc for data dir and examples

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.1-2
- Disable RPM LTO (%%global _lto_cflags %%{nil}) fix shared lib link libavcodec/libswscale

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.1-1
- Add FFmpeg 8.1 (GPLv3+, libs, devel, common free codecs, GnuTLS)
