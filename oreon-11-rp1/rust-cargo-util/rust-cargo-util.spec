%global source0_hash dbe819082beae53247a2c440bece59bc2d1d90736cf5bed6b87f5e5bb53f0d30
%bcond check 1
%global debug_package %{nil}
%global crate cargo-util
Name:           rust-cargo-util
Version:        0.2.32
Release:        1%{?dist}
Summary:        Miscellaneous support code used by Cargo
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo-util
Source0:        https://static.crates.io/crates/cargo-util/cargo-util-%{version}.crate
Patch:          cargo-util-fix-metadata-auto.diff
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
Summary:        Miscellaneous support code used by Cargo
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
%files -n rust-cargo-util-devel -f %{oreon_filedir}/rust-cargo-util-devel.list

%changelog

%autochangelog
