%global source0_hash 6442248665a5aa2514e794af3b39661a8e73033b1cc5e59899e1276117ee4400
%bcond check 1
%global debug_package %{nil}
%global crate notify-rust
Name:           rust-notify-rust
Version:        4.11.7
Release:        1%{?dist}
Summary:        Show desktop notifications
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/notify-rust
Source0:        https://static.crates.io/crates/notify-rust/notify-rust-%{version}.crate
Patch:          notify-rust-fix-metadata-auto.diff
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
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+d-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+d-devel

This package contains library source intended for building other packages which
use the "d" feature of the "%{crate}" crate.

%package     -n %{name}+dbus-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+dbus-devel

This package contains library source intended for building other packages which
use the "dbus" feature of the "%{crate}" crate.

%package     -n %{name}+debug_namespace-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+debug_namespace-devel

This package contains library source intended for building other packages which
use the "debug_namespace" feature of the "%{crate}" crate.

%package     -n %{name}+env_logger-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+env_logger-devel

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+images-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+images-devel

This package contains library source intended for building other packages which
use the "images" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+lazy_static-devel

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+z-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+z-devel

This package contains library source intended for building other packages which
use the "z" feature of the "%{crate}" crate.

%package     -n %{name}+zbus-devel
Summary:        Show desktop notifications
BuildArch:      noarch
%description -n %{name}+zbus-devel

This package contains library source intended for building other packages which
use the "zbus" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip realworld
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-notify-rust-devel -f %{oreon_filedir}/rust-notify-rust-devel.list

%changelog

%autochangelog
