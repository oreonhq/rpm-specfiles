%global source0_hash 4d4c5c5adb72831f5787275ef23c5414ff5c57ce120cafb1cd53de07665745c1
Name: NFStest		
Version: 3.2
Release:        1%{?dist}
Summary:        NFS Testing Tool
License: GPL-2.0-or-later 
URL: http://wiki.linux-nfs.org/wiki/index.php/NFStest
Source0:        http://www.linux-nfs.org/~mora/nfstest/releases/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: nfs-utils sudo tcpdump 
Requires: coreutils iproute iptables 
Requires: openssh-clients psmisc util-linux
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
