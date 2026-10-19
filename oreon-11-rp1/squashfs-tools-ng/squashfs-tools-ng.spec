%global source0_hash ef619b49efb9f792d80c777fdd2d639ed2839da98bffe8b4754c8e5ce61592fb
Name: squashfs-tools-ng
Version: 1.3.2
Summary:        A new set of tools and libraries for working with SquashFS images
URL:	 https://github.com/AgentD/squashfs-tools-ng
Source0:        https://infraroot.at/pub/squashfs/squashfs-tools-ng-%{version}.tar.gz
Release:        1%{?dist}
License: LGPL-3.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND MIT
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libattr-devel
BuildRequires:  libselinux-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains modified utilities for manipulating squashfs filesystems.

%package libs
Summary: The squashfs-tools-ng libsquashfs library
%description libs
The squashfs-tools-ng-libs package contains the libsquashfs
library provided and used by squashfs-tools-ng.

%package devel
Summary: Header files for squashfs-tools-ng development
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The squashfs-tools-ng-devel package contains the header files needed to
develop programs that use the squashfs-tools-ng libsquashfs library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n squashfs-tools-ng-libs -f %{oreon_filedir}/squashfs-tools-ng-libs.list
%files -n squashfs-tools-ng-devel -f %{oreon_filedir}/squashfs-tools-ng-devel.list

%changelog

%autochangelog
