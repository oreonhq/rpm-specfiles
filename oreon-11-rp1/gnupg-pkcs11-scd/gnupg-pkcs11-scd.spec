%global source0_hash 954787e562f2b3d9294212c32dd0d81a2cd37aca250e6685002d2893bb959087
Name:           gnupg-pkcs11-scd
Version:        0.11.0
Release:        1%{?dist}
Summary:        GnuPG-compatible smart-card daemon with PKCS#11 support
License:        BSD-3-Clause
URL:            http://gnupg-pkcs11.sourceforge.net
Source0:        https://github.com/alonbl/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Requires:       openssl
Requires:       pkcs11-helper >= 1.03
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libassuan-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libpkcs11-helper-1)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
gnupg-pkcs11-scd is a drop-in replacement for the smart-card daemon (scd)
shipped with the next-generation GnuPG (gnupg2). The daemon interfaces
with smart-cards by using RSA Security Inc.'s PKCS#11 Cryptographic Token
Interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%{make_build}
%install
%{make_install}
rm -rf ${RPM_BUILD_ROOT}%{_docdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
