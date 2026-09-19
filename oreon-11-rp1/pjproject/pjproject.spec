%global source0_hash 32a5ab5bfbb9752cb6a46627e4c410e61939c8dbbd833ac858473cfbd9fb9d7d

Name:    pjproject
Summary: Libraries for building embedded/non-embedded VoIP applications
Version: 2.13.1
Release: 8%{?dist}
# main source code is GPL-2.0-or-later
# third_party/srtp is BSD-3-Clause
# third_party/webrtc is BSD-3-Clause
License: GPL-2.0-or-later AND BSD-3-Clause
URL:     http://www.pjsip.org

Source: https://github.com/pjsip/pjproject/archive/%{version}/%{name}-%{version}.tar.gz

Patch: 0001-Tell-the-build-system-not-to-use-most-of-the-third_party-directory.patch
Patch: 0002-Add-a-config_site.h-file.patch
Patch: 0003-Fix-ARMv7-endianness.patch
Patch: 0004-Add-aarch64-detection.patch
Patch: 0005-Add-ppc64-detection.patch
Patch: 0006-Add-s390-detection.patch
Patch: 0007-Don-t-use-SSE2-if-it-is-not-available.patch
Patch: 0008-Add-riscv-support.patch

BuildRequires: make
BuildRequires: autoconf
BuildRequires: alsa-lib-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gsm-devel
BuildRequires: libsrtp-devel
BuildRequires: libuuid-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: portaudio-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel
BuildRequires: libyuv-devel

# See third_party/webrtc/README.chromium
# (version shipped in Fedora (webrtc-audio-processing) is incompatible)
Provides: bundled(webrtc) = 90

# See third_party/srtp/VERSION
# (libsrtp-2.3.0 shipped in Fedora seems incompatible,
# results in Error initializing SRTP library: cipher failure [status=259807])
Provides: bundled(srtp) = 2.1.0

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
# Regenerate aconfigure for Patch8
autoconf aconfigure.ac > aconfigure

# We're building without audio or video support, as Asterisk isn't using
# that functionality, and it made it easier to ensure that we don't
# bundle any unnecessary libraries.  Please contact me if your project
# needs this support, and I'll re-enable it
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

#make %{?_smp_mflags} dep
#make %{?_smp_mflags}
make -j1 dep
make -j1

%install
%make_install

install -p -D -m 0755 pjsip-apps/bin/pjsua-* %{buildroot}%{_bindir}/pjsua

# Remove the static libraries, as they aren't wanted
find %{buildroot} -type f -name "*.a" -delete

%files
%doc README.txt README-RTEMS INSTALL.txt
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/pj++/
%{_includedir}/pj/
%{_includedir}/pjlib-util/
%{_includedir}/pjmedia-audiodev/
%{_includedir}/pjmedia-codec/
%{_includedir}/pjmedia-videodev/
%{_includedir}/pjmedia/
%{_includedir}/pjnath/
%{_includedir}/pjsip-simple/
%{_includedir}/pjsip-ua/
%{_includedir}/pjsip/
%{_includedir}/pjsua-lib/
%{_includedir}/pjsua2/
%{_includedir}/*.h
%{_includedir}/*.hpp
%{_libdir}/pkgconfig/libpjproject.pc

%files -n pjsua
%{_bindir}/pjsua

%changelog
%autochangelog
