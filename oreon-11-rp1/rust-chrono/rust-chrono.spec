%global source2_hash 562eeec1a61e6d46a9b32bf5c49bddbab6d23a55c84048047675805a90bbd634
%global source1_hash 13d8d2f8ff68377530a61bc79791c474f93eef08879ca4478d2c39d5d2f8d12e
%global source0_hash 1aa79e62e7697b8e29b513a68abacf485adcd1fe8284a4316c5ae868e6633327
%bcond check 1
%global debug_package %{nil}
%global crate chrono
Name:           rust-chrono
Version:        0.4.45
Release:        1%{?dist}
Summary:        Date and time library for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chrono
Source0:        https://static.crates.io/crates/chrono/chrono-%{version}.crate
Source1:        https://github.com/chronotope/chrono/raw/v0.4.45/tests/android/tzdata#/android-tzdata
Source2:        https://github.com/chronotope/chrono/raw/v0.4.45/tests/ohos/tzdata#/ohos-tzdata
Patch:          chrono-drop-win-wasm-tests.diff
Patch:          chrono-fix-metadata-auto.diff
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
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__internal_bench-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+__internal_bench-devel

This package contains library source intended for building other packages which
use the "__internal_bench" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+clock-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+clock-devel

This package contains library source intended for building other packages which
use the "clock" feature of the "%{crate}" crate.

%package     -n %{name}+core-error-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+core-error-devel

This package contains library source intended for building other packages which
use the "core-error" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+defmt-devel

This package contains library source intended for building other packages which
use the "defmt" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+now-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+now-devel

This package contains library source intended for building other packages which
use the "now" feature of the "%{crate}" crate.

%package     -n %{name}+oldtime-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+oldtime-devel

This package contains library source intended for building other packages which
use the "oldtime" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-16-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-16-devel

This package contains library source intended for building other packages which
use the "rkyv-16" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-32-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-32-devel

This package contains library source intended for building other packages which
use the "rkyv-32" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-64-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-64-devel

This package contains library source intended for building other packages which
use the "rkyv-64" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-validation-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-validation-devel

This package contains library source intended for building other packages which
use the "rkyv-validation" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-locales-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+unstable-locales-devel

This package contains library source intended for building other packages which
use the "unstable-locales" feature of the "%{crate}" crate.

%package     -n %{name}+winapi-devel
Summary:        Date and time library for Rust
BuildArch:      noarch
%description -n %{name}+winapi-devel

This package contains library source intended for building other packages which
use the "winapi" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
mkdir -p tests/android tests/ohos
cp -p %{SOURCE1} tests/android/tzdata
cp -p %{SOURCE2} tests/ohos/tzdata
rm tests/win_bindings.rs tests/wasm.rs
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
%files -n rust-chrono-devel -f %{oreon_filedir}/rust-chrono-devel.list

%changelog

%autochangelog
