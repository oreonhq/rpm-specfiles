%global source0_hash c67bf5de8fc21617545ac2f3d63e7d3e0b872d611948c26535a9032987c3a7af

%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name:       nss-pem
Version:    1.1.1
Release:    3%{?dist}
Summary:    PEM file reader for Network Security Services (NSS)

# See README for details
# list.h - GPL-2.0-only
# *      - MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
License:    GPL-2.0-only AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:        https://github.com/kdudka/nss-pem
Source0:    https://github.com/kdudka/nss-pem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/kdudka/nss-pem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc

# gpg --keyserver pgp.mit.edu --recv-key 992A96E075056E79CD8214F9873DB37572A37B36
# gpg --output kdudka.pgp --armor --export kdudka@redhat.com
Source2:    kdudka.pgp

BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: make
BuildRequires: nss-pkcs11-devel

# require at least the version of nss that nss-pem was built against (#1428965)
Requires: nss%{?_isa} >= %(nss-config --version 2>/dev/null || echo 0)

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

%check
%ctest3

%files
%{_libdir}/libnsspem.so
%license COPYING.{GPL,MPL}

%changelog
%autochangelog
