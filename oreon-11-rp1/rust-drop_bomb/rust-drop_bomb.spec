%global source0_hash 9bda8e21c04aca2ae33ffc2fd8c23134f3cac46db123ba97bd9d3f3b8a4a85e1
%bcond check 0
%global debug_package %{nil}
%global crate drop_bomb
Name:           rust-drop_bomb
Version:        0.1.5
Release:        1%{?dist}
Summary:        Runtime guard for implementing linear types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/drop_bomb
Source0:        https://static.crates.io/crates/drop_bomb/drop_bomb-%{version}.crate
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
Summary:        Runtime guard for implementing linear types
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
%files -n rust-drop_bomb-devel -f %{oreon_filedir}/rust-drop_bomb-devel.list

%changelog

%autochangelog
