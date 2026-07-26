%global source0_hash 67fba9940582cddfa70113235818fb52d81e5be3db483dfb0816acb330515f64

Name:		z80asm
Version:	1.8
Release:	30%{?dist}
Summary:	Z80 Assembler
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://savannah.nongnu.org/projects/%{name}/
Source0:	http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz

# Don't use bundled libraries!
# Also patch Makefile to separate test target to support RPM check
Patch0:		z80asm-1.8-no-bundled-libs.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	dos2unix

%description
z80asm is an assembler for the Z80 microprocessor. The assembler aims
to be portable and complete. Of course it assembles all official
mnemonics, but it also aims to assemble the unofficial mnemonics.
The assembler was written with the MSX computer in mind as the target
platform, but it can be used for any system with a Z80 in it. Some
header files with labels of MSX specific addresses (BIOS, BDOS, system
variables) are included.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Fix line endings
dos2unix examples/hello.asm

# Don't use bundled libraries!
# Also patch Makefile to separate test target to support RPM check
%patch -P 0 -p1 -b .no-bundled-libs
rm -rf gnulib

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%check
make %{?_smp_mflags} CFLAGS="%{optflags}" test

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 %{name} %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 %{name}.1 %{buildroot}%{_mandir}/man1
install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -p -m0644 headers/*.asm %{buildroot}%{_datadir}/%{name}

%files
%doc COPYING GPL3 ChangeLog examples
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}

%changelog
%autochangelog
