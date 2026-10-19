%global source0_hash fcba141ce511bad08e80b43f02976571072e1ff4286f7d628943efbd277c6361
%bcond check 1
%global debug_package %{nil}
%global crate uutils_term_grid
Name:           rust-uutils_term_grid
Version:        0.7.0
Release:        1%{?dist}
Summary:        Library for formatting strings into a grid layout. Fork of term_grid
License:        MIT
URL:            https://crates.io/crates/uutils_term_grid
Source0:        https://static.crates.io/crates/uutils_term_grid/uutils_term_grid-%{version}.crate
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
Summary:        Library for formatting strings into a grid layout. Fork of term_grid
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
%files -n rust-uutils_term_grid-devel -f %{oreon_filedir}/rust-uutils_term_grid-devel.list

%changelog

%autochangelog
