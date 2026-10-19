%global source0_hash a06f77d526c1a601b7c4cdd98f54b5eaabffc14d5f2f0296febdc7f357c6d3ba
%bcond check 1
%global debug_package %{nil}
%global crate fuchsia-cprng
Name:           rust-fuchsia-cprng
Version:        0.1.1
Release:        1%{?dist}
Summary:        Rust crate for the Fuchsia cryptographically secure pseudorandom numb...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fuchsia-cprng
Source0:        https://static.crates.io/crates/fuchsia-cprng/fuchsia-cprng-%{version}.crate
Patch:          fuchsia-cprng-test-zircon-call.patch
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
Summary:        Rust crate for the Fuchsia cryptographically secure pseudorandom numb...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -i '/^readme = "README.md"$/d' Cargo.toml
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
%files -n rust-fuchsia-cprng-devel -f %{oreon_filedir}/rust-fuchsia-cprng-devel.list

%changelog

%autochangelog
