%global source0_hash e943b2c21337b7e3ec6678500687cdc741b7639ad457f234693352075c082204
%bcond check 0
%global debug_package %{nil}
%global crate nanoserde-derive
Name:           rust-nanoserde-derive
Version:        0.1.22
Release:        1%{?dist}
Summary:        Fork of makepad-tinyserde derive without any external dependencies
License:        MIT
URL:            https://crates.io/crates/nanoserde-derive
Source0:        https://static.crates.io/crates/nanoserde-derive/nanoserde-derive-%{version}.crate
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
Summary:        Fork of makepad-tinyserde derive without any external dependencies
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Fork of makepad-tinyserde derive without any external dependencies
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Fork of makepad-tinyserde derive without any external dependencies
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

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
%files -n rust-nanoserde-derive-devel -f %{oreon_filedir}/rust-nanoserde-derive-devel.list

%changelog

%autochangelog
