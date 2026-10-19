%global source0_hash 0f814dd8cbb812233751ff6857b7fa86d9f52e88ac64e8f54e7a1ca0168f03da
%bcond check 0
%global debug_package %{nil}
%global crate const-default-derive
Name:           rust-const-default-derive
Version:        0.2.0
Release:        1%{?dist}
Summary:        #[derive(ConstDefault)]
License:        MIT
URL:            https://crates.io/crates/const-default-derive
Source0:        https://static.crates.io/crates/const-default-derive/const-default-derive-%{version}.crate
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
Summary:        #[derive(ConstDefault)]
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
%files -n rust-const-default-derive-devel -f %{oreon_filedir}/rust-const-default-derive-devel.list

%changelog

%autochangelog
