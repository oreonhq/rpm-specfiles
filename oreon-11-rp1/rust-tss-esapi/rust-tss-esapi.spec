%global source0_hash 3f10b25a84912b894d0e6d68f4a3771c923e9c44ddaaed7920cde92ed28aa84e
%bcond check 0
%global debug_package %{nil}
%global crate tss-esapi
Name:           rust-tss-esapi
Version:        7.7.0
Release:        1%{?dist}
Summary:        Rust-native wrapper around TSS 2.0 Enhanced System API
License:        Apache-2.0
URL:            https://crates.io/crates/tss-esapi
Source0:        https://static.crates.io/crates/tss-esapi/tss-esapi-%{version}.crate
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

%package     -n %{name}+generate-bindings-devel
Summary:        Rust-native wrapper around TSS 2.0 Enhanced System API
BuildArch:      noarch
%description -n %{name}+generate-bindings-devel

This package contains library source intended for building other packages which
use the "generate-bindings" feature of the "%{crate}" crate.

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
%files -n rust-tss-esapi-devel -f %{oreon_filedir}/rust-tss-esapi-devel.list

%changelog

%autochangelog
