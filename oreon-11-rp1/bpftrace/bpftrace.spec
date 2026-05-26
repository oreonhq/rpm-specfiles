# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 e0514aa3e1a032b0b2de2cf3c281bfee9b9e80509498e70ed78786bbd64db373
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

#global llvm_compat 18

Name:           bpftrace
Version:        0.24.2
Release:        3%{?dist}
Summary:        High-level tracing language for Linux eBPF
License:        Apache-2.0

URL:            https://github.com/iovisor/bpftrace
Source0:        https://github.com/iovisor/bpftrace/archive/v0.24.2/bpftrace-0.24.2.tar.gz

# Arches will be included as upstream support is added and dependencies are
# satisfied in the respective arches
ExclusiveArch:  x86_64 %{power64} aarch64 s390x riscv64

BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  cmake
BuildRequires:  elfutils-libelf-devel
BuildRequires:  zlib-devel
BuildRequires:  llvm%{?llvm_compat}-devel
BuildRequires:  clang%{?llvm_compat}-devel
BuildRequires:  bcc-devel >= 0.19.0-1
BuildRequires:  libbpf-devel
BuildRequires:  libbpf-static
BuildRequires:  binutils-devel
BuildRequires:  cereal-devel
BuildRequires:  lldb-devel
%if ! 0%{?rhel} || 0%{?oreon}
BuildRequires:  libpcap-devel
%endif
BuildRequires:  rubygem-asciidoctor
BuildRequires:  xxd
BuildRequires:  libxml2-devel
BuildRequires:  libffi-devel
BuildRequires:  elfutils-devel


%description
BPFtrace is a high-level tracing language for Linux enhanced Berkeley Packet
Filter (eBPF) available in recent Linux kernels (4.x). BPFtrace uses LLVM as a
backend to compile scripts to BPF-bytecode and makes use of BCC for
interacting with the Linux BPF system, as well as existing Linux tracing
capabilities: kernel dynamic tracing (kprobes), user-level dynamic tracing
(uprobes), and tracepoints. The BPFtrace language is inspired by awk and C,
and predecessor tracers such as DTrace and SystemTap


%prep
%oreon_verify_sources
%autosetup -p1


%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DBUILD_TESTING:BOOL=OFF \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
%if 0%{?llvm_compat}
       -DLLVM_DIR=/usr/lib64/llvm%{llvm_compat}/lib/cmake/llvm/ \
       -DClang_DIR=/usr/lib64/llvm%{llvm_compat}/lib/cmake/clang/ \
%endif
       %{nil}
%cmake_build


%install
# The post hooks strip the binary which removes
# the BEGIN_trigger and END_trigger functions
# which are needed for the BEGIN and END probes
%global __os_install_post %{nil}
%global _find_debuginfo_opts -g

%cmake_install

# Fix shebangs ()
find %{buildroot}%{_datadir}/%{name}/tools -type f -exec \
  sed -i -e '1s=^#!/usr/bin/env %{name}\([0-9.]\+\)\?$=#!%{_bindir}/%{name}=' {} \;


%files
%doc README.md CONTRIBUTING-TOOLS.md
%doc docs/reference_guide.md docs/tutorial_one_liners.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tools
%dir %{_datadir}/%{name}/tools/old
%{_bindir}/%{name}
%{_bindir}/%{name}-aotrt
%{_mandir}/man8/*
%attr(0755,-,-) %{_datadir}/%{name}/tools/*.bt
%attr(0755,-,-) %{_datadir}/%{name}/tools/old/*.bt
%{_datadir}/bash-completion/completions/%{name}


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.24.2-3
- Import
