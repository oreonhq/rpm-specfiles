%global source0_hash f7cd059e70fc57e888db282c622ec050c0dcdbaacc65e3c1eb163cd9d92d810d

Name:		fsarchiver
Version:	0.8.7
Release:	3%{?dist}
Summary:	Safe and flexible file-system backup/deployment tool

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://www.fsarchiver.org
Source0:	https://github.com/fdupoux/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	e2fsprogs-devel => 1.41.4
BuildRequires:	libuuid-devel
BuildRequires:	libblkid-devel
BuildRequires:	e2fsprogs
BuildRequires:	libattr-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	lzo-devel
BuildRequires:	xz-devel
BuildRequires:	lz4-devel
BuildRequires:	libzstd-devel
BuildRequires: make

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

%autosetup -p1

%build
%configure
%{make_build}

%install
%{make_install}

%files
%doc README THANKS NEWS
%license COPYING
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*

%changelog
%autochangelog
