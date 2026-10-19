%global source0_hash c3464313de0c867016e3e69d7e1e9ae3499bcc4c18e12283d381359ed38b5b9e
%bcond check 0
%global debug_package %{nil}
%global crate assert-impl
Name:           rust-assert-impl
Version:        0.1.3
Release:        1%{?dist}
Summary:        Macro for static assert types implement a trait or not
License:        MIT
URL:            https://crates.io/crates/assert-impl
Source0:        https://static.crates.io/crates/assert-impl/assert-impl-%{version}.crate
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
Summary:        Macro for static assert types implement a trait or not
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
%files -n rust-assert-impl-devel -f %{oreon_filedir}/rust-assert-impl-devel.list

%changelog

%autochangelog
