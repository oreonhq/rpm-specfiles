%define	_bindir	/bin

Summary: A utility for configuring serial ports
Name: setserial
Version: 2.17
Release: 64%{?dist}
Source: https://sourceforge.net/projects/setserial/files/setserial/%{version}/%{name}-%{version}.tar.gz
Patch0: setserial-2.17-fhs.patch
Patch1: setserial-2.17-rc.patch
Patch2: setserial-2.17-readme.patch
Patch3: setserial-2.17-spelling.patch
Patch4: setserial-hayesesp.patch
Patch5: setserial-aarch64.patch
Patch6: setserial-configure-c99.patch
Patch7: setserial-c99.patch
# oreon url source checksums begin
%global source0_sha256 7e4487d320ac31558563424189435d396ddf77953bb23111a17a3d1487b5794a
%global source0_file setserial-2.17.tar.gz
# oreon url source checksums end
License: GPL-1.0-or-later
URL: http://setserial.sourceforge.net/
ExcludeArch: s390 s390x

BuildRequires: make
BuildRequires: gcc
BuildRequires: groff

%description
Setserial is a basic system utility for displaying or setting serial
port information. Setserial can reveal and allow you to alter the I/O
port and IRQ that a particular serial device is using, and more.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/setserial-2.17.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7e4487d320ac31558563424189435d396ddf77953bb23111a17a3d1487b5794a" || { echo "oreon: Source0 SHA256 mismatch for setserial-2.17.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
# Use FHS directory layout.
%patch -P0 -p1 -b .fhs

# Fixed initscript.
%patch -P1 -p1 -b .rc

# Corrected readme file.
%patch -P2 -p1 -b .readme

# Fixed spelling in help output.
%patch -P3 -p1 -b .spelling

# Don't require hayesesp.h (bug #564947).
%patch -P4 -p1 -b .hayesesp
rm -f config.cache

# Support aarch64 (bug #926522).
%patch -P5 -p1 -b .aarch64
%patch -P6 -p1
%patch -P7 -p1

%build
%set_build_flags
# Makefile expects CFLAGS to contain linker flags.
CFLAGS="$CFLAGS $LDFLAGS"
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8
make install DESTDIR=${RPM_BUILD_ROOT}

%files
%doc README rc.serial
%{_bindir}/setserial
%{_mandir}/man*/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17-64
- Import
