Name: dropwatch
Version: 1.5.5
Release: 3%{?dist}
Summary: Kernel dropped packet monitor

License: GPL-2.0-or-later
URL: https://github.com/nhorman/dropwatch
Source0: https://github.com/nhorman/dropwatch/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 73d4bcbbb056b3bd514b7d88ef927ece8aca32c2d50724b37c7d0a0d4d133009
%global source0_file dropwatch-1.5.5.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dropwatch-1.5.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "73d4bcbbb056b3bd514b7d88ef927ece8aca32c2d50724b37c7d0a0d4d133009" || { echo "oreon: Source0 SHA256 mismatch for dropwatch-1.5.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
