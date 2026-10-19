%global source1_hash d8870d5e2ab20fc50915b711c5aa7588131c9abcc1bcb980da1efd7486522a46
%global source0_hash 7f6fde18ff429ffc8fe78e2bf7f8b7a5a5a6e2a8b58bc5a9ac69198bbda9189c
%bcond check 1
%global debug_package %{nil}
%global crate phf_macros
Name:           rust-phf_macros0.8
Version:        0.8.0
Release:        1%{?dist}
Summary:        Macros to generate types in the phf crate
License:        MIT
URL:            https://crates.io/crates/phf_macros
Source0:        https://static.crates.io/crates/phf_macros/phf_macros-%{version}.crate
Source1:        https://github.com/rust-phf/rust-phf/raw/v%{version}/LICENSE
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
Summary:        Macros to generate types in the phf crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-phf_macros0.8-devel -f %{oreon_filedir}/rust-phf_macros0.8-devel.list

%changelog

%autochangelog
