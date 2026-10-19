%global source0_hash 69d6512d3eb05ffe5004c59c206de7f99c34951504056ce23fc953842f12c445
%bcond check 0
%global debug_package %{nil}
%global crate abi_stable
Name:           rust-abi_stable
Version:        0.11.3
Release:        1%{?dist}
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/abi_stable
Source0:        https://static.crates.io/crates/abi_stable/abi_stable-%{version}.crate
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
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__ui-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+__ui-devel

This package contains library source intended for building other packages which
use the "__ui" feature of the "%{crate}" crate.

%package     -n %{name}+channels-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+channels-devel

This package contains library source intended for building other packages which
use the "channels" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-channel-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+crossbeam-channel-devel

This package contains library source intended for building other packages which
use the "crossbeam-channel" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+no_fn_promotion-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+no_fn_promotion-devel

This package contains library source intended for building other packages which
use the "no_fn_promotion" feature of the "%{crate}" crate.

%package     -n %{name}+no_tagging_doctest-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+no_tagging_doctest-devel

This package contains library source intended for building other packages which
use the "no_tagging_doctest" feature of the "%{crate}" crate.

%package     -n %{name}+nonexhaustive_examples-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+nonexhaustive_examples-devel

This package contains library source intended for building other packages which
use the "nonexhaustive_examples" feature of the "%{crate}" crate.

%package     -n %{name}+only_new_tests-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+only_new_tests-devel

This package contains library source intended for building other packages which
use the "only_new_tests" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_64-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+rust_1_64-devel

This package contains library source intended for building other packages which
use the "rust_1_64" feature of the "%{crate}" crate.

%package     -n %{name}+rust_latest_stable-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+rust_latest_stable-devel

This package contains library source intended for building other packages which
use the "rust_latest_stable" feature of the "%{crate}" crate.

%package     -n %{name}+sabi_trait_examples-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+sabi_trait_examples-devel

This package contains library source intended for building other packages which
use the "sabi_trait_examples" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+test_miri_track_raw-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+test_miri_track_raw-devel

This package contains library source intended for building other packages which
use the "test_miri_track_raw" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        For doing Rust-to-Rust ffi,writing libraries loaded at program startup.
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

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
%files -n rust-abi_stable-devel -f %{oreon_filedir}/rust-abi_stable-devel.list

%changelog

%autochangelog
