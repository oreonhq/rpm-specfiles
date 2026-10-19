%global source0_hash 87bf01fc3269ada7109531b0d964ceb5527d1ef7b9c9a4269b3aabdf872f0e26
%if 0%{?oreon} >= 11
%global llvm_compat 21
%elif 0%{?fedora} >= 44
%global llvm_compat 20
%else
%global llvm_compat 22
%endif
Name:           bpftrace
Version:        0.27.0
Release:        1%{?dist}
Summary:        High-level tracing language for Linux eBPF
License:        Apache-2.0
URL:            https://github.com/iovisor/bpftrace
Source0:        https://github.com/iovisor/bpftrace/archive/refs/tags/v%{version}.tar.gz#/bpftrace-%{version}.tar.gz
ExclusiveArch:  x86_64 %{power64} aarch64 s390x riscv64
%if ! 0%{?rhel} || (0%{?oreon} >= 11)
%endif
# oreon:deps
BuildRequires:  bcc-devel
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  cereal-devel
BuildRequires:  clang20-devel
BuildRequires:  cmake
BuildRequires:  elfutils-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libbpf-devel
BuildRequires:  libbpf-static
BuildRequires:  libffi-devel
BuildRequires:  libpcap-devel
BuildRequires:  libxml2-devel
BuildRequires:  lldb-devel
BuildRequires:  llvm20-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  xxd
BuildRequires:  zlib-devel
# /oreon:deps
%description
BPFtrace is a high-level tracing language for Linux enhanced Berkeley Packet
Filter (eBPF) available in recent Linux kernels (4.x). BPFtrace uses LLVM as a
backend to compile scripts to BPF-bytecode and makes use of BCC for
interacting with the Linux BPF system, as well as existing Linux tracing
capabilities: kernel dynamic tracing (kprobes), user-level dynamic tracing
(uprobes), and tracepoints. The BPFtrace language is inspired by awk and C,
and predecessor tracers such as DTrace and SystemTap

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bpftrace-0.24.2
%oreon_prep
%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DBUILD_TESTING:BOOL=OFF \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DLLVM_REQUESTED_VERSION=%{llvm_compat} \
%if 0%{?llvm_compat}
       -DLLVM_DIR=/usr/lib64/llvm%{llvm_compat}/lib/cmake/llvm/ \
       -DClang_DIR=/usr/lib64/llvm%{llvm_compat}/lib/cmake/clang/ \
%endif
       %{nil}
%cmake_build
%install
%global __os_install_post %{nil}
%global _find_debuginfo_opts -g
%cmake_install
find %{buildroot}%{_datadir}/%{name}/tools -type f -exec \
  sed -i -e '1s=^#!/usr/bin/env %{name}\([0-9.]\+\)\?$=#!%{_bindir}/%{name}=' {} \;
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.24.2-3
- Import
