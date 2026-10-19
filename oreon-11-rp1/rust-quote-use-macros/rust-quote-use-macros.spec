%global source10_hash 522c909460ec03b8ea01e5126d2948fb55897f613fd3520c86546d8268c90ad8
%global source0_hash 8cf1c5de6a7cc231c71e03c77aa4c7019097859ea7029156b54d2894a8430704
%bcond check 1
%global debug_package %{nil}
%global crate quote-use-macros
Name:           rust-quote-use-macros
Version:        0.9.0
Release:        1%{?dist}
Summary:        Support use in procmacros hygienically
License:        MIT
URL:            https://crates.io/crates/quote-use-macros
Source0:        https://static.crates.io/crates/quote-use-macros/quote-use-macros-%{version}.crate
Source10:       https://github.com/ModProg/quote-use/raw/e4b59902f6af22b8317714e4e7ec695c0fc9e621/LICENSE
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
Summary:        Support use in procmacros hygienically
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' .
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
%files -n rust-quote-use-macros-devel -f %{oreon_filedir}/rust-quote-use-macros-devel.list

%changelog

%autochangelog
