# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash be14a5820ec457eac5154462ffae51ba5d8a643f6760514d4b4b83a77be91573

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global _lto_cflags %{nil}

%global origname SoftHSMv2

Name:           softhsm
Version:        2.7.0
Release:        1%{?dist}
Summary:        Software version of a PKCS#11 Hardware Security Module
License:        BSD-2-Clause
URL:            https://www.softhsm.org/
Source0:        https://github.com/softhsm/SoftHSMv2/archive/refs/tags/%{version}/%{origname}-%{version}.tar.gz
Source1:        %{name}-sysusers.conf
Patch0:         memory-leaks-and-openssl-4.patch
Patch1:         prevent-global-deleted-objects-access.patch
Patch2:         softhsm-skip-unsupported-crypto-tests.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel >= 1.0.1k-6
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel >= 3.4.2
BuildRequires:  systemd-rpm-macros

%{?sysusers_requires_compat}
Requires:       p11-kit
Requires:       openssl-libs >= 1.0.1k-6

%description
SoftHSM is a software implementation of a generic cryptographic device with
a PKCS#11 interface. It was designed to meet the requirements of OpenDNSSEC,
but can also work together with other cryptographic products because of the
PKCS#11 interface.

%package devel
Summary:        Development files for softhsm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel
Requires:       sqlite-devel

%description devel
The devel package contains the libsofthsm include files.

%prep
%oreon_sha256
%autosetup -p1 -n %{origname}-%{version}
sed -i 's:^full_libdir=":#full_libdir=":g' configure.ac
autoreconf -fiv

%build
%configure \
    --libdir=%{_libdir}/pkcs11 \
    --with-openssl=%{_prefix} \
    --enable-ecc \
    --enable-eddsa \
    --disable-gost \
    --with-migrate \
    --enable-visibility \
    --with-p11-kit=%{_datadir}/p11-kit/modules/
%make_build

%install
%make_install

install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

rm -f %{buildroot}%{_sysconfdir}/softhsm2.conf.sample
rm -f %{buildroot}%{_libdir}/pkcs11/*.la
mkdir -p %{buildroot}%{_includedir}/softhsm
cp -p src/lib/*.h %{buildroot}%{_includedir}/softhsm
mkdir -p %{buildroot}%{_sharedstatedir}/softhsm/tokens

mkdir -p %{buildroot}%{_libdir}/softhsm
ln -s ../pkcs11/libsofthsm2.so %{buildroot}%{_libdir}/softhsm/libsofthsm.so
ln -s pkcs11/libsofthsm2.so %{buildroot}%{_libdir}/libsofthsm2.so

%check
for d in crypto data_mgr handle_mgr object_store session_mgr slot_mgr; do
    make check -C src/lib/$d
done

pushd src/lib/test
make p11test
for t in TokenTests AsymWrapUnwrapTests DigestTests ForkTests \
         InitTests InfoTests SessionTests UserTests RandomTests \
         SignVerifyTests AsymEncryptDecryptTests DeriveTests \
         ObjectTests SymmetricAlgorithmTests; do
    ./p11test $t
done
popd

%pre
%sysusers_create_compat %{SOURCE1}

%triggerpostun -- softhsm < 2.0.0
if [ -f /var/softhsm/slot0.db ]; then
    runuser -g ods ods -c 'softhsm2-migrate --db /var/softhsm/slot0.db --pin 1234 --slot 0' || :
fi

%files
%license LICENSE
%doc README.md NEWS
%config(noreplace) %{_sysconfdir}/softhsm2.conf
%{_bindir}/*
%dir %{_libdir}/softhsm
%{_libdir}/pkcs11/libsofthsm2.so
%{_libdir}/libsofthsm2.so
%{_libdir}/softhsm/libsofthsm.so
%attr(0664,root,root) %{_datadir}/p11-kit/modules/softhsm2.module
%attr(0750,ods,ods) %dir %{_sharedstatedir}/softhsm
%attr(1770,ods,ods) %dir %{_sharedstatedir}/softhsm/tokens
%{_mandir}/*/*
%{_sysusersdir}/%{name}.conf

%files devel
%attr(0755,root,root) %dir %{_includedir}/softhsm
%{_includedir}/softhsm/*.h

%changelog
%autochangelog
