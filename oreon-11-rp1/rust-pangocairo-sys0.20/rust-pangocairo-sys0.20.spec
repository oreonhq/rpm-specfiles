%global source0_hash b9952903f88aa93e2927e7bca2d1ebae64fc26545a9280b4ce6bddeda26b5c42
%bcond check 0
%global debug_package %{nil}
%global crate pangocairo-sys
Name:           rust-pangocairo-sys0.20
Version:        0.20.10
Release:        1%{?dist}
Summary:        FFI bindings to PangoCairo
License:        MIT
URL:            https://crates.io/crates/pangocairo-sys
Source0:        https://static.crates.io/crates/pangocairo-sys/pangocairo-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pangocairo) >= 1.40
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to PangoCairo
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
%files -n rust-pangocairo-sys0.20-devel -f %{oreon_filedir}/rust-pangocairo-sys0.20-devel.list

%changelog

%autochangelog
