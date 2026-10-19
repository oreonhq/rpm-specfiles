%global source0_hash f9d441c3b2ebf55cebf796bfdc265d67fa09db17b7bb6bd4be75c509e1e8fec3
%bcond check 0
%global debug_package %{nil}
%global crate rustc-std-workspace-alloc
Name:           rust-rustc-std-workspace-alloc
Version:        1.0.1
Release:        1%{?dist}
Summary:        crate for integration of crates.io crates into rust-lang/rust standar...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc-std-workspace-alloc
Source0:        https://static.crates.io/crates/rustc-std-workspace-alloc/rustc-std-workspace-alloc-%{version}.crate
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
Summary:        crate for integration of crates.io crates into rust-lang/rust standar...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-rustc-std-workspace-alloc-devel -f %{oreon_filedir}/rust-rustc-std-workspace-alloc-devel.list

%changelog

%autochangelog
