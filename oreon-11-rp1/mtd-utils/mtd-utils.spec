%global source0_hash f7ae20b2eb79ee83441468f0b99d897024cd96ff853eea59106fb1952065c803
Name:    mtd-utils
Version: 2.2.1
Release:        1%{?dist}
License: GPL-2.0-or-later
Summary:        Utilities for dealing with MTD (flash) devices
URL:     http://www.linux-mtd.infradead.org/
Source0:        ftp://ftp.infradead.org/pub/mtd-utils/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
The mtd-utils package contains utilities related to handling MTD devices,
and for dealing with FTL, NFTL JFFS2 etc.

%package ubi
Summary: Utilities for dealing with UBI
%description ubi
The mtd-utils-ubi package contains utilities for manipulating UBI on 
MTD (flash) devices.

%package tests
Summary: Test utilities for mtd-utils
%description tests
Various test programs related to mtd-utils

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%{make_build}
%install
%{make_install}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mtd-utils-ubi -f %{oreon_filedir}/mtd-utils-ubi.list
%files -n mtd-utils-tests -f %{oreon_filedir}/mtd-utils-tests.list

%changelog

%autochangelog
