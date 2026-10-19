%global source0_hash 976f4a23eaf3397a1a2c3a7aac80bf971a8c3d829c9a79f06145bfaeeae5eca7
Name:           opensc
Version:        0.27.1
Release:        1%{?dist}
Summary:        Smart card library and applications
License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/OpenSC/OpenSC/wiki
Source0:        https://github.com/OpenSC/OpenSC/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        opensc.module
Patch1:         opensc-0.19.0-pinpad.patch
Patch8:         %{name}-0.22.0-file-cache.patch
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pcsc-lite
Obsoletes:      mozilla-opensc-signer < 0.12.0
Obsoletes:      opensc-devel < 0.12.0
Obsoletes:      coolkey <= 1.1.0-36
Provides:       bundled(simclist) = 1.5
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash-completion
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  libcmocka-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  readline-devel
BuildRequires:  vim-common
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch 1 -p1 -b .pinpad
%patch 8 -p1 -b .file-cache

XFAIL_TESTS="test-pkcs11-tool-test-threads.sh test-pkcs11-tool-test.sh"

# In FIPS mode, OpenSSL doesn't allow RSA-PKCS, this is hardcoded into OpenSSL
# and we cannot influence it. Hence, the test is expected to fail in FIPS mode.
if [[ -f "/proc/sys/crypto/fips_enabled" && $(cat /proc/sys/crypto/fips_enabled) == "1" ]]; then
	XFAIL_TESTS+=" test-pkcs11-tool-unwrap-wrap-test.sh"
fi

sed -i -e "/XFAIL_TESTS/,$ {
  s/XFAIL_TESTS.*/XFAIL_TESTS=$XFAIL_TESTS/
  q
}" tests/Makefile.am

cp -p src/pkcs15init/README ./README.pkcs15init
cp -p src/scconf/README.scconf .
# No {_libdir} here to avoid multilib conflicts; it's just an example
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
rm -rf %{buildroot}%{_bindir}/pkcs11-register
rm -rf %{buildroot}%{_mandir}/man1/pkcs11-register.1*
rm %{buildroot}%{_datadir}/applications/org.opensc.notify.desktop
rm %{buildroot}%{_mandir}/man1/opensc-notify.1*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n opensc-libs -f %{oreon_filedir}/opensc-libs.list

%changelog

%autochangelog
