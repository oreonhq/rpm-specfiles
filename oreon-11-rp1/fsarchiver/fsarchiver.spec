%global source0_hash ade1d9d3c7de815c0b40b54e24e39b53d4a3b0add69d47f23b36fc2fd8f21843
Name:		fsarchiver
Version:	0.8.9
Release:        1%{?dist}
Summary:        Safe and flexible file-system backup/deployment tool
License:	GPL-2.0-only
URL:		http://www.fsarchiver.org
Source0:        https://github.com/fdupoux/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  e2fsprogs
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  libattr-devel
BuildRequires:  libblkid-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libuuid-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
FSArchiver is a system tool that allows you to save the contents of a 
file-system to a compressed archive file. The file-system can be restored 
on a partition which has a different size and it can be restored on a 
different file-system. Unlike tar/dar, FSArchiver also creates the 
file-system when it extracts the data to partitions. Everything is 
checksummed in the archive in order to protect the data. If the archive 
is corrupt, you just lose the current file, not the whole archive.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%{make_build}
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
