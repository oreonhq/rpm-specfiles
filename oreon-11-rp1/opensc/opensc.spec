# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 976f4a23eaf3397a1a2c3a7aac80bf971a8c3d829c9a79f06145bfaeeae5eca7
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           opensc
Version:        0.27.1
Release:        1%{?dist}
Summary:        Smart card library and applications

License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/OpenSC/OpenSC/wiki
Source0:        https://github.com/OpenSC/OpenSC/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        opensc.module
Patch1:         opensc-0.19.0-pinpad.patch
Patch9:         %{name}-0.27.1-fips-sha1.patch
Patch10:        %{name}-0.27.1-deepbind-workaround.patch
Patch11:        0001-Use-OpenSSL-accessors-for-opaque-structures.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  make
BuildRequires:  pcsc-lite-devel
BuildRequires:  readline-devel
BuildRequires:  openssl-devel
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  clang
%if 0%{?fedora} > 40 || 0%{?rhel} > 10
BuildRequires:  bash-completion-devel
%else
BuildRequires:  bash-completion
%endif
BuildRequires:  zlib-devel
BuildRequires:  libcmocka-devel
BuildRequires:  vim-common
%if ! 0%{?rhel}
BuildRequires:  softhsm
BuildRequires:  openpace-devel
%endif
BuildRequires:  openssl
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pcsc-lite
Obsoletes:      mozilla-opensc-signer < 0.12.0
Obsoletes:      opensc-devel < 0.12.0
Obsoletes:      coolkey <= 1.1.0-36
Provides:       bundled(simclist) = 1.5

%description
OpenSC provides a set of libraries and utilities to work with smart cards. Its
main focus is on cards that support cryptographic operations, and facilitate
their use in security applications such as authentication, mail encryption and
digital signatures. OpenSC implements the PKCS#11 API so applications
supporting this API (such as Mozilla Firefox and Thunderbird) can use it. On
the card OpenSC implements the PKCS#15 standard and aims to be compatible with
every software/card that does so, too.

%package        libs
Requires:       pcsc-lite-libs%{?_isa}
Summary:        OpenSC libraries

%description    libs
OpenSC libraries.

%prep
%oreon_sha256
%autosetup -n opensc-%{version} -p1

XFAIL_TESTS="test-pkcs11-tool-test-threads.sh test-pkcs11-tool-test.sh"

if [[ -f "/proc/sys/crypto/fips_enabled" && $(cat /proc/sys/crypto/fips_enabled) == "1" ]]; then
	XFAIL_TESTS+=" test-pkcs11-tool-unwrap-wrap-test.sh"
fi

sed -i -e "/XFAIL_TESTS/,$ {
  s/XFAIL_TESTS.*/XFAIL_TESTS=$XFAIL_TESTS/
  q
}" tests/Makefile.am

cp -p src/pkcs15init/README ./README.pkcs15init
cp -p src/scconf/README.scconf .
sed -i -e 's|/usr/local/towitoko/lib/|/usr/lib/ctapi/|' etc/opensc.conf.example.in

%build
autoreconf -fvi
%ifarch %{ix86}
sed -i -e 's/opensc.conf/opensc-%{_arch}.conf/g' src/libopensc/Makefile.in
%endif
sed -i -e 's|"/lib /usr/lib\b|"/%{_lib} %{_libdir}|' configure # lib64 rpaths
%set_build_flags
CFLAGS="$CFLAGS -Wstrict-aliasing=2 -Wno-deprecated-declarations"
%configure --disable-static \
  --disable-autostart-items \
  --disable-notify \
  --disable-assert \
  --enable-pcsc \
  --enable-cmocka \
  --enable-sm
%make_build

%check
make check

%install
%make_install
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/p11-kit/modules/opensc.module

%ifarch %{ix86}
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/opensc.conf
install -Dpm 644 etc/opensc.conf $RPM_BUILD_ROOT%{_sysconfdir}/opensc-%{_arch}.conf
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/opensc.conf.5
install -Dpm 644 doc/files/opensc.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/opensc-%{_arch}.conf.5
touch -r NEWS $RPM_BUILD_ROOT%{_sysconfdir}/opensc-%{_arch}.conf
touch -r NEWS $RPM_BUILD_ROOT%{_mandir}/man5/opensc-%{_arch}.conf.5
%else
ln -s %{_sysconfdir}/opensc.conf $RPM_BUILD_ROOT%{_sysconfdir}/opensc-%{_arch}.conf
%endif

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" | xargs rm

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/opensc

rm -f $RPM_BUILD_ROOT%{_libdir}/libopensc.so
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
rm -f $RPM_BUILD_ROOT%{_libdir}/libsmm-local.so

%if 0%{?rhel}
rm -rf %{buildroot}%{_bindir}/npa-tool
rm -rf %{buildroot}%{_mandir}/man1/npa-tool.1*
%endif

rm -rf %{buildroot}%{_bindir}/pkcs11-register
rm -rf %{buildroot}%{_mandir}/man1/pkcs11-register.1*

rm %{buildroot}%{_datadir}/applications/org.opensc.notify.desktop
rm %{buildroot}%{_mandir}/man1/opensc-notify.1*

%files
%doc COPYING NEWS README*

%{_datadir}/bash-completion/*

%{_bindir}/cardos-tool
%{_bindir}/cryptoflex-tool
%{_bindir}/eidenv
%{_bindir}/iasecc-tool
%{_bindir}/gids-tool
%{_bindir}/netkey-tool
%if ! 0%{?rhel}
%{_bindir}/npa-tool
%endif
%{_bindir}/openpgp-tool
%{_bindir}/opensc-explorer
%{_bindir}/opensc-tool
%{_bindir}/opensc-asn1
%{_bindir}/piv-tool
%{_bindir}/pkcs11-tool
%{_bindir}/pkcs15-crypt
%{_bindir}/pkcs15-init
%{_bindir}/pkcs15-tool
%{_bindir}/sc-hsm-tool
%{_bindir}/dnie-tool
%{_bindir}/westcos-tool
%{_bindir}/egk-tool
%{_bindir}/goid-tool
%{_bindir}/dtrust-tool
%{_datadir}/opensc/
%{_mandir}/man1/cardos-tool.1*
%{_mandir}/man1/cryptoflex-tool.1*
%{_mandir}/man1/eidenv.1*
%{_mandir}/man1/gids-tool.1*
%{_mandir}/man1/goid-tool.1*
%{_mandir}/man1/iasecc-tool.1*
%{_mandir}/man1/netkey-tool.1*
%if ! 0%{?rhel}
%{_mandir}/man1/npa-tool.1*
%endif
%{_mandir}/man1/openpgp-tool.1*
%{_mandir}/man1/opensc-explorer.*
%{_mandir}/man1/opensc-tool.1*
%{_mandir}/man1/opensc-asn1.1*
%{_mandir}/man1/piv-tool.1*
%{_mandir}/man1/pkcs11-tool.1*
%{_mandir}/man1/pkcs15-crypt.1*
%{_mandir}/man1/pkcs15-init.1*
%{_mandir}/man1/pkcs15-tool.1*
%{_mandir}/man1/sc-hsm-tool.1*
%{_mandir}/man1/westcos-tool.1*
%{_mandir}/man1/dnie-tool.1*
%{_mandir}/man1/egk-tool.1*
%{_mandir}/man1/dtrust-tool.1*
%{_mandir}/man5/pkcs15-profile.5*

%files libs
%ifarch %{ix86}
%{_mandir}/man5/opensc-%{_arch}.conf.5*
%else
%config(noreplace) %{_sysconfdir}/opensc.conf
%{_mandir}/man5/opensc.conf.5*
%endif

%config(noreplace) %{_sysconfdir}/opensc-%{_arch}.conf
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%{_datadir}/p11-kit/modules/opensc.module
%{_libdir}/lib*.so.*
%{_libdir}/opensc-pkcs11.so
%{_libdir}/pkcs11-spy.so
%{_libdir}/onepin-opensc-pkcs11.so
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/opensc-pkcs11.so
%{_libdir}/pkcs11/onepin-opensc-pkcs11.so
%{_libdir}/pkcs11/pkcs11-spy.so

%if ! 0%{?rhel}
%config(noreplace) %{_sysconfdir}/eac/cvc/DESCHSMCVCA00001
%config(noreplace) %{_sysconfdir}/eac/cvc/DESRCACC100001
%endif

%changelog
%autochangelog
