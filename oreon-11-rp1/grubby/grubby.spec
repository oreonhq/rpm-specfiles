%global source0_hash none

# What?  No.
%define __brp_mangle_shebangs %{nil}

Name: grubby
Version: 8.40
Release: 88%{?dist}
Summary: Command line tool for updating bootloader configs
License: GPL-2.0-or-later
Source1: grubby-bls
# Source2: rpm-sort.c
Source3: COPYING
Source5: 95-kernel-hooks.install
Source6: 10-devicetree.install
Source7: grubby.8
Source8: kernel.sysconfig

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libblkid-devel
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: popt-devel
BuildRequires: rpm-devel
BuildRequires: sed
%ifarch aarch64 x86_64 %{power64} riscv64
BuildRequires: grub2-tools-minimal
Requires: grub2-tools-minimal
Requires: grub2-tools
%endif
%ifarch s390 s390x
Requires: s390utils-core
%endif
Requires: findutils
Requires: util-linux

ExcludeArch: %{ix86}
Conflicts:	uboot-tools < 2021.01-0.1.rc2
Obsoletes:	%{name}-bls < %{version}-%{release}
Obsoletes:	%{name}-deprecated < %{version}-%{release}

%description
This package provides a grubby compatibility script that manages
BootLoaderSpec files and is meant to be backward compatible with
the previous grubby tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }# Make sure the license can be found in mock
cp %{SOURCE3} . || true

%build
%set_build_flags

%install
mkdir -p %{buildroot}%{_sbindir}/
install -T -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/grubby

install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE5}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE6}

mkdir -p %{buildroot}%{_mandir}/man8
install -m 0644 %{SOURCE7} %{buildroot}%{_mandir}/man8/

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/kernel

%post
if [ "$1" = 2 ]; then
    arch=$(uname -m)
    [[ $arch == "s390x" ]] && \
    zipl-switch-to-blscfg --backup-suffix=.rpmsave &>/dev/null || :
fi

%files
%license COPYING
%attr(0755,root,root) %{_sbindir}/grubby
%attr(0755,root,root) %{_prefix}/lib/kernel/install.d/10-devicetree.install
%attr(0755,root,root) %{_prefix}/lib/kernel/install.d/95-kernel-hooks.install
%{_mandir}/man8/grubby.8*
%config(noreplace) %{_sysconfdir}/sysconfig/kernel

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.40-88
- Prepare for Oreon 11 (RP1)
