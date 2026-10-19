%global source0_hash 040a65b0c29f298d71ca45dd52d02b0d0ddc15b9b97d95dfeebe67d6fdd42a28
%bcond check 1
%global debug_package %{nil}
%global crate vm-allocator
Name:           rust-vm-allocator
Version:        0.1.3
Release:        1%{?dist}
Summary:        Helpers for allocating resources needed during the lifetime of a VM
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vm-allocator
Source0:        https://static.crates.io/crates/vm-allocator/vm-allocator-%{version}.crate
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
Summary:        Helpers for allocating resources needed during the lifetime of a VM
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Helpers for allocating resources needed during the lifetime of a VM
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-vm-allocator-devel -f %{oreon_filedir}/rust-vm-allocator-devel.list

%changelog

%autochangelog
