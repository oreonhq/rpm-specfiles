%global source0_hash 82f4b26e751e711a5302649417f2da046dce6391b2ea30a4820f37462314f0b9
%bcond check 1
%global debug_package %{nil}
%global crate cargo_toml
Name:           rust-cargo_toml
Version:        1.0.1
Release:        1%{?dist}
Summary:        Cargo.toml struct definitions for parsing with Serde
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/cargo_toml
Source0:        https://static.crates.io/crates/cargo_toml/cargo_toml-%{version}.crate
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
Summary:        Cargo.toml struct definitions for parsing with Serde
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+features-devel
Summary:        Cargo.toml struct definitions for parsing with Serde
BuildArch:      noarch
%description -n %{name}+features-devel

This package contains library source intended for building other packages which
use the "features" feature of the "%{crate}" crate.

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
%files -n rust-cargo_toml-devel -f %{oreon_filedir}/rust-cargo_toml-devel.list

%changelog

%autochangelog
