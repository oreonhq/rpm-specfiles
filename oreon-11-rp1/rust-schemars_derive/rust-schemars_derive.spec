%global source0_hash d98c67716b46af2f0b8cf752abc930f6f9aecfbf671ecfb531db8a31dbe4e2ba
%bcond check 1
%global debug_package %{nil}
%global crate schemars_derive
Name:           rust-schemars_derive
Version:        1.2.2
Release:        1%{?dist}
Summary:        Macros for #[derive(JsonSchema)], for use with schemars
License:        MIT
URL:            https://crates.io/crates/schemars_derive
Source0:        https://static.crates.io/crates/schemars_derive/schemars_derive-%{version}.crate
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
Summary:        Macros for #[derive(JsonSchema)], for use with schemars
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
%files -n rust-schemars_derive-devel -f %{oreon_filedir}/rust-schemars_derive-devel.list

%changelog

%autochangelog
