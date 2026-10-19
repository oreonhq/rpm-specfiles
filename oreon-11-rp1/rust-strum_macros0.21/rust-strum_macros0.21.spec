%global source0_hash d06aaeeee809dbc59eb4556183dd927df67db1540de5be8d3ec0b6636358a5ec
%bcond check 0
%global debug_package %{nil}
%global crate strum_macros
Name:           rust-strum_macros0.21
Version:        0.21.1
Release:        1%{?dist}
Summary:        Helpful macros for working with enums and strings
License:        MIT
URL:            https://crates.io/crates/strum_macros
Source0:        https://static.crates.io/crates/strum_macros/strum_macros-%{version}.crate
Patch:          strum_macros-fix-metadata.diff
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
Summary:        Helpful macros for working with enums and strings
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
%files -n rust-strum_macros0.21-devel -f %{oreon_filedir}/rust-strum_macros0.21-devel.list

%changelog

%autochangelog
