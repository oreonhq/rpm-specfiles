%global source0_hash 0037cd9b5beb33a6ac58a27712b5fa99da316fc76ff5d8cf3926c3443bef2b78
%global forgeurl https://github.com/adam900710/btrfs-fuse
%global commit 812c4b70c6fd4e2efdd13256c3b5c4a7fd596b2a
%forgemeta
Name:           btrfs-fuse
Version:        0
Release:        1%{?dist}
Summary:        Read-only, license friendly, FUSE based btrfs implementation
License:        GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  btrfs-progs-devel
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libb2-devel
BuildRequires:  liburing-devel
BuildRequires:  libuuid-devel
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  xfsprogs-devel
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This is a read-only btrfs implementation using FUSE (Filesystem in Userspace).

Although btrfs is already in mainline Linux kernel, there are still use-cases
for such read-only btrfs implementation:
- Educational purpose: let new developers get a quick way to learn how a
  complex and modern filesystem works;
- For certain bootloaders: certain bootloaders need code base compatible with
  their license;
- As a last resort method for subpage/multipage support: currently (v5.16-rc)
  the Linux kernel can only support sectorsize == pagesize , and 4K sectorsize
  with 64K page size; thus this project can act as a last resort method to read
  data from filesystem with unsupported sectorsize.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
