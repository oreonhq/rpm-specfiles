%global source0_hash 25dea7ac8057892855ec285c440160265225438c3c45072613c25a4b26e98ef5
%bcond check 0
%global debug_package %{nil}
%global crate metrics
Name:           rust-metrics
Version:        0.24.2
Release:        1%{?dist}
Summary:        Lightweight metrics facade
License:        MIT
URL:            https://crates.io/crates/metrics
Source0:        https://static.crates.io/crates/metrics/metrics-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Lightweight metrics facade
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml del dev-dependencies.criterion
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
%files -n rust-metrics-devel -f %{oreon_filedir}/rust-metrics-devel.list

%changelog

%autochangelog
