%global source0_hash 0a025752d8cae2f96a9215b34187f4cbbe96d5df0511575fbbdb8882700877c8
%bcond check 0
%global debug_package %{nil}
%global crate nu-derive-value
Name:           rust-nu-derive-value
Version:        0.99.1
Release:        1%{?dist}
Summary:        Macros implementation of #[derive(FromValue, IntoValue)]
License:        MIT
URL:            https://crates.io/crates/nu-derive-value
Source0:        https://static.crates.io/crates/nu-derive-value/nu-derive-value-%{version}.crate
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
Summary:        Macros implementation of #[derive(FromValue, IntoValue)]
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
%files -n rust-nu-derive-value-devel -f %{oreon_filedir}/rust-nu-derive-value-devel.list

%changelog

%autochangelog
