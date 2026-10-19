%global source0_hash ba7795da175654fe16979af73f81f26a8ea27638d8d9823d317016888a63dc4c
%bcond check 0
%global debug_package %{nil}
%global crate enum-primitive-derive
Name:           rust-enum-primitive-derive
Version:        0.3.0
Release:        1%{?dist}
Summary:        Enum_primitive implementation using procedural macros to have a custom derive
License:        MIT
URL:            https://crates.io/crates/enum-primitive-derive
Source0:        https://static.crates.io/crates/enum-primitive-derive/enum-primitive-derive-%{version}.crate
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
Summary:        Enum_primitive implementation using procedural macros to have a custom derive
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
%files -n rust-enum-primitive-derive-devel -f %{oreon_filedir}/rust-enum-primitive-derive-devel.list

%changelog

%autochangelog
