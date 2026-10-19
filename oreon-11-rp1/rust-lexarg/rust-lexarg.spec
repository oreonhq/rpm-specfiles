%global source0_hash 84373d01a60bb462a2e7caa28796669692d38ba075028a656bd626ac211062d4
%bcond check 1
%global debug_package %{nil}
%global crate lexarg
Name:           rust-lexarg
Version:        0.0.2
Release:        1%{?dist}
Summary:        Minimal, API stable CLI parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lexarg
Source0:        https://static.crates.io/crates/lexarg/lexarg-%{version}.crate
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
Summary:        Minimal, API stable CLI parser
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
%files -n rust-lexarg-devel -f %{oreon_filedir}/rust-lexarg-devel.list

%changelog

%autochangelog
