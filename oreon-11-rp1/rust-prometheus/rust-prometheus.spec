%global source0_hash 3ca5326d8d0b950a9acd87e6a3f94745394f62e4dae1b1ee22b2bc0c394af43a
%bcond check 1
%global debug_package %{nil}
%global crate prometheus
Name:           rust-prometheus
Version:        0.14.0
Release:        1%{?dist}
Summary:        Prometheus instrumentation library for Rust applications
License:        Apache-2.0
URL:            https://crates.io/crates/prometheus
Source0:        https://static.crates.io/crates/prometheus/prometheus-%{version}.crate
Patch:          prometheus-fix-metadata.diff
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
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gen-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+gen-devel

This package contains library source intended for building other packages which
use the "gen" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+process-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+process-devel

This package contains library source intended for building other packages which
use the "process" feature of the "%{crate}" crate.

%package     -n %{name}+procfs-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+procfs-devel

This package contains library source intended for building other packages which
use the "procfs" feature of the "%{crate}" crate.

%package     -n %{name}+protobuf-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+protobuf-devel

This package contains library source intended for building other packages which
use the "protobuf" feature of the "%{crate}" crate.

%package     -n %{name}+protobuf-codegen-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+protobuf-codegen-devel

This package contains library source intended for building other packages which
use the "protobuf-codegen" feature of the "%{crate}" crate.

%package     -n %{name}+push-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+push-devel

This package contains library source intended for building other packages which
use the "push" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-devel
Summary:        Prometheus instrumentation library for Rust applications
BuildArch:      noarch
%description -n %{name}+reqwest-devel

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

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
%files -n rust-prometheus-devel -f %{oreon_filedir}/rust-prometheus-devel.list

%changelog

%autochangelog
