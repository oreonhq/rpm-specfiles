# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6b027b396cfdea32343515ada5ea08a18b7c2366de3ac1a105b2e37d83c938ab
%global source3_hash 736b467530f916737b7031310ccb21d8218c6229e61e8e160cd1d3458cd543a8
%global source5_hash 2f04c5619fc27480558a8369cbe208b4aca1e5ae4131955a9e72a8208e1adb3e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond check 1
%bcond gpgcheck 1

%global osslver 4.0.2
%global features fips,nssdb,ossl400

%global srpmhash() %{lua:
local files = rpm.expand("%_specdir/fips-provider.spec")
for i, p in ipairs(patches) do
   files = files.." "..p
end
for i, p in ipairs(sources) do
   files = files.." "..p
end
local sha256sum = assert(io.popen("cat "..files.." 2>/dev/null | sha256sum"))
local hash = sha256sum:read("*a")
sha256sum:close()
print(string.sub(hash, 0, 16))
}

Name:           fips-provider
Version:        1.5.3
Release:        1%{?dist}
Summary:        A FIPS provider built from the Kryoptic project

SourceLicense:        GPL-3.0-or-later and Apache-2.0
License: Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND GPL-3.0-or-later AND ISC AND MIT AND (MIT-0 OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib

URL:            https://github.com/latchset/kryoptic
Source0:        https://github.com/latchset/kryoptic/releases/download/v%{version}/kryoptic-%{version}.tar.gz
%if %{with gpgcheck}
Source1:        kryoptic-1.5.3.tar.gz.asc
Source2:        simo_oreon.asc
%endif
Source3:        https://github.com/openssl/openssl/releases/download/openssl-4.0.2/openssl-4.0.2.tar.gz
Source4:        fips-hmacify.sh
Source5:        kryoptic-%{version}-vendor.tar.xz
Source6:        kryoptic-%{version}-Cargo.lock

Patch105:        0001-Remove-bundled-rusqlite-from-fips-feature.patch
Patch106:        548.patch
Patch200:        openssl-4.0.2-kryoptic.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  rustc
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  zlib-devel
BuildRequires:  /usr/bin/cmp
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Pod::Html)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(bigint)
%if %{with gpgcheck}
BuildRequires:  gnupg2
%endif

Provides:       fips-provider-so
Provides:       bundled(openssl) = %{osslver}

%description
This package provides a cryptographic module that is both an OpenSSL provider
as well as a PKCS#11 software token.

%files
%attr(0755,root,root) %{_libdir}/pkcs11
%attr(0755,root,root) %{_libdir}/ossl-modules
%{_libdir}/ossl-modules/fips.so
%{_libdir}/pkcs11/fipstokn.so
%license LICENSE.txt
%license LICENSE.dependencies

%prep
%oreon_sha256
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -

%if %{with gpgcheck}
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%endif

%setup -n kryoptic-%{version} -q
%autopatch -p1 -M 199
cp -a %{SOURCE6} Cargo.lock
tar -xf %{SOURCE5}
%oreon_cargo_prep vendor
%setup -n kryoptic-%{version} -q -T -D -a 3

pushd openssl-%{osslver}
%autopatch -p1 -m 200
popd

%build
sslarch=%{_os}-%{_target_cpu}
%ifarch x86_64
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch s390x
sslarch="linux64-s390x"
sslflags=no-ec_nistp_64_gcc_128
%endif
%ifarch aarch64
sslarch="linux-aarch64"
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch ppc64le
sslarch="linux-ppc64le"
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch %ix86
sslarch=linux-elf
%endif

RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS -Wl,--allow-multiple-definition"

pushd openssl-%{osslver}

./Configure \
    --prefix=%{_prefix} --openssldir=%{_sysconfdir}/pki/tls \
    ${sslflags} ${sslarch} enable-fips \
    no-deprecated no-engine no-legacy no-tests \
    no-atexit no-comp no-egd no-static-engine no-ui-console \
    no-dgram no-http no-ssl no-ssl-trace no-sock no-srtp \
    no-dtls no-dtls1-method no-dtls1_2-method \
    no-tls no-tls1-method no-tls1_1-method no-tls1_2-method \
    no-aria no-argon2 no-blake2 no-camellia no-cast no-chacha \
    no-des no-dsa no-ec2m no-gost no-idea no-ktls no-mdc2 \
    no-md4 no-poly1305 no-rc2 no-rc4 no-rc5 no-rmd160 no-seed no-siphash \
    no-sm2 no-sm2-precomp no-sm3 no-sm4 no-whirlpool \
    -DDEVRANDOM='"\"/dev/urandom\""' \
    -DOPENSSL_PEDANTIC_ZEROIZATION \
    -DKRYOPTIC_FIPS_VENDOR='"\"Kryoptic FIPS Provider\""' \
    -DKRYOPTIC_FIPS_VERSION='"\"%{version}\""' \
    -DKRYOPTIC_FIPS_BUILD='"\"%{srpmhash}\""'

perl configdata.pm --dump

make -s %{?_smp_mflags} all

popd

export CARGO_HOME=%{_builddir}/cargo-home
mkdir -p "$CARGO_HOME"
export KRYOPTIC_OPENSSL_SOURCES=${PWD}/openssl-%{osslver}
%oreon_cargo_build --no-default-features --features %{features}
(
  printf 'Vendored crate list\n\n'
  ls -1 vendor | sort
) > LICENSE.dependencies

%if %{with check}
%check
export CARGO_HOME=%{_builddir}/cargo-home
export KRYOPTIC_OPENSSL_SOURCES=${PWD}/openssl-%{osslver}
%oreon_cargo_test --no-default-features --features %{features}
%endif

%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    pushd openssl-%{osslver} \
    %{SOURCE4} $RPM_BUILD_ROOT/%{_libdir}/ossl-modules/fips.so \
%{nil}

%install
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/ossl-modules
install -m755 target/release/libkryoptic_pkcs11.so $RPM_BUILD_ROOT/%{_libdir}/ossl-modules/fips.so
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/pkcs11
ln -s ../ossl-modules/fips.so $RPM_BUILD_ROOT%{_libdir}/pkcs11/fipstokn.so
