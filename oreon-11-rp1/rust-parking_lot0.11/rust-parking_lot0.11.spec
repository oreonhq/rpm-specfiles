%global source0_hash 7d17b78036a60663b797adeaee46f5c9dfebb86948d1255007a1d6be0271ff99
%bcond check 0
%global debug_package %{nil}
%global crate parking_lot
Name:           rust-parking_lot0.11
Version:        0.11.2
Release:        1%{?dist}
Summary:        More compact and efficient implementations of the standard synchroniz...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/parking_lot
Source0:        https://static.crates.io/crates/parking_lot/parking_lot-%{version}.crate
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
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc_lock-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+arc_lock-devel

This package contains library source intended for building other packages which
use the "arc_lock" feature of the "%{crate}" crate.

%package     -n %{name}+deadlock_detection-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+deadlock_detection-devel

This package contains library source intended for building other packages which
use the "deadlock_detection" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+owning_ref-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+owning_ref-devel

This package contains library source intended for building other packages which
use the "owning_ref" feature of the "%{crate}" crate.

%package     -n %{name}+send_guard-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+send_guard-devel

This package contains library source intended for building other packages which
use the "send_guard" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+stdweb-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+stdweb-devel

This package contains library source intended for building other packages which
use the "stdweb" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-bindgen-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+wasm-bindgen-devel

This package contains library source intended for building other packages which
use the "wasm-bindgen" feature of the "%{crate}" crate.

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
%files -n rust-parking_lot0.11-devel -f %{oreon_filedir}/rust-parking_lot0.11-devel.list

%changelog

%autochangelog
