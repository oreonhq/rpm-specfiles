%global source0_hash 32a5ab5bfbb9752cb6a46627e4c410e61939c8dbbd833ac858473cfbd9fb9d7d
Name:    pjproject
Summary:        Libraries for building embedded/non-embedded VoIP applications
Version: 2.13.1
Release:        8%{?dist}
License: GPL-2.0-or-later AND BSD-3-Clause
URL:     http://www.pjsip.org
Source0:        https://github.com/pjsip/pjproject/archive/%{version}/%{name}-%{version}.tar.gz
Patch: 0001-Tell-the-build-system-not-to-use-most-of-the-third_party-directory.patch
Patch: 0002-Add-a-config_site.h-file.patch
Patch: 0003-Fix-ARMv7-endianness.patch
Patch: 0004-Add-aarch64-detection.patch
Patch: 0005-Add-ppc64-detection.patch
Patch: 0006-Add-s390-detection.patch
Patch: 0007-Don-t-use-SSE2-if-it-is-not-available.patch
Patch: 0008-Add-riscv-support.patch
Provides: bundled(webrtc) = 90
Provides: bundled(srtp) = 2.1.0
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  libsrtp-devel
BuildRequires:  libuuid-devel
BuildRequires:  libyuv-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
# /oreon:deps
%description
This package provides the Open Source, comprehensive, high performance,
small footprint multimedia communication libraries written in C
language for building embedded/non-embedded VoIP applications.
It contains:
- PJSIP - Open Source SIP Stack
- PJMEDIA - Open Source Media Stack
- PJNATH - Open Source NAT Traversal Helper Library
- PJLIB-UTIL - Auxiliary Library
- PJLIB - Ultra Portable Base Framework Library
- PJSUA2 - Object Oriented abstractions layer for PJSUA

%package devel
Summary: Development files to use pjproject
Requires: %{name} = %{version}-%{release}
%description devel
Header information for:
- PJSIP - Open Source SIP Stack
- PJMEDIA - Open Source Media Stack
- PJNATH - Open Source NAT Traversal Helper Library
- PJLIB-UTIL - Auxiliary Library
- PJLIB - Ultra Portable Base Framework Library

%package -n pjsua
Summary: command line SIP user agent
Requires: %{name} = %{version}-%{release}
%description -n pjsua
pjsua is an open source command line SIP user agent (softphone)
that is used as the reference implementation for PJSIP, PJNATH, and PJMEDIA.
Despite its simple command line appearance, it does pack many features!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Update old FSF addresses
grep -ril '59 Temple Place' * | xargs sed -i 's/59 Temple Place,\s\+Suite 330,/51 Franklin Street, Fifth Floor,/im'
grep -ril '59 Temple Place' * | xargs sed -i 's/59 Temple Place - Suite 330,/51 Franklin Street, Fifth Floor,/im'
grep -ril 'Boston, MA\s\+02111-1307' * | xargs sed -i 's/Boston,\s\+MA\s\+02111-1307/Boston, MA  02110-1335/im'

# make sure we don't bundle these third-party libraries
# (They're excluded through ./configure, but this is an
# additional safety net)
# Kept bundled libraries: see Provides: bundled(...) above
rm -rf third_party/BaseClasses
rm -rf third_party/bdsound
rm -rf third_party/bin
rm -rf third_party/g7221
rm -rf third_party/gsm
rm -rf third_party/ilbc
rm -rf third_party/milenage
rm -rf third_party/mp3
rm -rf third_party/resample
rm -rf third_party/speex
# rm -rf third_party/srtp
# rm -rf third_party/webrtc
rm -rf third_party/threademulation
rm -rf third_party/yuv
rm -rf third_party/build/baseclasses
rm -rf third_party/build/g7221
rm -rf third_party/build/gsm
rm -rf third_party/build/ilbc
rm -rf third_party/build/milenage
rm -rf third_party/build/resample
rm -rf third_party/build/samplerate
rm -rf third_party/build/speex
# rm -rf third_party/build/srtp
# rm -rf third_party/build/webrtc
rm -rf third_party/build/yuv

%build

autoconf aconfigure.ac > aconfigure
export CFLAGS="-DPJ_HAS_IPV6=1 -DNDEBUG ${ARCHFLAGS} %{optflags}"
%configure --enable-shared        \
           --with-external-gsm    \
           --with-external-pa     \
           --with-external-speex  \
           --with-external-yuv    \
           --disable-opencore-amr \
           --disable-resample     \
           --disable-sound        \
           --disable-video        \
           --disable-v4l2         \
           --disable-ilbc-codec   \
           --disable-g7221-codec  
make -j1 dep
make -j1
%install
%make_install
install -p -D -m 0755 pjsip-apps/bin/pjsua-* %{buildroot}%{_bindir}/pjsua
find %{buildroot} -type f -name "*.a" -delete
%oreon_autofiles pjsua usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pjproject-devel -f %{oreon_filedir}/pjproject-devel.list
%files -n pjsua -f %{oreon_filedir}/pjsua.list

%changelog

%autochangelog
