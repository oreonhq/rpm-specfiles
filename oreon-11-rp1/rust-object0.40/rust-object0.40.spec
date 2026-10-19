%global source0_hash dd229a0361b9d0d4396176e02d65897f487eebeab7caa6d443855ee152ca0b9c
%bcond check 1
%global debug_package %{nil}
%global crate object
Name:           rust-object0.40
Version:        0.40.0
Release:        1%{?dist}
Summary:        Unified interface for reading and writing object file formats
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/object
Source0:        https://static.crates.io/crates/object/object-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+archive-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+archive-devel

This package contains library source intended for building other packages which
use the "archive" feature of the "%{crate}" crate.

%package     -n %{name}+build-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+build-devel

This package contains library source intended for building other packages which
use the "build" feature of the "%{crate}" crate.

%package     -n %{name}+build_core-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+build_core-devel

This package contains library source intended for building other packages which
use the "build_core" feature of the "%{crate}" crate.

%package     -n %{name}+cargo-all-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+cargo-all-devel

This package contains library source intended for building other packages which
use the "cargo-all" feature of the "%{crate}" crate.

%package     -n %{name}+coff-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+coff-devel

This package contains library source intended for building other packages which
use the "coff" feature of the "%{crate}" crate.

%package     -n %{name}+compression-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+compression-devel

This package contains library source intended for building other packages which
use the "compression" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+elf-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+elf-devel

This package contains library source intended for building other packages which
use the "elf" feature of the "%{crate}" crate.

%package     -n %{name}+goff-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+goff-devel

This package contains library source intended for building other packages which
use the "goff" feature of the "%{crate}" crate.

%package     -n %{name}+macho-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+macho-devel

This package contains library source intended for building other packages which
use the "macho" feature of the "%{crate}" crate.

%package     -n %{name}+names-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+names-devel

This package contains library source intended for building other packages which
use the "names" feature of the "%{crate}" crate.

%package     -n %{name}+pe-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+pe-devel

This package contains library source intended for building other packages which
use the "pe" feature of the "%{crate}" crate.

%package     -n %{name}+read-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+read-devel

This package contains library source intended for building other packages which
use the "read" feature of the "%{crate}" crate.

%package     -n %{name}+read_core-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+read_core-devel

This package contains library source intended for building other packages which
use the "read_core" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unaligned-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+unaligned-devel

This package contains library source intended for building other packages which
use the "unaligned" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-all-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+unstable-all-devel

This package contains library source intended for building other packages which
use the "unstable-all" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

%package     -n %{name}+write-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+write-devel

This package contains library source intended for building other packages which
use the "write" feature of the "%{crate}" crate.

%package     -n %{name}+write_core-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+write_core-devel

This package contains library source intended for building other packages which
use the "write_core" feature of the "%{crate}" crate.

%package     -n %{name}+write_std-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+write_std-devel

This package contains library source intended for building other packages which
use the "write_std" feature of the "%{crate}" crate.

%package     -n %{name}+xcoff-devel
Summary:        Unified interface for reading and writing object file formats
BuildArch:      noarch
%description -n %{name}+xcoff-devel

This package contains library source intended for building other packages which
use the "xcoff" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-object0.40-devel -f %{oreon_filedir}/rust-object0.40-devel.list

%changelog

%autochangelog
