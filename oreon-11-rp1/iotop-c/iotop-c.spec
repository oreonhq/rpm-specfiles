# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7c697a447f7ee95ccbf71619478a024f43016f8448e8eb4ce683e2baff124d9d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           iotop-c
Version:        1.33
Release:        1%{?dist}
Summary:        Simple top-like I/O monitor (implemented in C)

License:        GPL-2.0-or-later
URL:            https://github.com/Tomas-M/iotop/
Source0:        https://github.com/Tomas-M/iotop/releases/download/v%{version}/iotop-%{version}.tar.xz
Source1:        iotop-1.33.tar.xz.asc
Source2:        signing-key.asc

Provides:       iotop
Obsoletes:      iotop < 0.7

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  ncurses-devel
BuildRequires:  make
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  oreon-rpm-macros

%description
iotop-c does for I/O usage what top(1) does for CPU usage. It watches I/O
usage information output by the Linux kernel and displays a table of
current I/O usage by processes on the system. It is handy for answering
the question "Why is the disk churning so much?".

iotop-c requires a Linux kernel built with the CONFIG_TASKSTATS,
CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING and
CONFIG_VM_EVENT_COUNTERS config options on.

iotop-c is an alternative re-implementation of iotop in C, optimized for
performance. Normally a monitoring tool intended to be used on a system
under heavy stress should use the least additional resources as
possible.

%global _hardened_build 1

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n iotop-%{version}

%build
%set_build_flags
NO_FLTO=1 %make_build

%install
V=1 STRIP=: BINDIR=$RPM_BUILD_ROOT%{_bindir} %make_install

%files
%license COPYING
%license LICENSE
%{_bindir}/iotop
%{_mandir}/man8/iotop.8*

