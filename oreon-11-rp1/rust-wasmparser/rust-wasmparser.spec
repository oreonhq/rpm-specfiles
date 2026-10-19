%global source0_hash f6d8db401b0528ec316dfbe579e6ab4152d61739cfe076706d2009127970159d
%bcond check 0
%global debug_package %{nil}
%global crate wasmparser
Name:           rust-wasmparser
Version:        0.243.0
Release:        1%{?dist}
Summary:        A simple event-driven library for parsing WebAssembly binary files.
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/wasmparser
Source0:        https://static.crates.io/crates/wasmparser/wasmparser-%{version}.crate
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
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+component-model-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+component-model-devel

This package contains library source intended for building other packages which
use the "component-model" feature of the "%{crate}" crate.

%package     -n %{name}+features-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+features-devel

This package contains library source intended for building other packages which
use the "features" feature of the "%{crate}" crate.

%package     -n %{name}+hash-collections-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+hash-collections-devel

This package contains library source intended for building other packages which
use the "hash-collections" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+prefer-btree-collections-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+prefer-btree-collections-devel

This package contains library source intended for building other packages which
use the "prefer-btree-collections" feature of the "%{crate}" crate.

%package     -n %{name}+semver-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+semver-devel

This package contains library source intended for building other packages which
use the "semver" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+validate-devel
Summary:        A simple event-driven library for parsing WebAssembly binary files.
BuildArch:      noarch
%description -n %{name}+validate-devel

This package contains library source intended for building other packages which
use the "validate" feature of the "%{crate}" crate.

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
%files -n rust-wasmparser-devel -f %{oreon_filedir}/rust-wasmparser-devel.list

%changelog

%autochangelog
