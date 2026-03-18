%global reponame crash-trace

Summary: Trace extension module for the crash utility
Name: crash-trace-command
Version: 3.0
Release: 16%{?dist}
License: GPL-2.0-only
Source: https://github.com/fujitsu/crash-trace/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-trace
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le riscv64 s390x x86_64
BuildRequires: crash-devel >= 7.2.0-2
BuildRequires: gcc
Requires: trace-cmd
Requires: crash >= 7.2.0-2

Patch0001: 0001-Makefile-set-DT_SONAME-to-trace.so.patch
Patch0002: 0002-Makefile-fix-build-failure-on-aarch64-and-ppc64le.patch
Patch0003: 0003-Makefile-fix-build-failure-on-riscv64.patch

%description
Command for reading ftrace data from a dump file.

%prep
%autosetup -n %{reponame}-%{version}

%build
%make_build

%install
install -m 0755 -d %{buildroot}%{_libdir}/crash/extensions
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions %{_builddir}/%{reponame}-%{version}/trace.so

%files
%dir %{_libdir}/crash
%dir %{_libdir}/crash/extensions
%{_libdir}/crash/extensions/trace.so
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-16
- Prepare for Oreon 11 (RP1)
