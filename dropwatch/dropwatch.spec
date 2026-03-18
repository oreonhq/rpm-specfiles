Name: dropwatch
Version: 1.5.5
Release: 3%{?dist}
Summary: Kernel dropped packet monitor

License: GPL-2.0-or-later
URL: https://github.com/nhorman/dropwatch
Source0: https://github.com/nhorman/dropwatch/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: kernel-headers
BuildRequires: binutils-devel
BuildRequires: libnl3-devel
BuildRequires: libpcap-devel
BuildRequires: readline-devel

Requires: libnl3
Requires: readline

%description
dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%{make_install}

%files
%{_bindir}/dropwatch
%{_bindir}/dwdump
%{_mandir}/man1/dropwatch.1*
%{_mandir}/man1/dwdump.1*
%doc README.md
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.5-3
- Prepare for Oreon 11 (RP1)
