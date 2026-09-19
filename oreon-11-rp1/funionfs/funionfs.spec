%global source0_hash 1a87a4b0521a9962100e3bdf393d2858e4de47b38e162e20384cc913845aacba

%define _hardened_build 1
Name:           funionfs
Version:        0.4.3
Release:        39%{?dist}
Summary:        Union filesystem in userspace

License:        GPL-2.0-or-later
URL:            http://funionfs.apiou.org
Source0:	http://funionfs.apiou.org/file/%{name}-%{version}.tar.gz

Requires:	fuse >= 2.5
BuildRequires:  gcc
BuildRequires:	fuse-devel >= 2.5
BuildRequires: make

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

%files
%license COPYING
%doc AUTHORS ChangeLog BUGS TODO NEWS README
%{_bindir}/funionfs
%{_mandir}/man1/*

%changelog
%autochangelog
