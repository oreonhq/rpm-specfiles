%global source2_hash 1db16fd8e0ad0db16d8fd421c98e20560f4ddad5756af21c648b1402fc7240f1
%global source1_hash b73254c2203d5cec9c7429846cc1b0743066d387291fe733978aeffd78126acd
%global source0_hash 7740ada353262808c12f19b5efc37b3c7bfb6be3be4abc0404557806d0204b26
Name:           iotop-c
Version:        1.31
Release:        1%{?dist}
Summary:        Simple top-like I/O monitor (implemented in C)
License:        GPL-2.0-or-later
URL:            https://github.com/Tomas-M/iotop/
Source0:        https://github.com/Tomas-M/iotop/releases/download/v%{version}/iotop-%{version}.tar.xz
Source1:        https://github.com/Tomas-M/iotop/releases/download/v%{version}/iotop-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/Tomas-M/iotop/v%{version}/debian/upstream/signing-key.asc
Provides:       iotop
Obsoletes:      iotop < 0.7
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(ncursesw)
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n iotop-%{version}

%build

%set_build_flags
NO_FLTO=1 %make_build
%install
V=1 STRIP=: BINDIR=$RPM_BUILD_ROOT%{_bindir} %make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31-1
- Prepare for Oreon 11 (RP1)
