%global source0_hash 1ee7b61769254a59de1011ca3fe0b6a17cc8e8412a4f564d77c324a160b4eccf
%global __brp_strip_static_archive %{nil}
Name:           igvm
Version:        0.4.0
Release:        1%{?dist}
Summary:        IGVM library
License:        MIT
URL:            https://github.com/microsoft/igvm
Source0:        https://github.com/microsoft/igvm/archive/refs/tags/igvm-v%{version}.tar.gz
ExcludeArch: %{ix86}
Patch1: 0001-Bump-bitfield-struct-to-0.12.1.patch
Patch2: 0002-igvm_c-switch-Makefile-to-cargo-c-94.patch
Patch3: 0003-igvm_c-Makefile-fix-installation-with-empty-destdir-.patch
Patch4: 0004-igvm_c-dump_igvm-add-missing-device-tree-directive-9.patch
Patch5: 0005-igvm_c-fix-pkg-config-file-and-header-installation-1.patch
# oreon:deps
BuildRequires:  CUnit-devel
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  cbindgen
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Igvm is an implementation of a parser for the Independent Guest Virtual Machine

%package libs
Summary: IGVM shared library
%description libs
Contains a shared library that applications that use %{name} will link to

%package devel
Provides: igvm-static = %{version}-%{release}
Requires: igvm-libs = %{version}-%{release}
Summary: IGVM library header files
%description devel
Contains header files and a static library for developing applications that use %{name}

%package tools
Requires: igvm-libs = %{version}-%{release}
Summary: IGVM tools
%description tools
The %{name}-tools package contains tools for
developing applications that use %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir igvm-igvm-v%{version}
%oreon_prep
%build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%{igvm_makeenv} %make_build -C igvm_c build %{igvm_makeflags}
%check

%{igvm_makeenv} %make_build -C igvm_c test %{igvm_makeflags}
%install
%{igvm_makeenv} %make_install -C igvm_c PREFIX=/usr DESTDIR=%{buildroot} %{igvm_makeflags}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n igvm-libs -f %{oreon_filedir}/igvm-libs.list
%files -n igvm-devel -f %{oreon_filedir}/igvm-devel.list
%files -n igvm-tools -f %{oreon_filedir}/igvm-tools.list

%changelog

%autochangelog
