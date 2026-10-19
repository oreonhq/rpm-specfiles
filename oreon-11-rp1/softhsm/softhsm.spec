%global source0_hash 8e992b042fd7d64a4984bc104f4ce0da017d12785f4b437f2e39333702b0e542
%global prever rc1
%global origname SoftHSMv2
Summary:        Software version of a PKCS#11 Hardware Security Module
Name: softhsm
Version: 2.7.0
Release:        1%{?dist}
License: BSD-2-clause
Url: http://www.softhsm.org/
Source0:        https://github.com/%{name}/%{origname}/archive/refs/tags/%{version}-%{prever}.tar.gz#/%{origname}-%{version}-%{prever}.tar.gz
Source2: %{name}-sysusers.conf
Requires(pre): shadow-utils
Requires: p11-kit
Requires: openssl-libs >= 1.0.1k-6
%global _hardened_build 1
%global softhsm_module "SoftHSM PKCS #11 Module"
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
mkdir -p %{buildroot}/%{_libdir}/softhsm/
ln -s ../pkcs11/libsofthsm2.so %{buildroot}/%{_libdir}/softhsm/libsofthsm.so
( cd  %{buildroot}/%{_libdir} ; ln -s pkcs11/libsofthsm2.so)
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%pre

%sysusers_create_package %{name} %{SOURCE2}
%post

%triggerpostun -- softhsm < 2.0.0

if [ -f /var/softhsm/slot0.db ]; then
      runuser -g ods ods -c 'softhsm2-migrate --db /var/softhsm/slot0.db --pin 1234 --slot 0' || :
fi
%files -f %{oreon_filedir}/main.list
%files -n softhsm-devel -f %{oreon_filedir}/softhsm-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-1
- Prepare for Oreon 11 (RP1)
