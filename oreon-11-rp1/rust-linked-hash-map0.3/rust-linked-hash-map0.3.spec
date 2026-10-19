%global source0_hash 6d262045c5b87c0861b3f004610afd0e2c851e2908d08b6c870cbb9d5f494ecd
%bcond check 0
%global debug_package %{nil}
%global crate linked-hash-map
Name:           rust-linked-hash-map0.3
Version:        0.3.0
Release:        1%{?dist}
Summary:        A HashMap wrapper that holds key-value pairs in insertion order
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/linked-hash-map
Source0:        https://static.crates.io/crates/linked-hash-map/linked-hash-map-%{version}.crate
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

%package     -n %{name}+clippy-devel
Summary:        A HashMap wrapper that holds key-value pairs in insertion order
BuildArch:      noarch
%description -n %{name}+clippy-devel

This package contains library source intended for building other packages which
use the "clippy" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A HashMap wrapper that holds key-value pairs in insertion order
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A HashMap wrapper that holds key-value pairs in insertion order
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_impl-devel
Summary:        A HashMap wrapper that holds key-value pairs in insertion order
BuildArch:      noarch
%description -n %{name}+serde_impl-devel

This package contains library source intended for building other packages which
use the "serde_impl" feature of the "%{crate}" crate.

%package     -n %{name}+serde_test-devel
Summary:        A HashMap wrapper that holds key-value pairs in insertion order
BuildArch:      noarch
%description -n %{name}+serde_test-devel

This package contains library source intended for building other packages which
use the "serde_test" feature of the "%{crate}" crate.

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
%files -n rust-linked-hash-map0.3-devel -f %{oreon_filedir}/rust-linked-hash-map0.3-devel.list

%changelog

%autochangelog
