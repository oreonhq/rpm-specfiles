%global source0_hash c996721fef924f538230338c9e0a41a361a296e87e7884d4599241a355266ca5

# Name of the upstream GitHub repository.
%global repo_name ProcDump-for-Linux

Name:           procdump
Version:        3.5.0
Release:        2%{?dist}
Summary:        Sysinternals process dump utility

License:        MIT
URL:            https://github.com/Microsoft/%{repo_name}
Source:         %{url}/archive/%{version}/%{repo_name}-%{version}.tar.gz
Patch1:         0001-tests-Remove-unused-variable-work_time-from-stress_c.patch
Patch2:         0002-Initialize-TerminalState-structure-properly.patch
Patch3:         0003-CMake-Add-ability-to-use-system-installed-libbpf-rat.patch
Patch4:         0004-cmake-Include-install-section-for-procdump-and-its-m.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  libbpf-devel
BuildRequires:  bpftool
BuildRequires:  git
BuildRequires:  zlib-devel
Requires:       gdb >= 7.6.1

%undefine _annotated_build
%undefine _hardened_build

# ProcDump does not support PPC64 (#163) and s390x.
# For further information see ./ebpf/vmlinux.h.
ExclusiveArch:    x86_64 aarch64

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

%files
%license LICENSE
%doc README.md
%doc procdump.gif
%{_bindir}/procdump
%{_mandir}/man1/procdump.1.gz

%changelog
%autochangelog
