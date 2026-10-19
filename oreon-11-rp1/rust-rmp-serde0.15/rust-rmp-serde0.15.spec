%global source0_hash 723ecff9ad04f4ad92fe1c8ca6c20d2196d9286e9c60727c4cb5511629260e9d
%bcond check 1
%global debug_package %{nil}
%global crate rmp-serde
Name:           rust-rmp-serde0.15
Version:        0.15.5
Release:        1%{?dist}
Summary:        Serde bindings for RMP
License:        MIT
URL:            https://crates.io/crates/rmp-serde
Source0:        https://static.crates.io/crates/rmp-serde/rmp-serde-%{version}.crate
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
Summary:        Serde bindings for RMP
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde128-devel
Summary:        Serde bindings for RMP
BuildArch:      noarch
%description -n %{name}+serde128-devel

This package contains library source intended for building other packages which
use the "serde128" feature of the "%{crate}" crate.

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
%files -n rust-rmp-serde0.15-devel -f %{oreon_filedir}/rust-rmp-serde0.15-devel.list

%changelog

%autochangelog
