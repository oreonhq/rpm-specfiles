%global source0_hash 3ab69f03cc8c4340c9c8e315114e1658e6775a9b16a04357973aa21cec22b32e
%bcond check 0
%global debug_package %{nil}
%global crate dbus
Name:           rust-dbus
Version:        0.9.12
Release:        1%{?dist}
Summary:        Bindings to D-Bus
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/dbus
Source0:        https://static.crates.io/crates/dbus/dbus-%{version}.crate
Patch:          dbus-fix-metadata-auto.diff
Patch:          dbus-fix-metadata.diff
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
Summary:        Bindings to D-Bus
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Bindings to D-Bus
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-channel-devel
Summary:        Bindings to D-Bus
BuildArch:      noarch
%description -n %{name}+futures-channel-devel

This package contains library source intended for building other packages which
use the "futures-channel" feature of the "%{crate}" crate.

%package     -n %{name}+futures-executor-devel
Summary:        Bindings to D-Bus
BuildArch:      noarch
%description -n %{name}+futures-executor-devel

This package contains library source intended for building other packages which
use the "futures-executor" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Bindings to D-Bus
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+no-string-validation-devel
Summary:        Bindings to D-Bus
BuildArch:      noarch
%description -n %{name}+no-string-validation-devel

This package contains library source intended for building other packages which
use the "no-string-validation" feature of the "%{crate}" crate.

%package     -n %{name}+stdfd-devel
Summary:        Bindings to D-Bus
BuildArch:      noarch
%description -n %{name}+stdfd-devel

This package contains library source intended for building other packages which
use the "stdfd" feature of the "%{crate}" crate.

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
%files -n rust-dbus-devel -f %{oreon_filedir}/rust-dbus-devel.list

%changelog

%autochangelog
