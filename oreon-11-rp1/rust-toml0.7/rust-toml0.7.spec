%global source0_hash dd79e69d3b627db300ff956027cc6c3798cef26d22526befdfcd12feeb6d2257
%bcond check 0
%global debug_package %{nil}
%global crate toml
Name:           rust-toml0.7
Version:        0.7.8
Release:        1%{?dist}
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml
Source0:        https://static.crates.io/crates/toml/toml-%{version}.crate
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
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
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
%files -n rust-toml0.7-devel -f %{oreon_filedir}/rust-toml0.7-devel.list

%changelog

%autochangelog
