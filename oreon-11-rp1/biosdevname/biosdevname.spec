Name:		biosdevname
Version:	0.7.3
Release:	21%{?dist}
Summary:	Udev helper for naming devices per BIOS names

# * biosdevname is GPL-2.0-only
# * bundled dmidecode is GPL-2.0-or-later
License:	GPL-2.0-only AND GPL-2.0-or-later

URL:		https://github.com/dell/%{name}
# SMBIOS only exists on these arches.  It's also likely that other
# arches don't expect the PCI bus to be sorted breadth-first, or of
# so, there haven't been any comments about that on LKML.
ExclusiveArch:	%{ix86} x86_64
# linux.dell.com tarball URL returns 404.
Source0:	https://github.com/dell/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.3-21
- Source0 from GitHub tag archive (Dell file mirror 404)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.3-21
- Prepare for Oreon 11 (RP1)
