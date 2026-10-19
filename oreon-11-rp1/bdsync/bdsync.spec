%global source0_hash e917f868c3340dce6dd3f26fecff2eeb96fdfbaf430b03b288029ccdf306ca0d
Name: bdsync
Summary:        Remote sync for block devices
Version: 0.11.4
Release:        1%{?dist}
License: GPL-2.0-only
Source0:        https://github.com/rolffokkens/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
URL: http://bdsync.rolf-fokkens.nl/
Patch1: bdsync-0.10-buildflags.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pandoc
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
