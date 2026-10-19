%global source0_hash 57226a8ec1bfbce06d68a42cde8cd980414a9457882e691fbce4a4f86c8d5f08
%bcond defrag 0
Name:           exfatprogs
Version:        1.4.3
Release:        1%{?dist}
Summary:        Userspace utilities for exFAT filesystems
License:        GPL-2.0-only
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(blkid)
# /oreon:deps
%description
Utilities for formatting and repairing exFAT filesystems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure \
    --enable-shared=yes \
    --enable-static=no
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-1
- Prepare for Oreon 11 (RP1)
