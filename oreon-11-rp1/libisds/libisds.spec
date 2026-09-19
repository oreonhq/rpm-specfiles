%global source0_hash 6146f837b27b11a6071e2148f7ae64521b4d8ad45325f998fe7b373137e418fb

# Build manual pages
%bcond_without libisds_enables_man
# Support network operations
%bcond_without libisds_enables_net
# Use OpenSSL instead of libgcrypt and gpgme
%bcond_with libisds_enables_openssl
# Perform tests
%bcond_without libisds_enables_test

Name:           libisds
Version:        0.11.2
Release:        15%{?dist}
Summary:        Library for accessing the Czech Data Boxes
# COPYING:      LGPL-3.0 text
# README:       LGPL-3.0-or-later
# src/gettext.h:            GPL-3.0-or-later
## Not delivered in any binary package
# aclocal.m4:   GPL-2.0-or-later WITH Libtool-exception AND FSFULLR
# client/Makefile.in:       FSFULLR
# config.guess: GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.rpath: FSFULLR
# config.sub:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# configure:    GPL-2.0-or-later WITH Libtool-exception AND FSFUL
# depcomp:      GPL-2.0-or-later WITH Libtool-exception
# doc/Makefile.in:  FSFULLR
# install-sh:       X11 AND LicenseRef-Fedora-Public-Domain
# ltmain.sh:        GPL-2.0-or-later WITH Libtool-exception AND
#                   GPL-3.0-or-later WITH Libtool-exception AND
#                   GPL-3.0-or-later
# m4/gettext.m4:    FSFULLR
# m4/gpgme.m4:      FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/libgcrypt.m4:  FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/libtool.m4:    GPL-2.0-or-later WITH Libtool-exception AND FSFUL
# m4/ltoptions.m4:  FSFULLR
# m4/ltsugar.m4:    FSFULLR
# m4/lt~obsolete.m4:    FSFULLR
# m4/ltversion.m4:  FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# Makefile.in:      FSFULLR
# missing:          GPL-2.0-or-later WITH Libtool-exception
# po/Makefile.in.in:    LicenseRef-Fedora-UltraPermissive
#                       <https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/764>
# src/Makefile.in:          FSFULLR
# test/Makefile.in:         FSFULLR
# test/offline/Makefile.in: FSFULLR
# test/online/Makefile.in:  FSFULLR
# test/simline/Makefile.in: FSFULLR
# test-driver:      GPL-2.0-or-later WITH Libtool-exception
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Libtool-exception AND FSFULLR AND FSFUL AND X11 AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
Source1:        %{url}dist/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
# Adapt tests to changes in curl-7.83, in upstream after 0.11.2,
# <https://github.com/curl/curl/issues/8844>
Patch0:         libisds-0.11.2-tests-Do-not-send-multi-line-HTTP-headers-by-server.patch
# Do not use deprecated CURLOPT_PROGRESSFUNCTION option,
# in upstream after 0.11.2
Patch1:         libisds-0.11.2-Use-CURLOPT_XFERINFOFUNCTION-curl-option-if-availabl.patch
# Fix a use-after-free in an example code, in upstream after 0.11.2
Patch2:         libisds-0.11.2-client-sendxmldoc-Fix-a-use-after-free-on-two-places.patch
# Adapt to changes in libxml2-2.12.0, in upstream after 0.11.2
Patch3:         libisds-0.11.2-Fix-building-with-libxml2-2.12.0.patch
# Fix reporting an amount of transferred data, in upstream after 0.11.0
Patch4:         libisds-0.11.2-Fix-using-CURLOPT_XFERINFOFUNCTION-curl-option.patch
# Fix building with curl-8.14.0
Patch5:         libisds-0.11.2-Fix-passing-integers-to-curl_easy_setopt.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
%if %{with libisds_enables_man}
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
%endif
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libxml2-devel
%if %{with libisds_enables_net}
BuildRequires:  libcurl-devel
%endif
%if %{with libisds_enables_openssl}
BuildRequires:  openssl
%else
BuildRequires:  gpgme-devel
BuildRequires:  libgcrypt-devel
%endif
BuildRequires:  make
BuildRequires:  expat-devel >= 2.0.0
# Run-time:
%if !%{with libisds_enables_openssl}
BuildRequires:  gnupg2-smime
%endif
# Tests:
%if %{with libisds_enables_test}
BuildRequires:  glibc-gconv-extra
BuildRequires:  gnutls-devel >= 2.12.0
%endif
%if !%{with libisds_enables_openssl}
Requires:       gnupg2-smime
%endif

%description
This is a library for accessing ISDS (Informační systém datových schránek /
Data Box Information System) SOAP services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-3.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxml2-devel%{?_isa}
Requires:       pkgconfig%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi

%build
%configure \
%if %{with libisds_enables_man}
    --enable-doc \
%else
    --disable-doc \
%endif
    --disable-online-test \
%if %{with libisds_enables_openssl}
    --enable-openssl-backend \
%else
    --disable-openssl-backend \
%endif
    --disable-static \
%if %{with libisds_enables_test}
    --enable-test \
%else
    --disable-test \
%endif
%if %{with libisds_enables_net}
    --with-libcurl \
%else
    --without-libcurl \
%endif
    --enable-curlreauthorizationbug
%{make_build}

%check
make check %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
# Remove multilib unsafe files
rm -rf client/.deps client/Makefile{,.in}

%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS TODO
%{_libdir}/libisds.so.5
%{_libdir}/libisds.so.5.*

%files devel
%{_includedir}/isds.h
%{_libdir}/libisds.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/isds.h.*
%{_mandir}/man3/libisds.*
%doc client

%changelog
%autochangelog
