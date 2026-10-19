%global source0_hash ed93ba1a9ffcca32130a5188701c81c0c49cf00d4b7c5007d5148951d743adcb
%bcond check 0
%global debug_package %{nil}
%global crate pest_meta
Name:           rust-pest_meta
Version:        2.9.2
Release:        1%{?dist}
Summary:        pest meta language parser and validator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pest_meta
Source0:        https://static.crates.io/crates/pest_meta/pest_meta-%{version}.crate
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
Summary:        pest meta language parser and validator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+grammar-extras-devel
Summary:        pest meta language parser and validator
BuildArch:      noarch
%description -n %{name}+grammar-extras-devel

This package contains library source intended for building other packages which
use the "grammar-extras" feature of the "%{crate}" crate.

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
%files -n rust-pest_meta-devel -f %{oreon_filedir}/rust-pest_meta-devel.list

%changelog

%autochangelog
