%global source0_hash 172f80a80089099c7e49be4e2c6c1af05cd2d9f9e9c49e81e96f498c2e21b53a
%global repo_name ProcDump-for-Linux
Name:           procdump
Version:        3.5.3
Release:        1%{?dist}
Summary:        Sysinternals process dump utility
License:        MIT
URL:            https://github.com/Microsoft/%{repo_name}
Source0:        https://github.com/Microsoft/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz
Patch1:         0001-tests-Remove-unused-variable-work_time-from-stress_c.patch
Patch2:         0002-Initialize-TerminalState-structure-properly.patch
Patch3:         0003-CMake-Add-ability-to-use-system-installed-libbpf-rat.patch
Patch4:         0004-cmake-Include-install-section-for-procdump-and-its-m.patch
Requires:       gdb >= 7.6.1
%undefine _annotated_build
%undefine _hardened_build
ExclusiveArch:    x86_64 aarch64
# oreon:deps
BuildRequires:  bpftool
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libbpf-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
ProcDump is a command-line utility whose primary purpose is monitoring an application
for various resources and generating crash dumps during a spike that an administrator
or developer can use to determine the cause of the issue. ProcDump also serves as a
general process dump utility that you can embed in other scripts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo_name}-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
