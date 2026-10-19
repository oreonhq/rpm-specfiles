%global source0_hash a24a02e26abc4055a190e7f14c207cec2853eada77485184835c0b220a71d385
Name:           R-openssl
Version:        %R_rpm_version 2.3.4
Release:        1%{?dist}
Summary:        Toolkit for Encryption, Signatures and Certificates Based on OpenSSL
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=openssl&version=%{version}#/openssl_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
Bindings to OpenSSL libssl and libcrypto, plus custom SSH key parsers.
Supports RSA, DSA and EC curves P-256, P-384, P-521, and curve25519.
Cryptographic signatures can either be created and verified manually or via
x509 certificates. AES can be used in cbc, ctr or gcm mode for symmetric
encryption; RSA for asymmetric (public key) encryption or EC for Diffie
Hellman. High-level envelope functions combine RSA and AES for encrypting
arbitrary sized data. Other utilities include key generators, hash functions
(md5, sha1, sha256, etc), base64 encoder, a secure random number generator, and
'bignum' math methods for manually performing crypto calculations on large
multibyte integers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f openssl/tests/testthat/test_google.R # network

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

export OPENSSL_ENABLE_SHA1_SIGNATURES=1
%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
