%global source0_hash 11de897f455a95ba58546bdcd40a95d3bda69866ec5f7879a83b024126c54c2a

Name:           ezstream
Version:        1.0.2
Release:        15%{?dist}
Summary:        Command line source client for Icecast media streaming servers
## Not installed files:
# aclocal.m4:               FSFULLRWD
# build-aux/compile:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/config.guess:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/config.rpath:   FSFULLR
# build-aux/config.sub:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/depcomp:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/install-sh:     X11 AND LicenseRef-Fedora-Public-Domain
# build-aux/ltmain.sh:      GPL-2.0-or-later WITH Libtool-exception AND
#                           GPL-3.0-or-later WITH Libtool-exception AND
#                           TODO:
#                           <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/661>
#                           GPL-3.0-or-later
# build-aux/missing:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/test-driver:    GPL-2.0-or-later WITH Autoconf-exception-generic
# compat/getopt.c:          ISC AND BSD-2-Clause
# compat/reallocarray.c:    ISC
# configure:                FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# doc/Makefile.in:          FSFULLRWD
# examples/Makefile.in:     FSFULLRWD
# INSTALL:                  FSFUL
# m4/attribute.m4:          ISC
# m4/ccflags.m4:            ISC
# m4/libshout.m4:           ISC
# m4/libtool.m4:            FSFULLR AND GPL-2.0-or-later WITH Libtool-exception AND FSFUL
# m4/libxml2.m4:            ISC
# m4/ltoptions.m4:          FSFULLR
# m4/ltsugar.m4:            FSFULLR
# m4/ltversion.m4:          FSFULLR
# m4/Makefile.in:           FSFULLRWD
# m4/tree.m4:               ISC
# Makefile.in:              FSFULLRWD
# src/Makefile.in:          FSFULLRWD
# tests/Makefile.in:        FSFULLRWD
## Installed files:
# compat/strlcat.c:         ISC
# compat/strlcpy.c:         ISC
# compat/strtonum.c:        ISC
# COPYING:                  GPL-2.0-only
# doc/ezstream-cfgmigrate.1.in.in:  ISC
# doc/ezstream-file.sh.1.in.in:     ISC
# doc/ezstream.1.in.in:             GPL-2.0-only
# src/cfg.c:                ISC
# src/cfg.h:                ISC
# src/cfg_decoder.c:        ISC
# src/cfg_decoder.h:        ISC
# src/cfg_encoder.c:        ISC
# src/cfg_encoder.h:        ISC
# src/cfg_intake.c:         ISC
# src/cfg_intake.h:         ISC
# src/cfg_private.h:        ISC
# src/cfg_server.c:         ISC
# src/cfg_server.h:         ISC
# src/cfg_stream.c:         ISC
# src/cfg_stream.h:         ISC
# src/cfgfile_xml.c:        ISC
# src/cfgfile_xml.h:        ISC
# src/cmdline.c:            ISC
# src/cmdline.h:            ISC
# src/ezconfig0.c:          GPL-2.0-only
# src/ezconfig0.h:          GPL-2.0-only
# src/ezstream.c:           GPL-2.0-only
# src/ezstream.h:           ISC
# src/ezstream-cfgmigrate.c:    ISC
# src/ezstream-file.sh.in:  ISC
# src/log.c:                ISC
# src/log.h:                ISC
# src/mdata.c:              ISC
# src/mdata.h:              ISC
# src/playlist.c:           ISC
# src/playlist.h:           ISC
# src/stream.c:             ISC
# src/stream.h:             ISC
# src/util.c:               GPL-2.0-only
# src/util.h:               GPL-2.0-only
# src/xalloc.c:             ISC
# src/xalloc.h:             ISC
License:        GPL-2.0-only AND ISC
URL:            https://www.icecast.org/%{name}/
Source0:        https://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
# Link to distribution-wide certificate store, not upsreamable
Patch0:         ezstream-1.0.1-doc-Link-to-distribution-OpenSSL-certificate-bundle.patch
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake >= 1.10
BuildRequires:  coreutils
BuildRequires:  gcc
# gettext-devel for AM_ICONV macro
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2
BuildRequires:  pkgconfig(shout) >= 2.2
BuildRequires:  pkgconfig(taglib_c) >= 1.4

%description
Ezstream is a command line source client for media streams, primarily for
streaming to Icecast servers.

It allows the creation of media streams based on input from files or standard
input that is piped through an optional external decoder and encoder. As every
part of this chain is highly configurable, ezstream can be useful in a large
number of streaming setups.

Supported media containers for streaming are MP3, Ogg, Theora, WebM, and
Matroska. Supported transport protocols are HTTP, ICY, and RoarAudio.
Metadata support is provided by TagLib library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
# Regenerate a build script
autoreconf -I /usr/share/gettext/m4 -fi
# Remove bundled code
rm compat/{getopt,reallocarray}.c
# Copy examples for a documention
mkdir __examples
cp -a examples __examples/examples
rm -f __examples/examples/Makefile*
chmod a-x __examples/examples/*

%build
%configure \
    --without-asan \
    --enable-largefile \
    --disable-maintainer-mode \
    --disable-rpath \
    --enable-shared \
    --disable-static
# --with-taglib actually inhibits the taglib support
%{make_build}

%check
make %{?_smp_mflags} check

%install
%{make_install}
rm -rf $RPM_BUILD_ROOT%{_docdir} $RPM_BUILD_ROOT%{_datadir}/examples

%files
%license COPYING
%doc ChangeLog NEWS README.md __examples/examples
%{_bindir}/ezstream
%{_bindir}/ezstream-cfgmigrate
%{_bindir}/ezstream-file.sh
%{_mandir}/man1/ezstream.1*
%{_mandir}/man1/ezstream-cfgmigrate.1*
%{_mandir}/man1/ezstream-file.sh.1*

%changelog
%autochangelog
