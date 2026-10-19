%global source0_hash 34634c8add651f1e796f50e4e9c6c69f5c3377c724ae61656f73e0f482bcf995
Name:          openssl-pkcs11-sign-provider
Version:       1.0.2
Release:        1%{?dist}
Summary:        A PKCS#11 provider for OpenSSL 3.0 (private key operations only)
License:       Apache-2.0
URL:           https://github.com/opencryptoki/%{name}
Source0:        https://github.com/opencryptoki/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires:      openssl >= 3.0.8
# oreon:deps
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  gnutls-utils
BuildRequires:  libtool
BuildRequires:  opencryptoki
BuildRequires:  opencryptoki-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  sed
# /oreon:deps
%description
This package contains a provider module for OpenSSL 3.0, interfacing to
PKCS#11 for operations with private keys in PKCS#11 tokens.

%global modulesdir %(pkg-config --variable=modulesdir libcrypto)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --libdir=%{modulesdir}
%make_build
for file in openssl-*.cnf.sample; do mv $file $file.%{_arch}; done
%check

%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
