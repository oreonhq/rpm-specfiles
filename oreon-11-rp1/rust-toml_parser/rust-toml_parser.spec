%global source0_hash 1d38ac1cf9b95face32296c0a3ede1fdc270627c9d9c02a7274dd6d960dc4d56
%bcond check 0
%global debug_package %{nil}
%global crate toml_parser
%global crate_version 1.1.3+spec-1.1.0
%global crate_instdir %{cargo_registry}/%{crate}-%{version}
Name:           rust-toml_parser
Version:        1.1.3
Release:        1%{?dist}
Summary:        Yet another format-preserving TOML parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml_parser
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          toml_parser-fix-metadata-auto.diff
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
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+unsafe-devel

This package contains library source intended for building other packages which
use the "unsafe" feature of the "%{crate}" crate.

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
%files -n rust-toml_parser-devel -f %{oreon_filedir}/rust-toml_parser-devel.list

%changelog

%autochangelog
