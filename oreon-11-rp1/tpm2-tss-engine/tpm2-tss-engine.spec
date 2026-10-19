%global source0_hash 3c94fef110dd3630b3c28c5875febba76b7d5ba2fcc04a14c4a30f5d2157c265
%global         build_type_safety_c 2
Name:           tpm2-tss-engine
Version:        1.2.0
Release:        1%{?dist}
Summary:        OpenSSL Engine for TPM2 devices using the tpm2-tss software stack
License:        BSD-3-Clause
URL:            https://github.com/tpm2-software/tpm2-tss-engine
Source0:        https://github.com/tpm2-software/tpm2-tss-engine/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires:       openssl 
Requires:       tpm2-tss
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  tpm2-tss-devel
# /oreon:deps
%description
tpm2-tss-engine is an engine implementation for OpenSSL that uses tpm2-tss 
software stack. It uses the Enhanced System API (ESAPI) interface of the
TSS 2.0 for downwards communication. It supports RSA decryption and signatures
as well as ECDSA signatures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package devel
Summary:  Headers and libraries for building applications against tpm2-tss-engine
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
This package contains headers and libraries for building apps applications
against tpm2-tss-engine

%package utilities
Summary:  Utility binary for openssl using tpm2-tss software stack
Requires: %{name}%{_isa} = %{version}-%{release}
%description utilities
This package contains the binary of the engine implementation for openssl that
uses the tpm2-tss software stack

%files -f %{oreon_filedir}/main.list
%files -n tpm2-tss-engine-devel -f %{oreon_filedir}/tpm2-tss-engine-devel.list
%files -n tpm2-tss-engine-utilities -f %{oreon_filedir}/tpm2-tss-engine-utilities.list

%changelog

%autochangelog
