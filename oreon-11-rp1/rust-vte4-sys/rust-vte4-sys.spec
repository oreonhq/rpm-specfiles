%global source0_hash 2c1aa57d29283c6eeac2e34c16791436275d254ac02b8590b02698feef197234
%bcond check 0
%global debug_package %{nil}
%global crate vte4-sys
Name:           rust-vte4-sys
Version:        0.8.0
Release:        1%{?dist}
Summary:        FFI bindings to vte-2.91-gtk4
License:        MIT
URL:            https://crates.io/crates/vte4-sys
Source0:        https://static.crates.io/crates/vte4-sys/vte4-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(vte-2.91-gtk4)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to vte-2.91-gtk4
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v0_66-devel
Summary:        FFI bindings to vte-2.91-gtk4
BuildArch:      noarch
Requires:       pkgconfig(vte-2.91-gtk4) >= 0.66
%description -n %{name}+v0_66-devel

This package contains library source intended for building other packages which
use the "v0_66" feature of the "%{crate}" crate.

%package     -n %{name}+v0_70-devel
Summary:        FFI bindings to vte-2.91-gtk4
BuildArch:      noarch
Requires:       pkgconfig(vte-2.91-gtk4) >= 0.70
%description -n %{name}+v0_70-devel

This package contains library source intended for building other packages which
use the "v0_70" feature of the "%{crate}" crate.

%package     -n %{name}+v0_72-devel
Summary:        FFI bindings to vte-2.91-gtk4
BuildArch:      noarch
Requires:       pkgconfig(vte-2.91-gtk4) >= 0.72
%description -n %{name}+v0_72-devel

This package contains library source intended for building other packages which
use the "v0_72" feature of the "%{crate}" crate.

%package     -n %{name}+v0_74-devel
Summary:        FFI bindings to vte-2.91-gtk4
BuildArch:      noarch
Requires:       pkgconfig(vte-2.91-gtk4) >= 0.74
%description -n %{name}+v0_74-devel

This package contains library source intended for building other packages which
use the "v0_74" feature of the "%{crate}" crate.

%package     -n %{name}+v0_76-devel
Summary:        FFI bindings to vte-2.91-gtk4
BuildArch:      noarch
%description -n %{name}+v0_76-devel

This package contains library source intended for building other packages which
use the "v0_76" feature of the "%{crate}" crate.

%package     -n %{name}+v0_78-devel
Summary:        FFI bindings to vte-2.91-gtk4
BuildArch:      noarch
%description -n %{name}+v0_78-devel

This package contains library source intended for building other packages which
use the "v0_78" feature of the "%{crate}" crate.

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
%files -n rust-vte4-sys-devel -f %{oreon_filedir}/rust-vte4-sys-devel.list

%changelog

%autochangelog
