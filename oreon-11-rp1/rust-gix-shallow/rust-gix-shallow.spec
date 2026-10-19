%global source0_hash 1ecc9f4b40537043e4bbd7d3d1760e74fb8e7b07a546166b558acaa73ad97f4a
%bcond check 0
%global debug_package %{nil}
%global crate gix-shallow
Name:           rust-gix-shallow
Version:        0.13.0
Release:        1%{?dist}
Summary:        Handle files specifying the shallow boundary
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-shallow
Source0:        https://static.crates.io/crates/gix-shallow/gix-shallow-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        Handle files specifying the shallow boundary
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-gix-shallow-devel -f %{oreon_filedir}/rust-gix-shallow-devel.list

%changelog

%autochangelog
