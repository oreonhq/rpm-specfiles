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
# oreon url source checksums begin
%global source0_sha256 f88335b7516a2995c9f798bc31c7fc463e3296c36ae2ce6b7db30a6ebd52d3c0
%global source0_file crash-trace-command-3.0.tar.gz
# oreon url source checksums end

%description
Command for reading ftrace data from a dump file.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/crash-trace-command-3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f88335b7516a2995c9f798bc31c7fc463e3296c36ae2ce6b7db30a6ebd52d3c0" || { echo "oreon: Source0 SHA256 mismatch for crash-trace-command-3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
