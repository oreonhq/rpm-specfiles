%global source0_hash 547b7b7f4d2e44bf91b6fc554664850c69563701deab9fd9cd7e21f694c88ea6
Name: squashfs-tools
Version: 4.7.5
Summary:        Utility for the creation of squashfs filesystems
%global forgeurl https://github.com/plougher/%{name}
%global tag %{version}
%forgemeta
URL:	 %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Release:        1%{?dist}
License: GPL-2.0-or-later
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libattr-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains the utilities for manipulating squashfs filesystems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgesetup

%build

%set_build_flags
pushd squashfs-tools
CFLAGS="%optflags" XZ_SUPPORT=1 LZO_SUPPORT=1 LZMA_XZ_SUPPORT=1 LZ4_SUPPORT=1 ZSTD_SUPPORT=1 make %{?_smp_mflags}
%install
pushd squashfs-tools
make INSTALL_PREFIX=%{buildroot}/usr INSTALL_DIR=%{buildroot}%{_sbindir} INSTALL_MANPAGES_DIR=%{buildroot}%{_mandir}/man1 install
%oreon_autofiles main

%check

[[ $(squashfs-tools/mksquashfs -version) =~ "%{version}" ]]
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
