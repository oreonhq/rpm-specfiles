%global source1_hash dfa11a2043e8f0192f52ad2ab1de862a95a1469e23e737f8d851d9e825e4797a
%global source0_hash c67bf5de8fc21617545ac2f3d63e7d3e0b872d611948c26535a9032987c3a7af
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build
Name:       nss-pem
Version:    1.1.1
Release:        3%{?dist}
Summary:        PEM file reader for Network Security Services (NSS)
License:    GPL-2.0-only AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:        https://github.com/kdudka/nss-pem
Source0:        https://github.com/kdudka/nss-pem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/kdudka/nss-pem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:    kdudka.pgp
Requires: nss%{?_isa} >= %(nss-config --version 2>/dev/null || echo 0)
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  nss-pkcs11-devel
# /oreon:deps
%description
PEM file reader for Network Security Services (NSS), implemented as a PKCS#11
module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build

%cmake3 -S src
%cmake3_build
%install
%cmake3_install
%oreon_autofiles main

%check

%ctest3
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
