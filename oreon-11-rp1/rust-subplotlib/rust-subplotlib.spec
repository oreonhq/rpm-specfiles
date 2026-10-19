%global source0_hash 6ddf898c1d4ef62f77028b546f7baf9c1e661c927587249da0b0fa5ec5906422
%bcond check 0
%global debug_package %{nil}
%global crate subplotlib
Name:           rust-subplotlib
Version:        0.12.0
Release:        1%{?dist}
Summary:        Utility functions and types for `subplot codegen` generated Rust based
License:        MIT-0
URL:            https://crates.io/crates/subplotlib
Source0:        https://static.crates.io/crates/subplotlib/subplotlib-%{version}.crate
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
Summary:        Utility functions and types for `subplot codegen` generated Rust based
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
%files -n rust-subplotlib-devel -f %{oreon_filedir}/rust-subplotlib-devel.list

%changelog

%autochangelog
