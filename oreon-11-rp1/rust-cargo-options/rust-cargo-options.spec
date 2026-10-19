%global source0_hash f89e1d6d6f65fe04d5e21be9de19d31a074e3b7e43aa39ee5b85f4cee16c3188
%bcond check 1
%global debug_package %{nil}
%global crate cargo-options
Name:           rust-cargo-options
Version:        0.7.6
Release:        1%{?dist}
Summary:        Reusable common Cargo command line options
License:        MIT
URL:            https://crates.io/crates/cargo-options
Source0:        https://static.crates.io/crates/cargo-options/cargo-options-%{version}.crate
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
Summary:        Reusable common Cargo command line options
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Reusable common Cargo command line options
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

%cargo_test -- --lib
%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cargo-options-devel -f %{oreon_filedir}/rust-cargo-options-devel.list

%changelog

%autochangelog
