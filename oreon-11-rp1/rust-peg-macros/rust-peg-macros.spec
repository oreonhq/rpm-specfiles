%global source0_hash ddd8ef6825cae95355031ae26a99b616a2a21f22ba2de0197c43dfb05acbe7ee
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate peg-macros
Name:           rust-peg-macros
Version:        0.8.6
Release:        1%{?dist}
Summary:        Procedural macros for rust-peg
License:        MIT
URL:            https://crates.io/crates/peg-macros
Source0:        https://static.crates.io/crates/peg-macros/peg-macros-%{version}.crate
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
Summary:        Procedural macros for rust-peg
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        Procedural macros for rust-peg
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

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
%files -n rust-peg-macros-devel -f %{oreon_filedir}/rust-peg-macros-devel.list

%changelog

%autochangelog
