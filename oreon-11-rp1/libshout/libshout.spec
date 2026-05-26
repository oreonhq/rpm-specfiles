Name:           libshout
Version:        2.4.6
Release:        10%{?dist}
Summary:        Icecast source streaming library

# COPYING:              GPLv2 text
# include/shout/shout.h.in:     LGPLv2+
# README:               LGPLv2+
# src/codec_opus.c:     LGPLv2+
# src/codec_speex.c:    LGPLv2+
# src/codec_theora.c:   LGPLv2+
# src/codec_vorbis.c:   LGPLv2+
# src/common/avl/avl.c: MIT
# src/common/httpp/encoding.c:  LGPLv2+
# src/common/httpp/encoding.h:  LGPLv2+
# src/common/httpp/httpp.c:     LGPLv2+
# src/common/httpp/httpp.h:     LGPLv2+
# src/common/net/resolver.c:    LGPLv2+
# src/common/net/resolver.h:    LGPLv2+
# src/common/net/sock.c:        LGPLv2+
# src/common/net/sock.h:        LGPLv2+
# src/common/thread/thread.c:   LGPLv2+
# src/common/thread/thread.h:   LGPLv2+
# src/common/timing/timing.c:   LGPLv2+
# src/common/timing/timing.h:   LGPLv2+
# src/connection.c:     LGPLv2+
# src/format_mp3.c:     LGPLv2+
# src/format_ogg.c:     LGPLv2+
# src/format_ogg.h:     LGPLv2+
# src/format_webm.c:    LGPLv2+
# src/proto_http.c:     LGPLv2+
# src/proto_icy.c:      LGPLv2+
# src/proto_roaraudio.c:    LGPLv2+
# src/proto_xaudiocast.c:   LGPLv2+
# src/queue.c:          LGPLv2+
# src/shout.c:          LGPLv2+
# src/shout_private.h:  LGPLv2+
# src/tls.c:            LGPLv2+
# src/util.c:           LGPLv2+
# src/util.h:           LGPLv2+
## Not in a binary package
# aclocal.m4:           GPLv2+ with Autoconf exception and FSFULLR
# compile:              GPLv2+ with Autoconf exception
# config.guess:         GPLv3+ with Autoconf exception
# config.sub:           GPLv3+ with Autoconf exception
# configure:            GPLv2+ with Libtool exception and FSFUL
# depcomp:              GPLv2+ with Autoconf exception
# doc/Makefile.in:      FSFULLR
# examples/Makefile.in: FSFULLR
# include/Makefile.in:  FSFULLR
# include/shout/Makefile.in:    FSFULLR
# install-sh:           MIT
# ltmain.sh:            GPLv2+ with a Libtool exception
# m4/lt~obsolete.m4:    FSFULLR
# m4/ltoptions.m4:      FSFULLR
# m4/ltsugar.m4:        FSFULLR
# m4/ltversion.m4:      FSFULLR
# m4/libtool.m4:        GPLv2+ with Libtool exception and FSFULLR and FSFUL
# Makefile.in:          FSFULLR
# missing:              GPLv2+ with Autoconf exception
# src/common/avl/COPYING:       LGPLv2 text
# src/common/avl/Makefile.in:   FSFULLR
# src/common/httpp/COPYING:     LGPLv2 text
# src/common/httpp/Makefile.in: FSFULLR
# src/common/httpp/README:      LGPLv2+
# src/common/net/COPYING:       LGPLv2 text
# src/common/net/Makefile.in:   FSFULLR
# src/common/thread/COPYING:    LGPLv2 text
# src/common/thread/Makefile.in:    FSFULLR
# src/common/timing/COPYING:    LGPLv2 text
# src/common/timing/Makefile.in:    FSFULLR
# src/Makefile.in:      FSFULLR
# win32/Makefile.in:    FSFULLR
License:        LGPL-2.0-or-later
URL:            https://www.icecast.org/
Source:         https://downloads.us.xiph.org/releases/libshout/libshout-%{version}.tar.gz
# Fedora does not support ckport. Enable disabling it.
# <https://gitlab.xiph.org/xiph/icecast-libshout/issues/2314>
Patch0:         libshout-2.4.3-Allow-disabling-ckport-database-installation.patch
# Enforce a Fedora system-wide crypto policy
# <https://docs.fedoraproject.org/en-US/packaging-guidelines/CryptoPolicies/#_cc_applications>
Patch1:         libshout-2.4.3-Default-OpenSSL-cipher-list-is-PROFILE-SYSTEM.patch
# oreon url source checksums begin
%global source0_sha256 39cbd4f0efdfddc9755d88217e47f8f2d7108fa767f9d58a2ba26a16d8f7c910
%global source0_file libshout-2.4.6.tar.gz
# oreon url source checksums end

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  sed
BuildRequires: make

%description
libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%package        devel
Summary:        Header files for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libshout-devel package contains the header files needed for developing
applications that send data to an icecast server.  Install libshout-devel if
you want to develop applications using libshout.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libshout-2.4.6.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "39cbd4f0efdfddc9755d88217e47f8f2d7108fa767f9d58a2ba26a16d8f7c910" || { echo "oreon: Source0 SHA256 mismatch for libshout-2.4.6.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P0 -p1
%patch -P1 -p1
autoreconf -fi

%build
%configure \
  --disable-ckport \
  --enable-examples \
  --enable-pkgconfig \
  --disable-silent-rules \
  --enable-shared \
  --enable-speex \
  --disable-static \
  --enable-theora \
  --enable-thread

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install

find $RPM_BUILD_ROOT -type f -name "*.la" -delete

rm -rf $RPM_BUILD_ROOT%{_docdir}

%files
%doc NEWS README
%license COPYING
%{_bindir}/shout
%{_libdir}/libshout.so.3
%{_libdir}/libshout.so.3.*
%{_mandir}/*/shout.*

%files devel
%doc examples/*.c doc/*.xml
%{_libdir}/libshout.so
%{_libdir}/pkgconfig/shout.pc
%{_includedir}/shout/
%{_datadir}/aclocal/shout.m4

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.6-10
- Prepare for Oreon 11 (RP1)
