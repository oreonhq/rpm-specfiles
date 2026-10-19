%global source0_hash 9f7c3e4beb33f85d45ae3e3a1792185706c8e16d043238c593331cc7cd313b50
%bcond check 0
%global debug_package %{nil}
%global crate once_cell
Name:           rust-once_cell
Version:        1.21.4
Release:        1%{?dist}
Summary:        Single assignment cells and lazy values
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/once_cell
Source0:        https://static.crates.io/crates/once_cell/once_cell-%{version}.crate
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
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+atomic-polyfill-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+atomic-polyfill-devel

This package contains library source intended for building other packages which
use the "atomic-polyfill" feature of the "%{crate}" crate.

%package     -n %{name}+critical-section-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+critical-section-devel

This package contains library source intended for building other packages which
use the "critical-section" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+race-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+race-devel

This package contains library source intended for building other packages which
use the "race" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Single assignment cells and lazy values
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-once_cell-devel -f %{oreon_filedir}/rust-once_cell-devel.list

%changelog

%autochangelog
