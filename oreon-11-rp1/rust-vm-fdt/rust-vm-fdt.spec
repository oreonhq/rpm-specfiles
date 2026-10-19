%global source0_hash 7e21282841a059bb62627ce8441c491f09603622cd5a21c43bfedc85a2952f23
%bcond check 0
%global debug_package %{nil}
%global crate vm-fdt
Name:           rust-vm-fdt
Version:        0.3.0
Release:        1%{?dist}
Summary:        For writing Flattened Devicetree blobs
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vm-fdt
Source0:        https://static.crates.io/crates/vm-fdt/vm-fdt-%{version}.crate
Patch:          vm-fdt-fix-metadata.diff
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
Summary:        For writing Flattened Devicetree blobs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        For writing Flattened Devicetree blobs
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        For writing Flattened Devicetree blobs
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+long_running_test-devel
Summary:        For writing Flattened Devicetree blobs
BuildArch:      noarch
%description -n %{name}+long_running_test-devel

This package contains library source intended for building other packages which
use the "long_running_test" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        For writing Flattened Devicetree blobs
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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

%ifarch %{ix86}
%cargo_test -f long_running_test -- -- --exact --skip=writer::tests::test_overflow_subtract
%else
%cargo_test -f long_running_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-vm-fdt-devel -f %{oreon_filedir}/rust-vm-fdt-devel.list

%changelog

%autochangelog
