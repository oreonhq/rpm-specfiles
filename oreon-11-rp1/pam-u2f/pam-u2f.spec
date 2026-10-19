%global source1_hash 46a194fb05e99531738c0150bc5afb986326622a17ad784c0b94eb365755094d
%global source0_hash a59927cea38ea8d91a6836a04e20fc629edde4204b16082f703f6db378e9c634
Name:          pam-u2f
Version:       1.4.0
Release:        1%{?dist}
Summary:        Implements PAM authentication over U2F
License:       BSD-2-Clause
URL:           https://github.com/Yubico/pam-u2f
Source0:        https://developers.yubico.com/pam-u2f/Releases/pam_u2f-%{version}.tar.gz
Source1:       https://developers.yubico.com/pam-u2f/Releases/pam_u2f-%{version}.tar.gz.sig
Source2:       yubico-release-gpgkeys.asc
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(pam)
# /oreon:deps
%description
The PAM U2F module provides an easy way to integrate the Yubikey (or
other U2F-compliant authenticators) into your existing user
authentication infrastructure.

%package -n pamu2fcfg
Summary:       Configures PAM authentication over U2F
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description -n pamu2fcfg
pamu2fcfg provides a command line tool for configuring PAM authentication
over U2F.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n pam_u2f-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles pamu2fcfg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n pamu2fcfg -f %{oreon_filedir}/pamu2fcfg.list

%changelog

%autochangelog
