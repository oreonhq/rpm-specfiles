%global source0_hash 8da2c4a58a3917a8229dec0da97e718f90ede84985424d74456575bf5acfeec8
Name:		z80dasm
Version:	1.2.0
Release:        1%{?dist}
Summary:        Z80 Disassembler
License:	GPL-2.0-or-later
URL:		http://www.tablix.org/~avian/blog/articles/%{name}/
Source0:        http://www.tablix.org/~avian/%{name}/%{name}-%{version}.tar.gz
Patch0:		z80dasm-1.1.3-16-bit-addr.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  z80asm
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
