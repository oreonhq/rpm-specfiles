# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define __brp_mangle_shebangs %{nil}

Name: grubby
Version: 8.40
Release: 1%{?dist}
Summary: Command line tool for updating bootloader configs
License: GPL-2.0-or-later
URL: https://src.fedoraproject.org/rpms/grubby
Source1: grubby-bls
Source3: COPYING
Source5: 95-kernel-hooks.install
Source6: 10-devicetree.install
Source7: grubby.8
Source8: kernel.sysconfig

BuildRequires: oreon-rpm-macros
BuildRequires: sed
%ifarch aarch64 x86_64
BuildRequires: grub2-tools-minimal
Requires: grub2-tools-minimal
Requires: grub2-tools
%endif
Requires: findutils
Requires: util-linux

ExcludeArch: %{ix86}
Obsoletes: %{name}-bls < %{version}-%{release}
Obsoletes: %{name}-deprecated < %{version}-%{release}

%description
This package provides a grubby compatibility script that manages
BootLoaderSpec files and is meant to be backward compatible with
the previous grubby tool.

%prep
cp %{SOURCE3} .

%build
:

%install
mkdir -p %{buildroot}%{_sbindir}/
install -T -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/grubby

install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE5}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE6}

mkdir -p %{buildroot}%{_mandir}/man8
install -m 0644 %{SOURCE7} %{buildroot}%{_mandir}/man8/

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/kernel

%files
%license COPYING
%attr(0755,root,root) %{_sbindir}/grubby
%attr(0755,root,root) %{_prefix}/lib/kernel/install.d/10-devicetree.install
%attr(0755,root,root) %{_prefix}/lib/kernel/install.d/95-kernel-hooks.install
%{_mandir}/man8/grubby.8*
%config(noreplace) %{_sysconfdir}/sysconfig/kernel

%changelog
%autochangelog
