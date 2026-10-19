%global source0_hash 83d13394d44dae3207b52a326c0c85a8bf87f1541f23b0d143811088497b09ab
%bcond check 0
%global debug_package %{nil}
%global crate tiny-skia
Name:           rust-tiny-skia
Version:        0.11.4
Release:        1%{?dist}
Summary:        Tiny Skia subset ported to Rust
License:        BSD-3-Clause
URL:            https://crates.io/crates/tiny-skia
Source0:        https://static.crates.io/crates/tiny-skia/tiny-skia-%{version}.crate
Patch:          tiny-skia-fix-metadata.diff
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
Summary:        Tiny Skia subset ported to Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no-std-float-devel
Summary:        Tiny Skia subset ported to Rust
BuildArch:      noarch
%description -n %{name}+no-std-float-devel

This package contains library source intended for building other packages which
use the "no-std-float" feature of the "%{crate}" crate.

%package     -n %{name}+png-devel
Summary:        Tiny Skia subset ported to Rust
BuildArch:      noarch
%description -n %{name}+png-devel

This package contains library source intended for building other packages which
use the "png" feature of the "%{crate}" crate.

%package     -n %{name}+png-format-devel
Summary:        Tiny Skia subset ported to Rust
BuildArch:      noarch
%description -n %{name}+png-format-devel

This package contains library source intended for building other packages which
use the "png-format" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Tiny Skia subset ported to Rust
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Tiny Skia subset ported to Rust
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
%files -n rust-tiny-skia-devel -f %{oreon_filedir}/rust-tiny-skia-devel.list

%changelog

%autochangelog
