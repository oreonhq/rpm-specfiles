%global source0_hash a1249a628de3ad34b821ecb1001355bca3940bcb2f88558f1a8bd82e977f75b5
%bcond check 1
%global debug_package %{nil}
%global crate unic-langid-macros-impl
Name:           rust-unic-langid-macros-impl
Version:        0.9.6
Release:        1%{?dist}
Summary:        API for managing Unicode Language Identifiers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-langid-macros-impl
Source0:        https://static.crates.io/crates/unic-langid-macros-impl/unic-langid-macros-impl-%{version}.crate
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
Summary:        API for managing Unicode Language Identifiers
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
%files -n rust-unic-langid-macros-impl-devel -f %{oreon_filedir}/rust-unic-langid-macros-impl-devel.list

%changelog

%autochangelog
