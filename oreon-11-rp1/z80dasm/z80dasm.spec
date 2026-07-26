%global source0_hash 1d6966bf7bddd0965421455e666872607019cfa43352188f5580304dd1039539

Name:		z80dasm
Version:	1.1.3
Release:	24%{?dist}
Summary:	Z80 Disassembler
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.tablix.org/~avian/blog/articles/%{name}/
Source0:	http://www.tablix.org/~avian/%{name}/%{name}-%{version}.tar.gz

# Target addresses are 16 bits, but relative address computations were not
# being masked to 16 bits, causing bad results on all systems and buffer
# overruns in sprintf on 64-bit systems.  Reported to upstream via email
# on 27-Feb-2012.
Patch0:		z80dasm-1.1.3-16-bit-addr.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	z80asm

%description
z80dasm is a disassembler for the Zilog Z80 microprocessor and
compatibles. It can be used to reverse engineer programs and operating
systems for 1980's microcomputers using this processor architecture
(for example ZX81, Spectrum, Galaksija and many others).  Generated
assembly code can be assembled back with a number of Z80
assemblers. Compatibility with z80asm was thoroughly tested.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b .16-bit-addr

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%check
make test

%install
make install DESTDIR="%{buildroot}"

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
