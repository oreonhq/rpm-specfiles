%global source0_hash 578a7433b776b56a35785ed5ce9a7e777ac0598aac5a6dd1b4b18a307c7fc71b
%bcond check 0
%global debug_package %{nil}
%global crate serde_yaml
Name:           rust-serde_yaml0.8
Version:        0.8.26
Release:        1%{?dist}
Summary:        YAML support for Serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_yaml
Source0:        https://static.crates.io/crates/serde_yaml/serde_yaml-%{version}.crate
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
Summary:        YAML support for Serde
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
%files -n rust-serde_yaml0.8-devel -f %{oreon_filedir}/rust-serde_yaml0.8-devel.list

%changelog

%autochangelog
