%global source0_hash f83d14da390562dca69fc84082e73e548e1ad308d24accdedd2720017cb37824
%bcond check 0
%global debug_package %{nil}
%global crate num-rational
Name:           rust-num-rational
Version:        0.4.2
Release:        1%{?dist}
Summary:        Rational numbers implementation for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-rational
Source0:        https://static.crates.io/crates/num-rational/num-rational-%{version}.crate
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
Summary:        Rational numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Rational numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-std-devel
Summary:        Rational numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+num-bigint-std-devel

This package contains library source intended for building other packages which
use the "num-bigint-std" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rational numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rational numbers implementation for Rust
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-num-rational-devel -f %{oreon_filedir}/rust-num-rational-devel.list

%changelog

%autochangelog
