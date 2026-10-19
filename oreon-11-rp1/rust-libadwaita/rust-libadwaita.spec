%global source0_hash bc0da4e27b20d3e71f830e5b0f0188d22c257986bf421c02cfde777fe07932a4
%bcond check 1
%global debug_package %{nil}
%global crate libadwaita
Name:           rust-libadwaita
Version:        0.9.1
Release:        1%{?dist}
Summary:        Rust bindings for libadwaita
License:        MIT
URL:            https://crates.io/crates/libadwaita
Source0:        https://static.crates.io/crates/libadwaita/libadwaita-%{version}.crate
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
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gio_v2_80-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+gio_v2_80-devel

This package contains library source intended for building other packages which
use the "gio_v2_80" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_18-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+gtk_v4_18-devel

This package contains library source intended for building other packages which
use the "gtk_v4_18" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_2-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+gtk_v4_2-devel

This package contains library source intended for building other packages which
use the "gtk_v4_2" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_20-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+gtk_v4_20-devel

This package contains library source intended for building other packages which
use the "gtk_v4_20" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_22-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+gtk_v4_22-devel

This package contains library source intended for building other packages which
use the "gtk_v4_22" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_6-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+gtk_v4_6-devel

This package contains library source intended for building other packages which
use the "gtk_v4_6" feature of the "%{crate}" crate.

%package     -n %{name}+v1_1-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_1-devel

This package contains library source intended for building other packages which
use the "v1_1" feature of the "%{crate}" crate.

%package     -n %{name}+v1_2-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_2-devel

This package contains library source intended for building other packages which
use the "v1_2" feature of the "%{crate}" crate.

%package     -n %{name}+v1_3-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_3-devel

This package contains library source intended for building other packages which
use the "v1_3" feature of the "%{crate}" crate.

%package     -n %{name}+v1_4-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_4-devel

This package contains library source intended for building other packages which
use the "v1_4" feature of the "%{crate}" crate.

%package     -n %{name}+v1_5-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_5-devel

This package contains library source intended for building other packages which
use the "v1_5" feature of the "%{crate}" crate.

%package     -n %{name}+v1_6-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_6-devel

This package contains library source intended for building other packages which
use the "v1_6" feature of the "%{crate}" crate.

%package     -n %{name}+v1_7-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_7-devel

This package contains library source intended for building other packages which
use the "v1_7" feature of the "%{crate}" crate.

%package     -n %{name}+v1_8-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_8-devel

This package contains library source intended for building other packages which
use the "v1_8" feature of the "%{crate}" crate.

%package     -n %{name}+v1_9-devel
Summary:        Rust bindings for libadwaita
BuildArch:      noarch
%description -n %{name}+v1_9-devel

This package contains library source intended for building other packages which
use the "v1_9" feature of the "%{crate}" crate.

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
%files -n rust-libadwaita-devel -f %{oreon_filedir}/rust-libadwaita-devel.list

%changelog

%autochangelog
