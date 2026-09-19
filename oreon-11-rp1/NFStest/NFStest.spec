%global source0_hash 4d4c5c5adb72831f5787275ef23c5414ff5c57ce120cafb1cd53de07665745c1

Name: NFStest		
Version: 3.2
Release: 16%{?dist}
Summary: NFS Testing Tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later 
URL: http://wiki.linux-nfs.org/wiki/index.php/NFStest
Source0: http://www.linux-nfs.org/~mora/nfstest/releases/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: nfs-utils sudo tcpdump 
Requires: coreutils iproute iptables 
Requires: openssh-clients psmisc util-linux

%description
Provides a set of tools for testing either the NFS client or the NFS server, 
most of the functionality is focused mainly on testing the client. 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/nfstest_alloc
%{_bindir}/nfstest_cache
%{_bindir}/nfstest_delegation
%{_bindir}/nfstest_dio
%{_bindir}/nfstest_file
%{_bindir}/nfstest_interop
%{_bindir}/nfstest_io
%{_bindir}/nfstest_lock
%{_bindir}/nfstest_pkt
%{_bindir}/nfstest_pnfs
%{_bindir}/nfstest_posix
%{_bindir}/nfstest_sparse
%{_bindir}/nfstest_xid
%{_bindir}/nfstest_ssc
%{_bindir}/nfstest_fcmp
%{_bindir}/nfstest_rdma
%{_bindir}/nfstest_xattr
%{_mandir}/*/*
#For noarch packages: sitelib
%{python3_sitelib}/*

%doc COPYING README

%changelog
%autochangelog
