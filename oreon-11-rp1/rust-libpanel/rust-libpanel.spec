%global source0_hash d7b5907dc844dc9cd243d810881e081d7e56088f28c08ac37fdc49d86e390238
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate libpanel
Name:           rust-libpanel
Version:        0.5.0
Release:        1%{?dist}
Summary:        Rust bindings for GNOME libpanel
License:        MIT
URL:            https://crates.io/crates/libpanel
Source0:        https://static.crates.io/crates/libpanel/libpanel-%{version}.crate
Patch:          libpanel-fix-metadata.diff
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
Summary:        Rust bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+adw_v1_2-devel
Summary:        Rust bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+adw_v1_2-devel

This package contains library source intended for building other packages which
use the "adw_v1_2" feature of the "%{crate}" crate.

%package     -n %{name}+v1_2-devel
Summary:        Rust bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+v1_2-devel

This package contains library source intended for building other packages which
use the "v1_2" feature of the "%{crate}" crate.

%package     -n %{name}+v1_4-devel
Summary:        Rust bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+v1_4-devel

This package contains library source intended for building other packages which
use the "v1_4" feature of the "%{crate}" crate.

%package     -n %{name}+v1_8-devel
Summary:        Rust bindings for GNOME libpanel
BuildArch:      noarch
%description -n %{name}+v1_8-devel

This package contains library source intended for building other packages which
use the "v1_8" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rf examples
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
%files -n rust-libpanel-devel -f %{oreon_filedir}/rust-libpanel-devel.list

%changelog

%autochangelog
