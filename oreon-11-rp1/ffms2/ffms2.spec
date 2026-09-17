%global source0_hash 7770af0bbc0063f9580a6a5c8e7c51f1788f171d7da0b352e48a1e60943a8c3c

%global git 0
%global gittag 5.0-RC3

Name:           ffms2
Version:        5.0
Release:        8%{?dist}
# src/index/vsutf16.h is LGPL-2.1-or-later
# the rest is MIT-licensed
License:        MIT AND LGPL-2.1-or-later
Summary:        Video source library for easy frame accurate access
URL:            https://github.com/FFMS/ffms2
%if 0%{?git}
Source0:        %{url}/archive/%{gittag}/ffms2-%{gittag}.tar.gz
# run ffms2-samples.sh to fetch samples from upstream
%else
Source0:        %{url}/archive/%{version}/ffms2-%{version}.tar.gz
%endif
Source1:        ffms2-samples.tar.gz
Source2:        ffms2-samples.sh
Patch:          ffms2-use-latest-stdc.patch
Patch:          ffms2-use-system-vapoursynth.patch
Patch:          ffms2-use-system-gtest.patch
Patch:          ffms2-skip-unsupported-codec-tests.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  gtest-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  zlib-devel

%description
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around FFmpeg. It gives you an easy, convenient way to say "open and
decompress this media file for me, I don't care how you do it" and get frame-
and sample-accurate access (usually), without having to bother with the
sometimes less than straightforward and less than perfectly documented FFmpeg
API.

%package devel
Summary:        Development package for ffms2
Requires:       ffms2%{?_isa} = %{version}-%{release}

%description devel
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper 
library around FFmpeg.

This package contains the headers and development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?git}
%autosetup -p1 -n ffms2-%{gittag} -a 1
%else
%autosetup -p1 -a 1
%endif
rm -rv src/vapoursynth/V*.h
mkdir -p src/config
autoreconf -vfi

%build
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
rm -v %{buildroot}%{_libdir}/libffms2.la
rm -rv %{buildroot}%{_docdir}

%check
# HDR test uses unsupported H.265 codec samples, so run only the other two tests
CPPFLAGS=-I/usr/include/ffmpeg make -C test SAMPLES_DIR=$(pwd)/test/samples TESTS="indexer display_matrix" run

%files
%license COPYING
%doc README.md
%{_bindir}/ffmsindex
%{_libdir}/libffms2.so.5{,.*}

%files devel
%doc doc/*
%{_libdir}/libffms2.so
%{_includedir}/ffms{,compat}.h
%{_libdir}/pkgconfig/ffms2.pc

%changelog
%autochangelog
