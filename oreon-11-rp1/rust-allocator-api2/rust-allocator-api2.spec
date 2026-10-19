%global source0_hash c880a97d28a3681c0267bd29cff89621202715b065127cd445fa0f0fe0aa2880
%bcond check 1
%global debug_package %{nil}
%global crate allocator-api2
Name:           rust-allocator-api2
Version:        0.4.0
Release:        1%{?dist}
Summary:        Mirror of Rust's allocator API
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/allocator-api2
Source0:        https://static.crates.io/crates/allocator-api2/allocator-api2-%{version}.crate
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
Summary:        Mirror of Rust's allocator API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Mirror of Rust's allocator API
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+fresh-rust-devel
Summary:        Mirror of Rust's allocator API
BuildArch:      noarch
%description -n %{name}+fresh-rust-devel

This package contains library source intended for building other packages which
use the "fresh-rust" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Mirror of Rust's allocator API
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Mirror of Rust's allocator API
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

%{cargo_test -- -- %{shrink:
    --skip "src/stable/boxed.rs"
    --skip "src/stable/vec/mod.rs"
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-allocator-api2-devel -f %{oreon_filedir}/rust-allocator-api2-devel.list

%changelog

%autochangelog
