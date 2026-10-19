%global source0_hash bda66b810a62be75176a80873726630147a5ca780cd33921e0b5709033e66b0a
%bcond check 1
%global debug_package %{nil}
%global crate parking_lot_core
Name:           rust-parking_lot_core0.6
Version:        0.6.3
Release:        1%{?dist}
Summary:        Advanced API for creating custom synchronization primitives
License:        Apache-2.0 OR MIT
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
Summary:        Advanced API for creating custom synchronization primitives
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Advanced API for creating custom synchronization primitives
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+deadlock_detection-devel
Summary:        Advanced API for creating custom synchronization primitives
BuildArch:      noarch
%description -n %{name}+deadlock_detection-devel

This package contains library source intended for building other packages which
use the "deadlock_detection" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Advanced API for creating custom synchronization primitives
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+petgraph-devel
Summary:        Advanced API for creating custom synchronization primitives
BuildArch:      noarch
%description -n %{name}+petgraph-devel

This package contains library source intended for building other packages which
use the "petgraph" feature of the "%{crate}" crate.

%package     -n %{name}+thread-id-devel
Summary:        Advanced API for creating custom synchronization primitives
BuildArch:      noarch
%description -n %{name}+thread-id-devel

This package contains library source intended for building other packages which
use the "thread-id" feature of the "%{crate}" crate.

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
%files -n rust-parking_lot_core0.6-devel -f %{oreon_filedir}/rust-parking_lot_core0.6-devel.list

%changelog

%autochangelog
