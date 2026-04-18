# Red Hat %%optflags default -flto breaks final link of libavcodec/libswscale .so
# (R_X86_64_PC32 against undefined symbol e.g. pd_1 in .ltrans object).
%global _lto_cflags %{nil}

# SONAME majors for FFmpeg %{version} (update on rebase if configure fails on %%files)
%global lavu_major   60
%global lavc_major   62
%global lavf_major   62
%global lavfi_major  11
%global lavd_major   62
%global lsws_major   9
%global lswr_major   6

Name:            ffmpeg
Version:         8.1
Release:         3%{?dist}
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

Requires:        %{name}-libs%{?_isa} = %{version}-%{release}
Provides:        ffmpeg-free = %{version}-%{release}

%package libs
Summary:         Libraries for FFmpeg apps
Provides:        ffmpeg-free-libs = %{version}-%{release}
Provides:        libavutil-free = %{version}-%{release}
Provides:        libavcodec-free = %{version}-%{release}
Provides:        libavformat-free = %{version}-%{release}
Provides:        libavfilter-free = %{version}-%{release}
Provides:        libavdevice-free = %{version}-%{release}
Provides:        libswscale-free = %{version}-%{release}
Provides:        libswresample-free = %{version}-%{release}
Requires:        libvpx%{?_isa}

%description libs
libavcodec, libavformat, libavutil, and related shared libraries.

%package devel
Summary:         Development headers and libraries for FFmpeg
Requires:        %{name}-libs%{?_isa} = %{version}-%{release}
Provides:        ffmpeg-free-devel = %{version}-%{release}
Provides:        libavutil-free-devel = %{version}-%{release}
Provides:        libavcodec-free-devel = %{version}-%{release}
Provides:        libavformat-free-devel = %{version}-%{release}
Provides:        libavfilter-free-devel = %{version}-%{release}
Provides:        libavdevice-free-devel = %{version}-%{release}
Provides:        libswscale-free-devel = %{version}-%{release}
Provides:        libswresample-free-devel = %{version}-%{release}

%description devel
Headers, pkg-config files, and unversioned shared library symlinks for
developing against FFmpeg.

%package doc
Summary:         FFmpeg presets, ffprobe schema, and upstream C examples
BuildArch:       noarch
Requires:        %{name} = %{version}-%{release}

%description doc
libvpx .ffpreset files, ffprobe.xsd, and the upstream C example tree under
%{_datadir}/ffmpeg/examples.

%prep
%autosetup -p1 -n ffmpeg-%{version}

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

%ldconfig_scriptlets libs

%files
%license %{_licensedir}/%{name}/*
%doc %{_docdir}/%{name}/README.md
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
%{_mandir}/man1/ffmpeg*.1*
%{_mandir}/man1/ffprobe*.1*

%files libs
%{_libdir}/libavutil.so.%{lavu_major}*
%{_libdir}/libavcodec.so.%{lavc_major}*
%{_libdir}/libavformat.so.%{lavf_major}*
%{_libdir}/libavfilter.so.%{lavfi_major}*
%{_libdir}/libavdevice.so.%{lavd_major}*
%{_libdir}/libswscale.so.%{lsws_major}*
%{_libdir}/libswresample.so.%{lswr_major}*

%files devel
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavfilter
%{_includedir}/libavformat
%{_includedir}/libavutil
%{_includedir}/libswresample
%{_includedir}/libswscale
%{_libdir}/libavcodec.so
%{_libdir}/libavdevice.so
%{_libdir}/libavfilter.so
%{_libdir}/libavformat.so
%{_libdir}/libavutil.so
%{_libdir}/libswresample.so
%{_libdir}/libswscale.so
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/pkgconfig/libswresample.pc
%{_libdir}/pkgconfig/libswscale.pc
%{_mandir}/man3/libav*.3.gz
%{_mandir}/man3/libsw*.3.gz

%files doc
%{_datadir}/ffmpeg/

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.1-3
- Package extra man1 pages, man3 API pages in devel, ffmpeg-doc for data dir and examples

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.1-2
- Disable RPM LTO (%%global _lto_cflags %%{nil}) fix shared lib link libavcodec/libswscale

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.1-1
- Add FFmpeg 8.1 (GPLv3+, libs, devel, common free codecs, GnuTLS)
