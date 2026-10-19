%global source0_hash 95784e84a571f44dc7fd4f0d3ab3f493d3c07b90d695450890490a89d83905a3
%bcond check 1
%global debug_package %{nil}
%global crate random-fast-rng
Name:           rust-random-fast-rng
Version:        0.1.1
Release:        1%{?dist}
Summary:        Rust library for Blazing fast non cryptographic random number generator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/random-fast-rng
Source0:        https://static.crates.io/crates/random-fast-rng/random-fast-rng-%{version}.crate
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
Summary:        Rust library for Blazing fast non cryptographic random number generator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust library for Blazing fast non cryptographic random number generator
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
printf "%s\n" "random-fast-rng" > README.md
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
%files -n rust-random-fast-rng-devel -f %{oreon_filedir}/rust-random-fast-rng-devel.list

%changelog

%autochangelog
