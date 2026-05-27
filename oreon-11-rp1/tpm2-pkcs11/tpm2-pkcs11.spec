%global source0_hash none

#global candidate RC0

Name:		tpm2-pkcs11
Version:	1.9.1
Release:	7%{?candidate:.%{candidate}}%{?dist}
Summary:	PKCS#11 interface for TPM 2.0 hardware

License:	BSD-2-Clause
URL:		https://github.com/tpm2-software/tpm2-pkcs11
Source0:	https://github.com/tpm2-software/%{name}/releases/download/%{version}%{?candidate:-%{candidate}}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz
Source1:	https://github.com/tpm2-software/%{name}/releases/download/%{version}%{?candidate:-%{candidate}}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz.asc
# William Roberts (Bill Roberts) key from pgp.mit.edu
Source2:	gpgkey-8E1F50C1.gpg

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	python3
BuildRequires:	libgcrypt-devel
BuildRequires:	libyaml-devel
BuildRequires:	openssl-devel
BuildRequires:	p11-kit-devel
BuildRequires:	sqlite-devel
BuildRequires:	tpm2-tools
BuildRequires:	tpm2-tss-devel
BuildRequires:	tpm2-abrmd-devel
# for tools
BuildRequires:	python3-devel
# for tests
BuildRequires:	libcmocka-devel
BuildRequires:	dbus-daemon
# for tarball signature verification
BuildRequires:	gnupg2

%description
PKCS #11 is a Public-Key Cryptography Standard that defines a standard method
to access cryptographic services from tokens/ devices such as hardware security
modules (HSM), smart cards, etc. In this project we intend to use a TPM2 device
as the cryptographic token.

%package devel
Summary:        Headers and libraries for building apps that use TPM2 for PKCS#11
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
This package contains headers and libraries required to build applications that
use TPM2 for PKCS#11.

%package tools
Summary: The tools required to setup and configure TPM2 for PKCS#11

%description tools
The tools required to setup and configure TPM2 for PKCS#11.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}
%if 0%{?rhel}
# not available in RHEL
sed -i -e "/'bcrypt',/d" tools/setup.py
%endif


%generate_buildrequires
pushd tools >&2
%pyproject_buildrequires
popd >&2


%build
%configure --enable-unit --with-fapi=yes
%{make_build}
pushd tools
%pyproject_wheel
popd


%install
%make_install
mkdir $RPM_BUILD_ROOT/%{_includedir}/
install src/pkcs11.h $RPM_BUILD_ROOT/%{_includedir}/
[ -f $RPM_BUILD_ROOT%{_libdir}/pkcs11/libtpm2_pkcs11.la ] && \
  rm $RPM_BUILD_ROOT%{_libdir}/pkcs11/libtpm2_pkcs11.la
[ -f $RPM_BUILD_ROOT%{_libdir}/pkcs11/libtpm2_pkcs11.a ] && \
  rm $RPM_BUILD_ROOT%{_libdir}/pkcs11/libtpm2_pkcs11.a

pushd tools
%pyproject_install
install -Dpm 755 tpm2_ptool $RPM_BUILD_ROOT%{_bindir}/tpm2_ptool
popd


%check
make check


%files
%license LICENSE
%{_datadir}/p11-kit/modules/tpm2_pkcs11.module
%%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/libtpm2_pkcs11.so
%{_libdir}/pkcs11/libtpm2_pkcs11.so.0*

%files devel
%{_libdir}/pkgconfig/tpm2-pkcs11.pc
%{_includedir}/pkcs11.h

%files tools
%{_bindir}/tpm2_ptool
%{python3_sitelib}/tpm2_pkcs11/*
%{python3_sitelib}/tpm2_pkcs11_tools-*.dist-info/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.1-7
- Prepare for Oreon 11 (RP1)
