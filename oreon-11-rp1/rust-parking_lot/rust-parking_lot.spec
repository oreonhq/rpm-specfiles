%global source0_hash 93857453250e3077bd71ff98b6a65ea6621a19bb0f559a85248955ac12c45a1a
%bcond check 0
%global debug_package %{nil}
%global crate parking_lot
Name:           rust-parking_lot
Version:        0.12.5
Release:        1%{?dist}
Summary:        More compact and efficient implementations of the standard synchroniz...
License:        MIT OR Apache-2.0
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

%package     -n %{name}+hardware-lock-elision-devel
Summary:        More compact and efficient implementations of the standard synchroniz...
BuildArch:      noarch
%description -n %{name}+hardware-lock-elision-devel

This package contains library source intended for building other packages which
use the "hardware-lock-elision" feature of the "%{crate}" crate.

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
%files -n rust-parking_lot-devel -f %{oreon_filedir}/rust-parking_lot-devel.list

%changelog

%autochangelog
