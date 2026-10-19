%global source0_hash 66f8ac0a79782d13e4ec2f955113676d786539965b3764e06fb4e107dcc3da64
%bcond check 1
%global debug_package %{nil}
%global crate natord-plus-plus
Name:           rust-natord-plus-plus
Version:        2.0.0
Release:        1%{?dist}
Summary:        Natural ordering for Rust
License:        MIT
URL:            https://crates.io/crates/natord-plus-plus
Source0:        https://static.crates.io/crates/natord-plus-plus/natord-plus-plus-%{version}.crate
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
Summary:        Natural ordering for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-natord-plus-plus-devel -f %{oreon_filedir}/rust-natord-plus-plus-devel.list

%changelog

%autochangelog
