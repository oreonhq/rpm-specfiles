%global source0_hash 90e502fe5db321c6e0ae649ccda600675680125a8e8dee327744fe1910b19332
%bcond check 1
%global debug_package %{nil}
%global crate neli-proc-macros
Name:           rust-neli-proc-macros
Version:        0.2.1
Release:        1%{?dist}
Summary:        Procedural macros for neli
License:        BSD-3-Clause
URL:            https://crates.io/crates/neli-proc-macros
Source0:        https://static.crates.io/crates/neli-proc-macros/neli-proc-macros-%{version}.crate
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
Summary:        Procedural macros for neli
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
%files -n rust-neli-proc-macros-devel -f %{oreon_filedir}/rust-neli-proc-macros-devel.list

%changelog

%autochangelog
