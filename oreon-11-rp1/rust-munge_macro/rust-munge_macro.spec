%global source0_hash 4568f25ccbd45ab5d5603dc34318c1ec56b117531781260002151b8530a9f931
%bcond check 0
%global debug_package %{nil}
%global crate munge_macro
Name:           rust-munge_macro
Version:        0.4.7
Release:        1%{?dist}
Summary:        Macro for custom destructuring
License:        MIT
URL:            https://crates.io/crates/munge_macro
Source0:        https://static.crates.io/crates/munge_macro/munge_macro-%{version}.crate
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
Summary:        Macro for custom destructuring
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
%files -n rust-munge_macro-devel -f %{oreon_filedir}/rust-munge_macro-devel.list

%changelog

%autochangelog
