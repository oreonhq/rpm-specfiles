%global source0_hash 920602543f0911ab71da12c50d59701da54c196d1a2bf5cb4b75667f137a406a
%bcond check 0
%global debug_package %{nil}
%global crate toml
%global crate_version 1.1.6+spec-1.1.0
%global crate_instdir %{cargo_registry}/%{crate}-%{version}
Name:           rust-toml
Version:        1.1.6
Release:        1%{?dist}
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          toml-fix-metadata-auto.diff
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
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+fast_hash-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+fast_hash-devel

This package contains library source intended for building other packages which
use the "fast_hash" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unbounded-devel
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams
BuildArch:      noarch
%description -n %{name}+unbounded-devel

This package contains library source intended for building other packages which
use the "unbounded" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-toml-devel -f %{oreon_filedir}/rust-toml-devel.list

%changelog

%autochangelog
