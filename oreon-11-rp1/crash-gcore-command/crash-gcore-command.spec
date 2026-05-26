%global reponame crash-gcore

Summary: Gcore extension module for the crash utility
Name: crash-gcore-command
Version: 1.6.4
Release: 11%{?dist}
License: GPL-2.0-only
Source0: https://github.com/fujitsu/crash-gcore/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-gcore
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le x86_64
BuildRequires: crash-devel >= 8.0.6
BuildRequires: gcc
Requires: crash >= 8.0.6

Patch0: crash-gcore-1.6.4-coredump-fix-building-failure-due-to-undefined-macro.patch
# https://github.com/fujitsu/crash-gcore/pull/6
Patch1: crash-gcore-1.6.4-set_context-third-arg.patch
Patch2: crash-gcore-1.6.4-x86-fix-the-issue-that-core-files-for-64-bit-tasks-a.patch
# oreon url source checksums begin
%global source0_sha256 e5d5f669c3c759da81ec39293330f532b4181231c5e967e9cbc993bae5d40aa4
%global source0_file crash-gcore-command-1.6.4.tar.gz
# oreon url source checksums end

%description
Command for creating a core dump file of a user-space task that was
running in a kernel dump file.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/crash-gcore-command-1.6.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e5d5f669c3c759da81ec39293330f532b4181231c5e967e9cbc993bae5d40aa4" || { echo "oreon: Source0 SHA256 mismatch for crash-gcore-command-1.6.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{reponame}-%{version} -p1

%build
%make_build -C src -f gcore.mk

%install
install -m 0755 -d %{buildroot}%{_libdir}/crash/extensions
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions %{_builddir}/%{reponame}-%{version}/src/gcore.so

%files
%dir %{_libdir}/crash
%dir %{_libdir}/crash/extensions
%{_libdir}/crash/extensions/gcore.so
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.4-11
- Prepare for Oreon 11 (RP1)
