# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 73d4bcbbb056b3bd514b7d88ef927ece8aca32c2d50724b37c7d0a0d4d133009
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
