%global source0_hash none

Name:		biosdevname
Version:	0.7.3
Release:	21%{?dist}
Summary:	Udev helper for naming devices per BIOS names

# * biosdevname is GPL-2.0-only
# * bundled dmidecode is GPL-2.0-or-later
License:	GPL-2.0-only AND GPL-2.0-or-later

URL:		http://linux.dell.com/files/%{name}
# SMBIOS only exists on these arches.  It's also likely that other
# arches don't expect the PCI bus to be sorted breadth-first, or of
# so, there haven't been any comments about that on LKML.
ExclusiveArch:	%{ix86} x86_64
Source0:        http://linux.dell.com/files/biosdevname/biosdevname-0.7.3/biosdevname-0.7.3.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  pciutils-devel
BuildRequires:  zlib-devel
BuildRequires: make

Patch1: 0001-Disable-biosdevname-by-default.patch
Patch2: 0002-Place-udev-rules-to-usr-lib.patch

%description
biosdevname in its simplest form takes a kernel device name as an
argument, and returns the BIOS-given name it "should" be.  This is necessary
on systems where the BIOS name for a given device (e.g. the label on
the chassis is "Gb1") doesn't map directly and obviously to the kernel
name (e.g. eth0).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%autopatch

%build
autoreconf -fvi
%configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install install-data DESTDIR=%{buildroot}

%files
%doc COPYING README
%{_sbindir}/%{name}
%{_prefix}/lib/udev/rules.d/*.rules
%{_mandir}/man1/%{name}.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.3-21
- Import
