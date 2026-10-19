%global source0_hash 10d60334b3b2e7c9d91ef8150abfb6fa4c1c39ebbcf4a81c2e346aad939fee3e
%bcond check 0
%global debug_package %{nil}
%global crate defmt-parser
Name:           rust-defmt-parser
Version:        1.0.0
Release:        1%{?dist}
Summary:        Parsing library for defmt format strings
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/defmt-parser
Source0:        https://static.crates.io/crates/defmt-parser/defmt-parser-%{version}.crate
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

%package     -n %{name}+unstable-devel
Summary:        Parsing library for defmt format strings
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-defmt-parser-devel -f %{oreon_filedir}/rust-defmt-parser-devel.list

%changelog

%autochangelog
