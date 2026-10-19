%global source0_hash 63d02788852644d871746e1a7a1d16c272c583c226f62576f5ad232a6a44e18c
Name:           pam_yubico
Version:        2.27
Release:        10%{?dist}
Summary:        A Pluggable Authentication Module for yubikeys
License:        LicenseRef-Callaway-BSD
URL:            https://developers.yubico.com/yubico-pam/
Source0:        https://developers.yubico.com/yubico-pam/Releases/pam_yubico-%{version}.tar.gz
Requires:       pam
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libyubikey-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  ykclient-devel
BuildRequires:  ykpers-devel
# /oreon:deps
%description
This is pam_yubico, a pluggable authentication module that can be used with
Linux-PAM and yubikeys. This module supports yubikey OTP checking.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoconf
%configure --libdir=/%{_lib} \
           --with-pam-dir=/%{_lib}/security/ \
           --disable-rpath
%make_build
%install
%make_install
rm $RPM_BUILD_ROOT/%{_lib}/security/pam_yubico.la
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
