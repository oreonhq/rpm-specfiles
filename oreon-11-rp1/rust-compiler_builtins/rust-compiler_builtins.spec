%global source0_hash 6376049cfa92c0aa8b9ac95fae22184b981c658208d4ed8a1dc553cd83612895
%bcond check 0
%global debug_package %{nil}
%global crate compiler_builtins
Name:           rust-compiler_builtins
Version:        0.1.160
Release:        1%{?dist}
Summary:        Compiler intrinsics used by the Rust compiler.
License:        MIT AND Apache-2.0 WITH LLVM-exception AND (MIT OR Apache-2.0)
URL:            https://crates.io/crates/compiler_builtins
Source0:        https://static.crates.io/crates/compiler_builtins/compiler_builtins-%{version}.crate
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
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+c-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+c-devel

This package contains library source intended for building other packages which
use the "c" feature of the "%{crate}" crate.

%package     -n %{name}+compiler-builtins-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+compiler-builtins-devel

This package contains library source intended for building other packages which
use the "compiler-builtins" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+mangled-names-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+mangled-names-devel

This package contains library source intended for building other packages which
use the "mangled-names" feature of the "%{crate}" crate.

%package     -n %{name}+mem-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+mem-devel

This package contains library source intended for building other packages which
use the "mem" feature of the "%{crate}" crate.

%package     -n %{name}+no-asm-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+no-asm-devel

This package contains library source intended for building other packages which
use the "no-asm" feature of the "%{crate}" crate.

%package     -n %{name}+no-f16-f128-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+no-f16-f128-devel

This package contains library source intended for building other packages which
use the "no-f16-f128" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-public-internals-devel
Summary:        Compiler intrinsics used by the Rust compiler.
BuildArch:      noarch
%description -n %{name}+unstable-public-internals-devel

This package contains library source intended for building other packages which
use the "unstable-public-internals" feature of the "%{crate}" crate.

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
%files -n rust-compiler_builtins-devel -f %{oreon_filedir}/rust-compiler_builtins-devel.list

%changelog

%autochangelog
