%global source0_hash f0805222e57f7521d6a62e36fa9163bc891acd422f971defe97d64e70d0a4fe5
%bcond check 1
%global debug_package %{nil}
%global crate windows-link
Name:           rust-windows-link
Version:        0.2.1
Release:        2%{?dist}
Summary:        Linking for Windows
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/windows-link
Source0:        https://static.crates.io/crates/windows-link/windows-link-%{version}.crate
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
Summary:        Linking for Windows
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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-windows-link-devel -f %{oreon_filedir}/rust-windows-link-devel.list

%changelog

%autochangelog
