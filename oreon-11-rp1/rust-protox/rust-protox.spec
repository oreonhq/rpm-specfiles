%global source0_hash 424c2bd294b69c49b949f3619362bc3c5d28298cd1163b6d1a62df37c16461aa
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate protox
Name:           rust-protox
Version:        0.8.0
Release:        1%{?dist}
Summary:        Rust implementation of the protobuf compiler
License:        (MIT OR Apache-2.0) AND BSD-3-Clause
URL:            https://crates.io/crates/protox
Source0:        https://static.crates.io/crates/protox/protox-%{version}.crate
Patch:          protox-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(protobuf) = 3.21.3
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust implementation of the protobuf compiler
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -i '/#\[cfg(test)\]/,/mod tests/d' src/file/mod.rs
sed -i '/#\[cfg(test)\]/,/mod tests/d' src/compile/mod.rs
%oreon_vendor_cargo
%build

%cargo_build -f bin
%install
%cargo_install -f bin
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f bin
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-protox-devel -f %{oreon_filedir}/rust-protox-devel.list

%changelog

%autochangelog
