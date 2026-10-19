%global source0_hash e5d5f669c3c759da81ec39293330f532b4181231c5e967e9cbc993bae5d40aa4
%global reponame crash-gcore
Summary:        Gcore extension module for the crash utility
Name: crash-gcore-command
Version: 1.6.4
Release:        1%{?dist}
License: GPL-2.0-only
Source0:        https://github.com/fujitsu/crash-gcore/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-gcore
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le x86_64
Requires: crash >= 8.0.6
Patch0: crash-gcore-1.6.4-coredump-fix-building-failure-due-to-undefined-macro.patch
Patch1: crash-gcore-1.6.4-set_context-third-arg.patch
Patch2: crash-gcore-1.6.4-x86-fix-the-issue-that-core-files-for-64-bit-tasks-a.patch
# oreon:deps
BuildRequires:  crash-devel
BuildRequires:  gcc
# /oreon:deps
%description
Command for creating a core dump file of a user-space task that was
running in a kernel dump file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{reponame}-%{version} -p1

%build

%make_build -C src -f gcore.mk
%install
install -m 0755 -d %{buildroot}%{_libdir}/crash/extensions
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions %{_builddir}/%{reponame}-%{version}/src/gcore.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.4-11
- Prepare for Oreon 11 (RP1)
