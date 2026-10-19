%global source0_hash b6ac1e58cded18cb28ddc17143c4dea5345b3ad575e14f32f66e4054a56eb271
%bcond check 1
%global debug_package %{nil}
%global crate actix_derive
Name:           rust-actix_derive
Version:        0.6.2
Release:        1%{?dist}
Summary:        Derive macros for actix actors
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix_derive
Source0:        https://static.crates.io/crates/actix_derive/actix_derive-%{version}.crate
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
Summary:        Derive macros for actix actors
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
%files -n rust-actix_derive-devel -f %{oreon_filedir}/rust-actix_derive-devel.list

%changelog

%autochangelog
