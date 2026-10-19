%global source0_hash e0232bd009a197ceec9cc881ba46f727fcd8060a2d8d6a9dde7a69030a6fe2bb
%bcond check 0
%global debug_package %{nil}
%global crate postcard-derive
Name:           rust-postcard-derive
Version:        0.2.2
Release:        1%{?dist}
Summary:        A no_std + serde compatible message library for Rust - Derive Crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/postcard-derive
Source0:        https://static.crates.io/crates/postcard-derive/postcard-derive-%{version}.crate
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
Summary:        A no_std + serde compatible message library for Rust - Derive Crate
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
%files -n rust-postcard-derive-devel -f %{oreon_filedir}/rust-postcard-derive-devel.list

%changelog

%autochangelog
