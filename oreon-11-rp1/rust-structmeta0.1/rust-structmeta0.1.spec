%global source0_hash 104842d6278bf64aa9d2f182ba4bde31e8aec7a131d29b7f444bb9b344a09e2a
%bcond check 0
%global debug_package %{nil}
%global crate structmeta
Name:           rust-structmeta0.1
Version:        0.1.6
Release:        1%{?dist}
Summary:        Parse Rust's attribute arguments by defining a struct.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/structmeta
Source0:        https://static.crates.io/crates/structmeta/structmeta-%{version}.crate
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
Summary:        Parse Rust's attribute arguments by defining a struct.
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
%files -n rust-structmeta0.1-devel -f %{oreon_filedir}/rust-structmeta0.1-devel.list

%changelog

%autochangelog
