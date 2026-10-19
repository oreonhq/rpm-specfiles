%global source0_hash caf17cbebe0bfdf4f279ef84eeefe0d50468b0b7116f078acf41d456e48fe81a
%bcond check 1
%global debug_package %{nil}
%global crate prometheus_exporter
Name:           rust-prometheus_exporter
Version:        0.8.5
Release:        1%{?dist}
Summary:        Helper libary to export prometheus metrics using tiny-http
License:        MIT
URL:            https://crates.io/crates/prometheus_exporter
Source0:        https://static.crates.io/crates/prometheus_exporter/prometheus_exporter-%{version}.crate
Patch:          prometheus_exporter-fix-metadata.diff
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
Summary:        Helper libary to export prometheus metrics using tiny-http
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+internal_metrics-devel
Summary:        Helper libary to export prometheus metrics using tiny-http
BuildArch:      noarch
%description -n %{name}+internal_metrics-devel

This package contains library source intended for building other packages which
use the "internal_metrics" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static-devel
Summary:        Helper libary to export prometheus metrics using tiny-http
BuildArch:      noarch
%description -n %{name}+lazy_static-devel

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Helper libary to export prometheus metrics using tiny-http
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Helper libary to export prometheus metrics using tiny-http
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

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
%files -n rust-prometheus_exporter-devel -f %{oreon_filedir}/rust-prometheus_exporter-devel.list

%changelog

%autochangelog
