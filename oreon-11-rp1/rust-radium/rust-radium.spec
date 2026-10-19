%global source0_hash dc33ff2d4973d518d823d61aa239014831e521c75da58e3df4840d3f47749d09
%bcond check 0
%global debug_package %{nil}
%global crate radium
Name:           rust-radium
Version:        0.7.0
Release:        1%{?dist}
Summary:        Portable interfaces for maybe-atomic types
License:        MIT
URL:            https://crates.io/crates/radium
Source0:        https://static.crates.io/crates/radium/radium-%{version}.crate
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
Summary:        Portable interfaces for maybe-atomic types
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
%files -n rust-radium-devel -f %{oreon_filedir}/rust-radium-devel.list

%changelog

%autochangelog
