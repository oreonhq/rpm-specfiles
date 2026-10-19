%global source0_hash a1e6a265c649f3f5979b601d26f1d05ada116434c87741c9493cb56218f76cbc
%bcond check 1
%global debug_package %{nil}
%global crate enum-as-inner
Name:           rust-enum-as-inner0.6
Version:        0.6.1
Release:        1%{?dist}
Summary:        Proc-macro for deriving inner field accessor functions on enums
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/enum-as-inner
Source0:        https://static.crates.io/crates/enum-as-inner/enum-as-inner-%{version}.crate
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
Summary:        Proc-macro for deriving inner field accessor functions on enums
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
%files -n rust-enum-as-inner0.6-devel -f %{oreon_filedir}/rust-enum-as-inner0.6-devel.list

%changelog

%autochangelog
