%global source0_hash 1a87a4b0521a9962100e3bdf393d2858e4de47b38e162e20384cc913845aacba
%define _hardened_build 1
Name:           funionfs
Version:        0.4.3
Release:        1%{?dist}
Summary:        Union filesystem in userspace
License:        GPL-2.0-or-later
URL:            http://funionfs.apiou.org
Source0:        http://funionfs.apiou.org/file/%{name}-%{version}.tar.gz
Requires:	fuse >= 2.5
# oreon:deps
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
FunionFS implements a union filesystem in userspace using FUSE.  FUSE
provides a Linux kernel module which allows virtual filesystems to be written
in userspace.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
make %{?_smp mflags}
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
