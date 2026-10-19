%global source0_hash 75b325c5dbd37f80359721ad39aca5a29fb04c89279657cffdda8736d0c0b9d2
%bcond check 1
%global debug_package %{nil}
%global crate downcast-rs
Name:           rust-downcast-rs1
Version:        1.2.1
Release:        1%{?dist}
Summary:        Trait object downcasting support using only safe Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/downcast-rs
Source0:        https://static.crates.io/crates/downcast-rs/downcast-rs-%{version}.crate
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
Summary:        Trait object downcasting support using only safe Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Trait object downcasting support using only safe Rust
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
%files -n rust-downcast-rs1-devel -f %{oreon_filedir}/rust-downcast-rs1-devel.list

%changelog

%autochangelog
