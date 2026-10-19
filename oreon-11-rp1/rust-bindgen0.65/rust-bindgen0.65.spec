%global source0_hash cfdf7b466f9a4903edc73f95d6d2bcd5baf8ae620638762244d3f60143643cc5
%bcond check 1
%global debug_package %{nil}
%global crate bindgen
Name:           rust-bindgen0.65
Version:        0.65.1
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
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
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__cli-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+__cli-devel

This package contains library source intended for building other packages which
use the "__cli" feature of the "%{crate}" crate.

%package     -n %{name}+annotate-snippets-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+annotate-snippets-devel

This package contains library source intended for building other packages which
use the "annotate-snippets" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_extra_assertions-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+testing_only_extra_assertions-devel

This package contains library source intended for building other packages which
use the "testing_only_extra_assertions" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_libclang_5-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+testing_only_libclang_5-devel

This package contains library source intended for building other packages which
use the "testing_only_libclang_5" feature of the "%{crate}" crate.

%package     -n %{name}+testing_only_libclang_9-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+testing_only_libclang_9-devel

This package contains library source intended for building other packages which
use the "testing_only_libclang_9" feature of the "%{crate}" crate.

%package     -n %{name}+which-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+which-devel

This package contains library source intended for building other packages which
use the "which" feature of the "%{crate}" crate.

%package     -n %{name}+which-rustfmt-devel
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
BuildArch:      noarch
%description -n %{name}+which-rustfmt-devel

This package contains library source intended for building other packages which
use the "which-rustfmt" feature of the "%{crate}" crate.

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
%files -n rust-bindgen0.65-devel -f %{oreon_filedir}/rust-bindgen0.65-devel.list

%changelog

%autochangelog
