%global source0_hash 8cb01cd46b0cf372153850f4c6c272d9cbea2da513e07538405148f95bd789f3
%bcond check 0
%global debug_package %{nil}
%global crate figment
Name:           rust-figment
Version:        0.10.19
Release:        1%{?dist}
Summary:        A configuration library so con-free, it's unreal.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/figment
Source0:        https://static.crates.io/crates/figment/figment-%{version}.crate
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

%package     -n %{name}+env-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+env-devel

This package contains library source intended for building other packages which
use the "env" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+parse-value-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+parse-value-devel

This package contains library source intended for building other packages which
use the "parse-value" feature of the "%{crate}" crate.

%package     -n %{name}+pear-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+pear-devel

This package contains library source intended for building other packages which
use the "pear" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_yaml-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+serde_yaml-devel

This package contains library source intended for building other packages which
use the "serde_yaml" feature of the "%{crate}" crate.

%package     -n %{name}+tempfile-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+tempfile-devel

This package contains library source intended for building other packages which
use the "tempfile" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        A configuration library so con-free, it's unreal.
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

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
%files -n rust-figment-devel -f %{oreon_filedir}/rust-figment-devel.list

%changelog

%autochangelog
