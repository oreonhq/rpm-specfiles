%global source0_hash b7186006dcb21920990093f30e3dea63b7d6e977bf1256be20c3563a5db070da
%bcond check 0
%global debug_package %{nil}
%global crate ref-cast-impl
Name:           rust-ref-cast-impl
Version:        1.0.25
Release:        1%{?dist}
Summary:        Derive implementation for ref_cast::RefCast
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ref-cast-impl
Source0:        https://static.crates.io/crates/ref-cast-impl/ref-cast-impl-%{version}.crate
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
Summary:        Derive implementation for ref_cast::RefCast
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
%files -n rust-ref-cast-impl-devel -f %{oreon_filedir}/rust-ref-cast-impl-devel.list

%changelog

%autochangelog
