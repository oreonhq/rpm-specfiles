%global source0_hash 3a67fee0c315996bbba586c1c077e57625382d38dc48fb3c9e84d56a7a5effad
Name:		biosdevname
Version:	0.7.3
Release:        21%{?dist}
Summary:        Udev helper for naming devices per BIOS names
License:	GPL-2.0-only AND GPL-2.0-or-later
URL:		http://linux.dell.com/files/%{name}
ExclusiveArch:	%{ix86} x86_64
Source0:        https://github.com/dell/biosdevname/archive/refs/tags/v%{version}.tar.gz#/biosdevname-%{version}.tar.gz
Patch1:        0001-Disable-biosdevname-by-default.patch
Patch2:        0002-Place-udev-rules-to-usr-lib.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pciutils-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
biosdevname in its simplest form takes a kernel device name as an
argument, and returns the BIOS-given name it "should" be.  This is necessary
on systems where the BIOS name for a given device (e.g. the label on
the chassis is "Gb1") doesn't map directly and obviously to the kernel
name (e.g. eth0).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%autopatch

%build

autoreconf -fvi
%configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make install install-data DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.3-21
- Import
