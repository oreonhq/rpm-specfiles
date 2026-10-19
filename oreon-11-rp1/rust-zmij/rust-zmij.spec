%global source0_hash 29666d0abbfad1e3dc4dcf6144730dd3a3ab225bbbdac83319345b1b44ccfc1b
%bcond check 0
%global debug_package %{nil}
%global crate zmij
Name:           rust-zmij
Version:        1.0.23
Release:        1%{?dist}
Summary:        Double-to-string conversion algorithm based on Schubfach and yy
License:        MIT
URL:            https://crates.io/crates/zmij
Source0:        https://static.crates.io/crates/zmij/zmij-%{version}.crate
Patch:          zmij-fix-metadata.diff
Patch2:         0001-drop-unnecessary-opt-level-crate-API-calls.patch
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
Summary:        Double-to-string conversion algorithm based on Schubfach and yy
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no-panic-devel
Summary:        Double-to-string conversion algorithm based on Schubfach and yy
BuildArch:      noarch
%description -n %{name}+no-panic-devel

This package contains library source intended for building other packages which
use the "no-panic" feature of the "%{crate}" crate.

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
%files -n rust-zmij-devel -f %{oreon_filedir}/rust-zmij-devel.list

%changelog

%autochangelog
