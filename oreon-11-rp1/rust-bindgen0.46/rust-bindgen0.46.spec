%global source0_hash 8f7f7f0701772b17de73e4f5cbcb1dd6926f4706cba4c1ab62c5367f8bdc94e1
%bcond check 0
%global debug_package %{nil}
%global crate bindgen
Name:           rust-bindgen0.46
Version:        0.46.0
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
License:        BSD-3-Clause
URL:            https://crates.io/crates/bindgen
Source0:        https://static.crates.io/crates/bindgen/bindgen-%{version}.crate
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
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+env_logger-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+env_logger-devel

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_docs-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+testing_only_docs-devel

This package contains library source intended for building other packages which
use the "testing_only_docs" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_extra_assertions-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+testing_only_extra_assertions-devel

This package contains library source intended for building other packages which
use the "testing_only_extra_assertions" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_libclang_3_8-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+testing_only_libclang_3_8-devel

This package contains library source intended for building other packages which
use the "testing_only_libclang_3_8" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_libclang_3_9-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+testing_only_libclang_3_9-devel

This package contains library source intended for building other packages which
use the "testing_only_libclang_3_9" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_libclang_4-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+testing_only_libclang_4-devel

This package contains library source intended for building other packages which
use the "testing_only_libclang_4" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_libclang_5-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries.
BuildArch:      noarch
%description -n %{name}+testing_only_libclang_5-devel

This package contains library source intended for building other packages which
use the "testing_only_libclang_5" feature of the "%{crate}" crate.

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
%files -n rust-bindgen0.46-devel -f %{oreon_filedir}/rust-bindgen0.46-devel.list

%changelog

%autochangelog
