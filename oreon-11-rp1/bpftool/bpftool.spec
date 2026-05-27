%global source0_hash 786dd16887fa97649eb6abed42c56aa45fd4592c8bd3a7aa4d4e7ca5d1b5f2fb

Name:           bpftool
Version:        7.6.0
Release:        3%{?dist}
Summary:        Inspection and simple manipulation of eBPF programs and maps

%global libname libbpf
%global sources %{name}-%{libname}-v%{version}-sources

License:        GPL-2.0-only OR BSD-2-Clause
URL:            https://github.com/libbpf/bpftool
Source:         https://github.com/libbpf/bpftool/releases/download/v%{version}/%{sources}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  binutils-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libcap-devel
BuildRequires:  llvm-devel
BuildRequires:  clang
BuildRequires:  python3-docutils
BuildRequires:  kernel-devel

%description
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{sources}

%build
# We need to use vmlinux.h from kernel-devel rather than the one from the running system
%define kernel_version %(rpm -q --qf "%%{VERSION}-%%{RELEASE}.%%{ARCH}" kernel-devel)
%make_build -C src/ EXTRA_CFLAGS="%{build_cflags}" EXTRA_LDFLAGS="%{build_ldflags}" VMLINUX_H="/usr/src/kernels/%{kernel_version}/vmlinux.h"

%install
%make_install -C src/ prefix=%{_prefix} bash_compdir=%{bash_completions_dir} mandir=%{_mandir} doc-install

# bpftool Makefile hardcodes installation to %%{_prefix}/sbin
mv %{buildroot}%{_prefix}/sbin %{buildroot}%{_bindir}

%files
%{_bindir}/bpftool
%{bash_completions_dir}/bpftool
%{_mandir}/man8/bpftool*.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.6.0-3
- Prepare for Oreon 11 (RP1)
