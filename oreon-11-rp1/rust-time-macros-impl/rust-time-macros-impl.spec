%global source0_hash fd3c141a1b43194f3f56a1411225df8646c55781d5f26db825b3d98507eb482f
%bcond check 0
%global debug_package %{nil}
%global crate time-macros-impl
Name:           rust-time-macros-impl
Version:        0.1.2
Release:        1%{?dist}
Summary:        Procedural macros for the time crate.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/time-macros-impl
Source0:        https://static.crates.io/crates/time-macros-impl/time-macros-impl-%{version}.crate
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
Summary:        Procedural macros for the time crate.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -i '/^readme *=/d' Cargo.toml
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
%files -n rust-time-macros-impl-devel -f %{oreon_filedir}/rust-time-macros-impl-devel.list

%changelog

%autochangelog
