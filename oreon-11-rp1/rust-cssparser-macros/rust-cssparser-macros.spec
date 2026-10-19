%global source0_hash d045de693cb712d0b22c6a64be5b953f67b3ce00ab5ad3dd5d8b441886ab8e1a
%bcond check 0
%global debug_package %{nil}
%global crate cssparser-macros
Name:           rust-cssparser-macros
Version:        0.7.1
Release:        1%{?dist}
Summary:        Procedural macros for cssparser
License:        MPL-2.0
URL:            https://crates.io/crates/cssparser-macros
Source0:        https://static.crates.io/crates/cssparser-macros/cssparser-macros-%{version}.crate
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
Summary:        Procedural macros for cssparser
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
%files -n rust-cssparser-macros-devel -f %{oreon_filedir}/rust-cssparser-macros-devel.list

%changelog

%autochangelog
