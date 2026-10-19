%global source0_hash 43b6dd56e85d9483277cde964fd1bdb0428de4fec5ebba7540995639a21cb32b
%bcond check 0
%global debug_package %{nil}
%global crate rav1e
Name:           rust-rav1e0.8
Version:        0.8.1
Release:        1%{?dist}
Summary:        The fastest and safest AV1 encoder
License:        BSD-2-Clause
URL:            https://crates.io/crates/rav1e
Source0:        https://static.crates.io/crates/rav1e/rav1e-%{version}.crate
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
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aom-sys-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+aom-sys-devel

This package contains library source intended for building other packages which
use the "aom-sys" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+av-metrics-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+av-metrics-devel

This package contains library source intended for building other packages which
use the "av-metrics" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+bench-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+binaries-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+binaries-devel

This package contains library source intended for building other packages which
use the "binaries" feature of the "%{crate}" crate.

%package     -n %{name}+byteorder-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+byteorder-devel

This package contains library source intended for building other packages which
use the "byteorder" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+channel-api-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+channel-api-devel

This package contains library source intended for building other packages which
use the "channel-api" feature of the "%{crate}" crate.

%package     -n %{name}+check_asm-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+check_asm-devel

This package contains library source intended for building other packages which
use the "check_asm" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+clap_complete-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+clap_complete-devel

This package contains library source intended for building other packages which
use the "clap_complete" feature of the "%{crate}" crate.

%package     -n %{name}+console-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+console-devel

This package contains library source intended for building other packages which
use the "console" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+crossbeam-devel

This package contains library source intended for building other packages which
use the "crossbeam" feature of the "%{crate}" crate.

%package     -n %{name}+dav1d-sys-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+dav1d-sys-devel

This package contains library source intended for building other packages which
use the "dav1d-sys" feature of the "%{crate}" crate.

%package     -n %{name}+decode_test-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+decode_test-devel

This package contains library source intended for building other packages which
use the "decode_test" feature of the "%{crate}" crate.

%package     -n %{name}+decode_test_dav1d-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+decode_test_dav1d-devel

This package contains library source intended for building other packages which
use the "decode_test_dav1d" feature of the "%{crate}" crate.

%package     -n %{name}+desync_finder-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+desync_finder-devel

This package contains library source intended for building other packages which
use the "desync_finder" feature of the "%{crate}" crate.

%package     -n %{name}+dump_ivf-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+dump_ivf-devel

This package contains library source intended for building other packages which
use the "dump_ivf" feature of the "%{crate}" crate.

%package     -n %{name}+dump_lookahead_data-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+dump_lookahead_data-devel

This package contains library source intended for building other packages which
use the "dump_lookahead_data" feature of the "%{crate}" crate.

%package     -n %{name}+fern-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+fern-devel

This package contains library source intended for building other packages which
use the "fern" feature of the "%{crate}" crate.

%package     -n %{name}+git_version-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+git_version-devel

This package contains library source intended for building other packages which
use the "git_version" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+ivf-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+ivf-devel

This package contains library source intended for building other packages which
use the "ivf" feature of the "%{crate}" crate.

%package     -n %{name}+nom-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+nom-devel

This package contains library source intended for building other packages which
use the "nom" feature of the "%{crate}" crate.

%package     -n %{name}+quick_test-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+quick_test-devel

This package contains library source intended for building other packages which
use the "quick_test" feature of the "%{crate}" crate.

%package     -n %{name}+scan_fmt-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+scan_fmt-devel

This package contains library source intended for building other packages which
use the "scan_fmt" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-big-array-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+serde-big-array-devel

This package contains library source intended for building other packages which
use the "serde-big-array" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+signal_support-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+signal_support-devel

This package contains library source intended for building other packages which
use the "signal_support" feature of the "%{crate}" crate.

%package     -n %{name}+threading-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+threading-devel

This package contains library source intended for building other packages which
use the "threading" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-chrome-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+tracing-chrome-devel

This package contains library source intended for building other packages which
use the "tracing-chrome" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-subscriber-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+tracing-subscriber-devel

This package contains library source intended for building other packages which
use the "tracing-subscriber" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-bindgen-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+wasm-bindgen-devel

This package contains library source intended for building other packages which
use the "wasm-bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+y4m-devel
Summary:        The fastest and safest AV1 encoder
BuildArch:      noarch
%description -n %{name}+y4m-devel

This package contains library source intended for building other packages which
use the "y4m" feature of the "%{crate}" crate.

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
%files -n rust-rav1e0.8-devel -f %{oreon_filedir}/rust-rav1e0.8-devel.list

%changelog

%autochangelog
