# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 40b61e842a4efcbf80f3e53b2f220c044e8cfe46eb4dd6396c83b751240b1c0d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine _auto_set_build_flags

Name: gnu-efi
Epoch: 1
Version: 4.0.4
Release: 1%{?dist}
Summary: Development Libraries and headers for EFI
License: BSD-2-Clause AND BSD-2-Clause-Patent AND BSD-3-Clause AND BSD-4-Clause AND GPL-2.0-or-later AND GPL-2.0-only
URL: https://github.com/ncroxon/gnu-efi

Source0:        https://github.com/ncroxon/gnu-efi/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch: %{efi}
BuildRequires: oreon-rpm-macros
BuildRequires: binutils
BuildRequires: efi-srpm-macros >= 5-4
BuildRequires: clang

BuildRequires: make

Obsoletes: %{name}-compat < 1:3.0.11-12

%define lib %{nil}lib%{nil}

%define debug_package %{nil}

%undefine __brp_strip_static_archive
%global __brp_strip_static_archive find '%{buildroot}' -name '*.a' -print -exec %{__strip} -gDp {} \\;

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%package devel
Summary: Development Libraries and headers for EFI
Obsoletes: gnu-efi < 1:3.0.2-1
Requires: gnu-efi = %{epoch}:%{version}-%{release}

%description devel
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%package utils
Summary: Utilities for EFI systems

%description utils
This package contains utilities for debugging and developing EFI systems.

%prep
%oreon_sha256
%autosetup -p1

%build
%undefine _hardened_ldflags
make CC=%{__cc} HOSTCC=%{__cc} LIBDIR=%{_prefix}/lib
make CC=%{__cc} HOSTCC=%{__cc} apps

%install
make CC=%{__cc} HOSTCC=%{__cc} PREFIX=%{_prefix} LIBDIR=%{_prefix}/lib INSTALLROOT=%{buildroot} install
mkdir -p %{buildroot}/%{efi_esp_dir}/%{efi_arch}
mv %{buildroot}/usr/lib/gnuefi/apps/*.efi %{buildroot}%{efi_esp_dir}/%{efi_arch}/

%ifarch x86_64 aarch64 riscv64
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_libdir}
%endif

rm %{buildroot}/usr/lib/gnuefi/apps/debughook.efi.debug

%pretrans devel -p <lua>
path = "/usr/include/efi/x86_64"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files
%{_prefix}/lib/*.o
%{_prefix}/lib/*.lds

%files devel
%doc README.*
%{_includedir}/efi
%{_prefix}/lib/libefi.a
%{_prefix}/lib/libgnuefi.a
%{_libdir}/pkgconfig/gnu-efi.pc

%files utils
%dir %attr(0700,root,root) %{efi_esp_dir}/%{efi_arch}/
%attr(0700,root,root) %{efi_esp_dir}/%{efi_arch}/*.efi

%changelog
%autochangelog
