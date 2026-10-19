%global source0_hash c61732974d4915c5112a82506cdc86e19a83d786497c2c8bcd80d065825c695d
%bcond check 0
%global debug_package %{nil}
%global crate vte4
Name:           rust-vte4
Version:        0.10.0
Release:        1%{?dist}
Summary:        Rust bindings for the VTE Gtk4 library
License:        MIT
URL:            https://crates.io/crates/vte4
Source0:        https://static.crates.io/crates/vte4/vte4-%{version}.crate
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
Summary:        Rust bindings for the VTE Gtk4 library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v0_66-devel
Summary:        Rust bindings for the VTE Gtk4 library
BuildArch:      noarch
%description -n %{name}+v0_66-devel

This package contains library source intended for building other packages which
use the "v0_66" feature of the "%{crate}" crate.

%package     -n %{name}+v0_70-devel
Summary:        Rust bindings for the VTE Gtk4 library
BuildArch:      noarch
%description -n %{name}+v0_70-devel

This package contains library source intended for building other packages which
use the "v0_70" feature of the "%{crate}" crate.

%package     -n %{name}+v0_72-devel
Summary:        Rust bindings for the VTE Gtk4 library
BuildArch:      noarch
%description -n %{name}+v0_72-devel

This package contains library source intended for building other packages which
use the "v0_72" feature of the "%{crate}" crate.

%package     -n %{name}+v0_74-devel
Summary:        Rust bindings for the VTE Gtk4 library
BuildArch:      noarch
%description -n %{name}+v0_74-devel

This package contains library source intended for building other packages which
use the "v0_74" feature of the "%{crate}" crate.

%package     -n %{name}+v0_76-devel
Summary:        Rust bindings for the VTE Gtk4 library
BuildArch:      noarch
%description -n %{name}+v0_76-devel

This package contains library source intended for building other packages which
use the "v0_76" feature of the "%{crate}" crate.

%package     -n %{name}+v0_78-devel
Summary:        Rust bindings for the VTE Gtk4 library
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-vte4-devel -f %{oreon_filedir}/rust-vte4-devel.list

%changelog

%autochangelog
