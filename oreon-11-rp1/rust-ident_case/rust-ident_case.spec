%global source0_hash b9e0384b61958566e926dc50660321d12159025e767c18e043daf26b70104c39
%bcond check 0
%global debug_package %{nil}
%global crate ident_case
Name:           rust-ident_case
Version:        1.0.1
Release:        1%{?dist}
Summary:        Utility for applying case rules to Rust identifiers.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ident_case
Source0:        https://static.crates.io/crates/ident_case/ident_case-%{version}.crate
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
Summary:        Utility for applying case rules to Rust identifiers.
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
%files -n rust-ident_case-devel -f %{oreon_filedir}/rust-ident_case-devel.list

%changelog

%autochangelog
