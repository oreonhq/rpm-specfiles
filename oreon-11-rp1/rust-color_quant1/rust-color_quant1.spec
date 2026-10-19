%global source0_hash 3d7b894f5411737b7867f4827955924d7c254fc9f4d91a6aad6b097804b1018b
%bcond check 1
%global debug_package %{nil}
%global crate color_quant
Name:           rust-color_quant1
Version:        1.1.0
Release:        1%{?dist}
Summary:        Color quantization library to reduce n colors to 256 colors
License:        MIT
URL:            https://crates.io/crates/color_quant
Source0:        https://static.crates.io/crates/color_quant/color_quant-%{version}.crate
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
Summary:        Color quantization library to reduce n colors to 256 colors
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
%files -n rust-color_quant1-devel -f %{oreon_filedir}/rust-color_quant1-devel.list

%changelog

%autochangelog
