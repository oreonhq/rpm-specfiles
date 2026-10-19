%global source0_hash 73d4bcbbb056b3bd514b7d88ef927ece8aca32c2d50724b37c7d0a0d4d133009
Name: dropwatch
Version: 1.5.5
Release:        1%{?dist}
Summary:        Kernel dropped packet monitor
License: GPL-2.0-or-later
URL: https://github.com/nhorman/dropwatch
Source0:        https://github.com/nhorman/dropwatch/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires: libnl3
Requires: readline
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
# /oreon:deps
%description
dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure
%make_build
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.5-3
- Prepare for Oreon 11 (RP1)
