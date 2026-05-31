%global source0_hash none

%global prever rc1
#global prerelease yes
%global origname SoftHSMv2

Summary: Software version of a PKCS#11 Hardware Security Module
Name: softhsm
Version: 2.7.0
Release: %{?prever:0.}1%{?prever:.%{prever}}%{?dist}.1
License: BSD-2-clause
# Upstream moved to a separate namespace from OpenDNSSEC
Url: http://www.softhsm.org/
Source:        https://github.com/softhsm/SoftHSMv2/archive/refs/tags/%{version}%{?prever:-%prever}/%{origname}-%{version}%{?prever:-%prever}.tar.gz
Source2: %{name}-sysusers.conf

BuildRequires: make
BuildRequires: openssl-devel >= 1.0.1k-6, sqlite-devel >= 3.4.2, cppunit-devel
BuildRequires: gcc-c++, pkgconfig, p11-kit-devel
BuildRequires: systemd-rpm-macros

Requires(pre): shadow-utils
Requires: p11-kit
Requires: openssl-libs >= 1.0.1k-6

%global _hardened_build 1

%global softhsm_module "SoftHSM PKCS #11 Module"

%description
OpenDNSSEC is providing a software implementation of a generic
cryptographic device with a PKCS#11 interface, the SoftHSM. SoftHSM is
designed to meet the requirements of OpenDNSSEC, but can also work together
with other cryptographic products because of the PKCS#11 interface.

%package devel
Summary: Development package of softhsm that includes the header files
Requires: %{name} = %{version}-%{release}, openssl-devel, sqlite-devel
%if 0%{?prever:1} || 0%{?prerelease:1}
BuildRequires: autoconf, libtool, automake
%endif

%description devel
The devel package contains the libsofthsm include files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{origname}-%{version}%{?prever:-%prever}

%if 0%{?prever:1} || 0%{?prerelease:1}
   # pre-release or post-release snapshots fixup
   sed -i 's:^full_libdir=":#full_libdir=":g' configure.ac
autoreconf -fiv
%else
   # remove softhsm/ subdir auto-added to --libdir
   sed -i 's:full_libdir/softhsm:full_libdir:g' configure
%endif

%build
# This package fails its testsuite with LTO enabled and needs further
# investigation
%define _lto_cflags %{nil}

%configure --libdir=%{_libdir}/pkcs11 --with-openssl=%{_prefix} --enable-ecc --enable-eddsa --disable-gost \
           --with-migrate --enable-visibility --with-p11-kit=%{_datadir}/p11-kit/modules/

%make_build

%check
for d in crypto data_mgr handle_mgr object_store session_mgr slot_mgr ; do
make check  -C src/lib/$d
done

pushd src/lib/test
make p11test
for t in TokenTests AsymWrapUnwrapTests DigestTests ForkTests \
         InitTests InfoTests SessionTests UserTests RandomTests \
         SignVerifyTests AsymEncryptDecryptTests DeriveTests \
         ObjectTests SymmetricAlgorithmTests ; do
./p11test $t
done
popd

%install
rm -rf %{buildroot}
%make_install

install -D %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

rm %{buildroot}/%{_sysconfdir}/softhsm2.conf.sample
rm -f %{buildroot}/%{_libdir}/pkcs11/*a
mkdir -p %{buildroot}%{_includedir}/softhsm
cp src/lib/*.h %{buildroot}%{_includedir}/softhsm
mkdir -p %{buildroot}/%{_sharedstatedir}/softhsm/tokens

# leave a softlink where softhsm-1 installed its library. Programs like
# opendnssec have that filename in their configuration file.
mkdir -p %{buildroot}/%{_libdir}/softhsm/
ln -s ../pkcs11/libsofthsm2.so %{buildroot}/%{_libdir}/softhsm/libsofthsm.so
# rhbz#1272423 NSS needs it to be in the search path too
( cd  %{buildroot}/%{_libdir} ; ln -s pkcs11/libsofthsm2.so)

%files
%config(noreplace) %{_sysconfdir}/softhsm2.conf
%{_bindir}/*
%dir %{_libdir}/softhsm
%{_libdir}/pkcs11/libsofthsm2.so
%{_libdir}/libsofthsm2.so
%{_libdir}/softhsm/libsofthsm.so
%attr(0664,root,root) %{_datadir}/p11-kit/modules/softhsm2.module
%attr(0750,ods,ods) %dir %{_sharedstatedir}/softhsm
%attr(1770,ods,ods) %dir %{_sharedstatedir}/softhsm/tokens
%doc LICENSE README.md NEWS
%{_mandir}/*/*
%{_sysusersdir}/%{name}.conf

%files devel
%attr(0755,root,root) %dir %{_includedir}/softhsm
%{_includedir}/softhsm/*.h

%pre

%sysusers_create_package %{name} %{SOURCE2}

%post

%triggerpostun -- softhsm < 2.0.0
if [ -f /var/softhsm/slot0.db ]; then
      runuser -g ods ods -c 'softhsm2-migrate --db /var/softhsm/slot0.db --pin 1234 --slot 0' || :
fi

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-1
- Prepare for Oreon 11 (RP1)
