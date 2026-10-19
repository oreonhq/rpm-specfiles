%global source0_hash 1f3ccbac311fea05f86f61904b462b55fb3df8837a366dfc601a0161d0532f20
%bcond_without check
%global debug_package %{nil}
%global crate tinyvec_macros
Name:           rust-tinyvec_macros
Version:        0.1.1
Release:        1%{?dist}
Summary:        Some macros for tiny containers
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/tinyvec_macros
Source0:        https://static.crates.io/crates/tinyvec_macros/tinyvec_macros-%{version}.crate
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
Summary:        Some macros for tiny containers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
%files -n rust-tinyvec_macros-devel -f %{oreon_filedir}/rust-tinyvec_macros-devel.list

%changelog

%autochangelog
