%global source0_hash 7f212c96ee66547eeefb531267b641e5473d7d8529f0bd8ccdefd33cf7413f5c
%undefine _auto_set_build_flags
Name: gnu-efi
Epoch: 1
Version: 3.0.18
Release:        1%{?dist}
Summary:        Development Libraries and headers for EFI
License: BSD-2-Clause AND BSD-2-Clause-Patent AND BSD-3-Clause AND BSD-4-Clause AND GPL-2.0-or-later AND GPL-2.0-only
URL: https://sourceforge.net/projects/gnu-efi/
Source0:        https://sourceforge.net/projects/gnu-efi/files/gnu-efi-%{version}.tar.bz2
Patch0048: 0049-objcopy-use-output-target-instead-of-target.patch
ExclusiveArch: %{efi}
%ifarch x86_64
%endif
Obsoletes: %{name}-compat < 1:3.0.11-12
%define lib %{nil}lib%{nil}
%define debug_package %{nil}
%undefine __brp_strip_static_archive
%global __brp_strip_static_archive find '%{buildroot}' -name '*.a' -print -exec %{__strip} -gDp {} \\;
# oreon:deps
BuildRequires:  binutils
BuildRequires:  efi-srpm-macros
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  git-core
BuildRequires:  make
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%undefine _hardened_ldflags
make LIBDIR=%{_prefix}/lib
make apps
%install
make PREFIX=%{_prefix} LIBDIR=%{_prefix}/lib INSTALLROOT=%{buildroot} install
mkdir -p %{buildroot}/%{efi_esp_dir}/%{efi_arch}
mv %{buildroot}/usr/lib/gnuefi/apps/*.efi %{buildroot}%{efi_esp_dir}/%{efi_arch}/
%ifarch x86_64 aarch64 riscv64
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_libdir}
%endif
rm %{buildroot}/usr/lib/gnuefi/apps/debughook.efi.debug
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pretrans devel -p <lua>

-- Handle replacing a symlink to a directory with an actual directory
-- https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
path = "/usr/include/efi/x86_64"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end
%files -f %{oreon_filedir}/main.list
%files -n gnu-efi-devel -f %{oreon_filedir}/gnu-efi-devel.list
%files -n gnu-efi-utils -f %{oreon_filedir}/gnu-efi-utils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.18-1
- Prepare for Oreon 11 (RP1)
