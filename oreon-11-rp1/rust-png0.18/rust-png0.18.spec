%global source0_hash 60769b8b31b2a9f263dae2776c37b1b28ae246943cf719eb6946a1db05128a61
%bcond check 0
%global debug_package %{nil}
%global crate png
Name:           rust-png0.18
Version:        0.18.1
Release:        1%{?dist}
Summary:        PNG decoding and encoding library in pure Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/png
Source0:        https://static.crates.io/crates/png/png-%{version}.crate
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

%package     -n %{name}+benchmarks-devel
Summary:        PNG decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+benchmarks-devel

This package contains library source intended for building other packages which
use the "benchmarks" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        PNG decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-rs-devel
Summary:        PNG decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+zlib-rs-devel

This package contains library source intended for building other packages which
use the "zlib-rs" feature of the "%{crate}" crate.

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
%files -n rust-png0.18-devel -f %{oreon_filedir}/rust-png0.18-devel.list

%changelog

%autochangelog
