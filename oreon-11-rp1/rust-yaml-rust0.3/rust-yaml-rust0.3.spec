%global source0_hash e66366e18dc58b46801afbf2ca7661a9f59cc8c5962c29892b6039b4f86fa992
%bcond check 0
%global debug_package %{nil}
%global crate yaml-rust
Name:           rust-yaml-rust0.3
Version:        0.3.5
Release:        1%{?dist}
Summary:        The missing YAML 1.2 parser for rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/yaml-rust
Source0:        https://static.crates.io/crates/yaml-rust/yaml-rust-%{version}.crate
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
Summary:        The missing YAML 1.2 parser for rust
BuildArch:      noarch
%description -n %{name}+clippy-devel

This package contains library source intended for building other packages which
use the "clippy" feature of the "%{crate}" crate.

%package     -n %{name}+linked-hash-map-devel
Summary:        The missing YAML 1.2 parser for rust
BuildArch:      noarch
%description -n %{name}+linked-hash-map-devel

This package contains library source intended for building other packages which
use the "linked-hash-map" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        The missing YAML 1.2 parser for rust
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

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
%files -n rust-yaml-rust0.3-devel -f %{oreon_filedir}/rust-yaml-rust0.3-devel.list

%changelog

%autochangelog
