%global source0_hash 2d05e9ecc3cabb249c79662f83bbc9835ac0d53bd4c304824c18b9b7597462fa
%global commit 9781ff1b3327cff25070a26a95f93992d13a3ffd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:          openvpn-otp
Version:       1.0^20241013git%{shortcommit}
Release:        1%{?dist}
Summary:        OpenVPN OTP authentication support
License:       GPL-1.0-or-later AND Apache-2.0 AND Apache-1.0 AND APSL-2.0
URL:           https://github.com/evgeny-gridasov/%{name}
Source0:        https://github.com/evgeny-gridasov/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Requires: openvpn >= 2.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openvpn-devel
BuildRequires:  sed
# /oreon:deps
%description
This plug-in adds support for time based OTP (totp) and HMAC based OTP (hotp)
tokens for OpenVPN. Compatible with Google Authenticator software token, other
software and hardware based OTP tokens.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}
sed -n -e '/@APPLE_LICENSE_HEADER_START@/,/@APPLE_LICENSE_HEADER_END@/p' < src/base64.c > base64_copyright
install -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build

./autogen.sh
%configure --with-openvpn-plugin-dir=%{_libdir}/openvpn/plugins/
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/openvpn/plugins/*.la
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
