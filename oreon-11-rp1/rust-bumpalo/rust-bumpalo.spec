%global source0_hash 72f5acc6cb2ba439de613abc23857ec3d78374d8ed5ac84e9d11336e87da8649
%bcond check 0
%global debug_package %{nil}
%global crate bumpalo
Name:           rust-bumpalo
Version:        3.20.3
Release:        2%{?dist}
Summary:        A fast bump allocation arena for Rust.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bumpalo
Source0:        https://static.crates.io/crates/bumpalo/bumpalo-%{version}.crate
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
Summary:        A fast bump allocation arena for Rust.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+allocator-api2-devel
Summary:        A fast bump allocation arena for Rust.
BuildArch:      noarch
%description -n %{name}+allocator-api2-devel

This package contains library source intended for building other packages which
use the "allocator-api2" feature of the "%{crate}" crate.

%package     -n %{name}+allocator_api-devel
Summary:        A fast bump allocation arena for Rust.
BuildArch:      noarch
%description -n %{name}+allocator_api-devel

This package contains library source intended for building other packages which
use the "allocator_api" feature of the "%{crate}" crate.

%package     -n %{name}+bench_allocator_api-devel
Summary:        A fast bump allocation arena for Rust.
BuildArch:      noarch
%description -n %{name}+bench_allocator_api-devel

This package contains library source intended for building other packages which
use the "bench_allocator_api" feature of the "%{crate}" crate.

%package     -n %{name}+boxed-devel
Summary:        A fast bump allocation arena for Rust.
BuildArch:      noarch
%description -n %{name}+boxed-devel

This package contains library source intended for building other packages which
use the "boxed" feature of the "%{crate}" crate.

%package     -n %{name}+collections-devel
Summary:        A fast bump allocation arena for Rust.
BuildArch:      noarch
%description -n %{name}+collections-devel

This package contains library source intended for building other packages which
use the "collections" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A fast bump allocation arena for Rust.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A fast bump allocation arena for Rust.
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-bumpalo-devel -f %{oreon_filedir}/rust-bumpalo-devel.list

%changelog

%autochangelog
