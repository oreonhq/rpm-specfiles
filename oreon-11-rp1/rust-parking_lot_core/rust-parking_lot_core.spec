%global source0_hash 2621685985a2ebf1c516881c026032ac7deafcda1a2c9b7850dc81e3dfcb64c1
%bcond check 0
%global debug_package %{nil}
%global crate parking_lot_core
Name:           rust-parking_lot_core
Version:        0.9.12
Release:        1%{?dist}
Summary:        An advanced API for creating custom synchronization primitives.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/parking_lot_core
Source0:        https://static.crates.io/crates/parking_lot_core/parking_lot_core-%{version}.crate
Patch:          parking_lot_core-fix-metadata-auto.diff
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
Summary:        An advanced API for creating custom synchronization primitives.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        An advanced API for creating custom synchronization primitives.
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+deadlock_detection-devel
Summary:        An advanced API for creating custom synchronization primitives.
BuildArch:      noarch
%description -n %{name}+deadlock_detection-devel

This package contains library source intended for building other packages which
use the "deadlock_detection" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        An advanced API for creating custom synchronization primitives.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+petgraph-devel
Summary:        An advanced API for creating custom synchronization primitives.
BuildArch:      noarch
%description -n %{name}+petgraph-devel

This package contains library source intended for building other packages which
use the "petgraph" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -i '/target_os = "redox"/,/^$/d' Cargo.toml
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
%files -n rust-parking_lot_core-devel -f %{oreon_filedir}/rust-parking_lot_core-devel.list

%changelog

%autochangelog
