%global source1_hash 60493c76fa9b86480ae68dfbb4a3a41bd0a6ce034282acab93fb7794bf1d289b
%global source0_hash fcb25c42f54298ece8b20684fb3c581ed9195a162cbc55180a4161501be93181
Name:		yubico-piv-tool
Version:	2.7.3
Release:        1%{?dist}
Summary:        Tool for interacting with the PIV applet on a YubiKey
License:	BSD-2-Clause
URL:		https://developers.yubico.com/yubico-piv-tool/
Source0:        https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz
Source1:	https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz.sig
Source2:	gpgkey-9588EA0F.gpg
Requires:		pcsc-lite-ccid
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  gnupg2
BuildRequires:  help2man
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.

With it you may generate keys on the device, importing keys and certificates,
and create certificate requests, and other operations. A shared library and
a command-line tool is included.

%package devel
Summary: Tool for interacting with the PIV applet on a YubiKey
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.
This package includes development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup

%build

%cmake \
    -DBUILD_STATIC_LIB=OFF
%cmake_build
%check

%ctest --output-on-failure
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n yubico-piv-tool-devel -f %{oreon_filedir}/yubico-piv-tool-devel.list

%changelog

%autochangelog
