%global source0_hash 79c4437c6f8ca904f46d33ac36062a65fdcf4a92a248478e408ab11295cf8e83

Name:		gxemul
Version:	0.7.0
Release:	13%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Summary:	Instruction-level machine emulator
URL:		http://gavare.se/gxemul/
Source0:	http://gavare.se/gxemul/src/%{name}-%{version}.tar.gz
Patch0:		gxemul-0.6.0.1-Makefile-cleanup.patch
Patch1:		gxemul-0.6.0.1-gcc47.patch
# https://sourceforge.net/p/gxemul/mailman/message/37270384/
Patch2:		gxemul-0.7.0-linux-fix.patch
Patch3:		gxemul-0.7.0-no-rpath.patch
BuildRequires:	libX11-devel, xorg-x11-proto-devel
BuildRequires:	gcc
BuildRequires:	make

%description
GXemul is an experimental instruction-level machine emulator. It can be
used to run binary code for (among others) MIPS-based machines, regardless
of host platform. Several emulation modes are available. For some modes,
processors and surrounding hardware components are emulated well enough to
let unmodified operating systems (e.g. NetBSD) run as if they were running
on a real machine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .cleanup
%patch -P1 -p1
%patch -P2 -p1 -b .linux-fix
%patch -P3 -p1 -b .no-rpath

%build
CFLAGS="$RPM_OPT_FLAGS" PREFIX="%{_prefix}" ./configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc LICENSE HISTORY README demos/
%doc %{_datadir}/doc/gxemul/
%{_bindir}/gxemul
%{_mandir}/man1/gxemul.*

%changelog
%autochangelog
