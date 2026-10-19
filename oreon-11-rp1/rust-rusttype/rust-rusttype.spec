%global source0_hash 3ff8374aa04134254b7995b63ad3dc41c7f7236f69528b28553da7d72efaa967
%bcond check 1
%global debug_package %{nil}
%global crate rusttype
Name:           rust-rusttype
Version:        0.9.3
Release:        1%{?dist}
Summary:        Pure Rust alternative to libraries like FreeType
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rusttype
Source0:        https://static.crates.io/crates/rusttype/rusttype-%{version}.crate
Patch:          rusttype-fix-metadata.diff
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
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-deque-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+crossbeam-deque-devel

This package contains library source intended for building other packages which
use the "crossbeam-deque" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-utils-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+crossbeam-utils-devel

This package contains library source intended for building other packages which
use the "crossbeam-utils" feature of the "%{crate}" crate.

%package     -n %{name}+gpu_cache-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+gpu_cache-devel

This package contains library source intended for building other packages which
use the "gpu_cache" feature of the "%{crate}" crate.

%package     -n %{name}+has-atomics-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+has-atomics-devel

This package contains library source intended for building other packages which
use the "has-atomics" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+libm-math-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+libm-math-devel

This package contains library source intended for building other packages which
use the "libm-math" feature of the "%{crate}" crate.

%package     -n %{name}+linked-hash-map-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+linked-hash-map-devel

This package contains library source intended for building other packages which
use the "linked-hash-map" feature of the "%{crate}" crate.

%package     -n %{name}+num_cpus-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+num_cpus-devel

This package contains library source intended for building other packages which
use the "num_cpus" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-hash-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+rustc-hash-devel

This package contains library source intended for building other packages which
use the "rustc-hash" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust alternative to libraries like FreeType
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rusttype-devel -f %{oreon_filedir}/rust-rusttype-devel.list

%changelog

%autochangelog
