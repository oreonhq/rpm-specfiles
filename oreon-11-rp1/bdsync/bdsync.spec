%global source0_hash c1af643de4f543f3f9f87c9329e5fae1ca9a37c215068b2079feb376ff44a322

Name: bdsync
Summary: Remote sync for block devices
Version: 0.11.2
Release: 17%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Source: https://github.com/rolffokkens/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
URL: http://bdsync.rolf-fokkens.nl/

Patch1: bdsync-0.10-buildflags.patch

BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: pandoc
BuildRequires: make

%description
Bdsync can be used to synchronize block devices over a network. It generates
a "binary patchfile" in an efficient way by comparing MD5 checksums of 32k
blocks of the local block device LOCDEV and the remote block device REMDEV.

This binary patchfile can be sent to the remote machine and applied to its
block device DSTDEV, after which the local blockdev LOCDEV and the remote
block device REMDEV are synchronized.

bdsync was built to do the only thing rsync isn't able to do: synchronize
block devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1

%build
%set_build_flags
%make_build

%check
make test

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{name} %{buildroot}/%{_bindir}/%{name}
cp %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files 
%if 0%{?fedora}
%license COPYING
%else
%doc COPYING
%endif
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
