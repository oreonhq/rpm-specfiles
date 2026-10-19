%global source0_hash 3c7028bdd3d43083f6d8d4d5187680d0d3560d54df4cc9d752005268b41e64d0
%bcond check 1
%global debug_package %{nil}
%global crate ouroboros_macro
Name:           rust-ouroboros_macro
Version:        0.18.5
Release:        1%{?dist}
Summary:        Proc macro for ouroboros crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ouroboros_macro
Source0:        https://static.crates.io/crates/ouroboros_macro/ouroboros_macro-%{version}.crate
Patch:          ouroboros_macro-fix-metadata.diff
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
Summary:        Proc macro for ouroboros crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Proc macro for ouroboros crate
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
%files -n rust-ouroboros_macro-devel -f %{oreon_filedir}/rust-ouroboros_macro-devel.list

%changelog

%autochangelog
