# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fed76b7acb54d810cc3982eb6394726010114977542fd146695887a7d904b60c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global libname libbpf
%global sources %{name}-%{libname}-v%{version}-sources

Name: bpftool
Version: 7.8.1
Release: 1%{?dist}
Summary: Inspection and simple manipulation of eBPF programs and maps
License: GPL-2.0-only OR BSD-2-Clause
URL: https://github.com/libbpf/bpftool
Source0: https://github.com/libbpf/bpftool/releases/download/v%{version}/%{sources}.tar.gz

ExcludeArch: %{ix86}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: binutils-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: libcap-devel
BuildRequires: llvm-devel
BuildRequires: python3-docutils
BuildRequires: kernel-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel

%description
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%prep
%oreon_sha256
%autosetup -p1 -n %{sources}

%build
%global kernel_version %(rpm -q --qf "%%{VERSION}-%%{RELEASE}.%%{ARCH}" kernel-devel 2>/dev/null | tail -n 1)
%make_build -C src CC=%{__cc} HOSTCC=%{__cc} EXTRA_CFLAGS="%{build_cflags}" EXTRA_LDFLAGS="%{build_ldflags}" HOST_EXTRACFLAGS="-Wno-error=format-security" VMLINUX_H="%{_usrsrc}/kernels/%{kernel_version}/vmlinux.h"

%install
%make_install -C src CC=%{__cc} HOSTCC=%{__cc} prefix=%{_prefix} bash_compdir=%{bash_completions_dir} mandir=%{_mandir} doc-install
mv %{buildroot}%{_prefix}/sbin %{buildroot}%{_bindir}

%files
%license LICENSE LICENSE.BSD-2-Clause LICENSE.GPL-2.0
%{_bindir}/bpftool
%{bash_completions_dir}/bpftool
%{_mandir}/man8/bpftool*.8*

%changelog
%autochangelog
