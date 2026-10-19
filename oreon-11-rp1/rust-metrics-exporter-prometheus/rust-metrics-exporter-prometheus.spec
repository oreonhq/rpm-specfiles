%global source0_hash 2b166dea96003ee2531cf14833efedced545751d800f03535801d833313f8c15
%bcond check 1
%global debug_package %{nil}
%global crate metrics-exporter-prometheus
Name:           rust-metrics-exporter-prometheus
Version:        0.17.2
Release:        1%{?dist}
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
License:        MIT
URL:            https://crates.io/crates/metrics-exporter-prometheus
Source0:        https://static.crates.io/crates/metrics-exporter-prometheus/metrics-exporter-prometheus-%{version}.crate
Patch:          metrics-exporter-prometheus-fix-metadata.diff
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
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_hyper-client-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+_hyper-client-devel

This package contains library source intended for building other packages which
use the "_hyper-client" feature of the "%{crate}" crate.

%package     -n %{name}+_hyper-server-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+_hyper-server-devel

This package contains library source intended for building other packages which
use the "_hyper-server" feature of the "%{crate}" crate.

%package     -n %{name}+async-runtime-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+async-runtime-devel

This package contains library source intended for building other packages which
use the "async-runtime" feature of the "%{crate}" crate.

%package     -n %{name}+http-body-util-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+http-body-util-devel

This package contains library source intended for building other packages which
use the "http-body-util" feature of the "%{crate}" crate.

%package     -n %{name}+http-listener-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+http-listener-devel

This package contains library source intended for building other packages which
use the "http-listener" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+hyper-devel

This package contains library source intended for building other packages which
use the "hyper" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-rustls-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+hyper-rustls-devel

This package contains library source intended for building other packages which
use the "hyper-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-util-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+hyper-util-devel

This package contains library source intended for building other packages which
use the "hyper-util" feature of the "%{crate}" crate.

%package     -n %{name}+ipnet-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+ipnet-devel

This package contains library source intended for building other packages which
use the "ipnet" feature of the "%{crate}" crate.

%package     -n %{name}+push-gateway-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+push-gateway-devel

This package contains library source intended for building other packages which
use the "push-gateway" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+uds-listener-devel
Summary:        Metrics-compatible exporter for sending metrics to Prometheus
BuildArch:      noarch
%description -n %{name}+uds-listener-devel

This package contains library source intended for building other packages which
use the "uds-listener" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-metrics-exporter-prometheus-devel -f %{oreon_filedir}/rust-metrics-exporter-prometheus-devel.list

%changelog

%autochangelog
