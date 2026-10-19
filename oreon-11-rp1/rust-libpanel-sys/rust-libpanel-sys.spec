%global source0_hash 6ddf5ff571cfd22c5cc9451a7897d6356905f3c37cb653360ac47b70e18faebb
%bcond check 0
%global debug_package %{nil}
%global crate libpanel-sys
Name:           rust-libpanel-sys
Version:        0.5.0
Release:        1%{?dist}
Summary:        FFI bindings for GNOME libpanel
License:        MIT
URL:            https://crates.io/crates/libpanel-sys
Source0:        https://static.crates.io/crates/libpanel-sys/libpanel-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libpanel-1)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v1_2-devel
Summary:        FFI bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+v1_2-devel

This package contains library source intended for building other packages which
use the "v1_2" feature of the "%{crate}" crate.

%package     -n %{name}+v1_4-devel
Summary:        FFI bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+v1_4-devel

This package contains library source intended for building other packages which
use the "v1_4" feature of the "%{crate}" crate.

%package     -n %{name}+v1_8-devel
Summary:        FFI bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+v1_8-devel

This package contains library source intended for building other packages which
use the "v1_8" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip cross_validate_constants_with_c --skip cross_validate_layout_with_c
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-libpanel-sys-devel -f %{oreon_filedir}/rust-libpanel-sys-devel.list

%changelog

%autochangelog
