%global source0_hash a8f355e230af5c0f5f95c46c5aeca3ce7bcb4e3e73300b44d7064b281ec8f124
%bcond check 0
%global debug_package %{nil}
%global crate powerfmt-macros
Name:           rust-powerfmt-macros
Version:        0.1.0
Release:        2%{?dist}
Summary:        Procedural macros for `powerfmt`.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/powerfmt-macros
Source0:        https://static.crates.io/crates/powerfmt-macros/powerfmt-macros-%{version}.crate
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
Summary:        Procedural macros for `powerfmt`.
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
%files -n rust-powerfmt-macros-devel -f %{oreon_filedir}/rust-powerfmt-macros-devel.list

%changelog

%autochangelog
