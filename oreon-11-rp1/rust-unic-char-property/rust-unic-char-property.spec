%global source0_hash a8c57a407d9b6fa02b4795eb81c5b6652060a15a7903ea981f3d723e6c0be221
%bcond check 1
%global debug_package %{nil}
%global crate unic-char-property
Name:           rust-unic-char-property
Version:        0.9.0
Release:        1%{?dist}
Summary:        UNIC — Unicode Character Tools — Character Property taxonomy,
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-char-property
Source0:        https://static.crates.io/crates/unic-char-property/unic-char-property-%{version}.crate
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
Summary:        UNIC — Unicode Character Tools — Character Property taxonomy,
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
%files -n rust-unic-char-property-devel -f %{oreon_filedir}/rust-unic-char-property-devel.list

%changelog

%autochangelog
