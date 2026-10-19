%global source0_hash c3c111baa184acaab34dd590ef874f7e5d41e36d216ad1af49837b9e320a0eb4
%global enginesdir %(pkg-config --variable=enginesdir libcrypto)
Name:           p11-remote
Version:        0.3
Release:        1%{?dist}
Summary:        Remoting of PKCS#11 modules across sessions
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/NetworkManager/%{name}
Source0:        https://github.com/NetworkManager/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires:       openssl-libs
Requires:       p11-kit-server
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel-engine(x86-64)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(systemd)
# /oreon:deps
%description
This is a PKCS#11 engine for OpenSSL based on p11-kit capable of utilizing the
p11-kit remoting capabilities. It also includes an on-demand activated UNIX
socket based p11-kit server for user sessions.

This is in particular useful to use a GNOME Keyring software HSM with daemons
running outside the user session, such as the NetworkManager managed VPN
daemons or wpa_supplicant.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%post

%systemd_user_post p11-kit-remote.socket
%preun

%systemd_user_preun p11-kit-remote.socket
%triggerun -- %{name} < 0.3-7

systemctl --no-reload preset --global p11-kit-remote.socket >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
