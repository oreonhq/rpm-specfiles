%global source0_hash 50524592e6bfbb1bf6f94e8184a786f637faeaf1cf37bbe65502b9a2c5c48939
%bcond check 0
%global debug_package %{nil}
%global crate cargo-lock
Name:           rust-cargo-lock
Version:        11.1.0
Release:        1%{?dist}
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/cargo-lock
Source0:        https://static.crates.io/crates/cargo-lock/cargo-lock-%{version}.crate
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

%package     -n %{name}+clap-devel
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+dependency-tree-devel
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis
BuildArch:      noarch
%description -n %{name}+dependency-tree-devel

This package contains library source intended for building other packages which
use the "dependency-tree" feature of the "%{crate}" crate.

%package     -n %{name}+petgraph-devel
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis
BuildArch:      noarch
%description -n %{name}+petgraph-devel

This package contains library source intended for building other packages which
use the "petgraph" feature of the "%{crate}" crate.

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
%files -n rust-cargo-lock-devel -f %{oreon_filedir}/rust-cargo-lock-devel.list

%changelog

%autochangelog
