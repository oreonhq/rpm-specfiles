%global source0_hash 98a0a0466484f64b07b5b8184d43fa46be78eb0b8e04ae4e179af31d770b76d9
%bcond check 0
%global debug_package %{nil}
%global crate gtk4
Name:           rust-gtk4_0.9
Version:        0.11.4
Release:        1%{?dist}
Summary:        Rust bindings of the GTK 4 library
License:        MIT
URL:            https://crates.io/crates/gtk4
Source0:        https://static.crates.io/crates/gtk4/gtk4-%{version}.crate
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
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blueprint-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+blueprint-devel

This package contains library source intended for building other packages which
use the "blueprint" feature of the "%{crate}" crate.

%package     -n %{name}+gio_v2_80-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+gio_v2_80-devel

This package contains library source intended for building other packages which
use the "gio_v2_80" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_42-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+gnome_42-devel

This package contains library source intended for building other packages which
use the "gnome_42" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_43-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+gnome_43-devel

This package contains library source intended for building other packages which
use the "gnome_43" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_44-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+gnome_44-devel

This package contains library source intended for building other packages which
use the "gnome_44" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_45-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+gnome_45-devel

This package contains library source intended for building other packages which
use the "gnome_45" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_46-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+gnome_46-devel

This package contains library source intended for building other packages which
use the "gnome_46" feature of the "%{crate}" crate.

%package     -n %{name}+gnome_47-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+gnome_47-devel

This package contains library source intended for building other packages which
use the "gnome_47" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-assume-initialized-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+unsafe-assume-initialized-devel

This package contains library source intended for building other packages which
use the "unsafe-assume-initialized" feature of the "%{crate}" crate.

%package     -n %{name}+v4_10-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_10-devel

This package contains library source intended for building other packages which
use the "v4_10" feature of the "%{crate}" crate.

%package     -n %{name}+v4_12-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_12-devel

This package contains library source intended for building other packages which
use the "v4_12" feature of the "%{crate}" crate.

%package     -n %{name}+v4_14-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_14-devel

This package contains library source intended for building other packages which
use the "v4_14" feature of the "%{crate}" crate.

%package     -n %{name}+v4_16-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_16-devel

This package contains library source intended for building other packages which
use the "v4_16" feature of the "%{crate}" crate.

%package     -n %{name}+v4_18-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_18-devel

This package contains library source intended for building other packages which
use the "v4_18" feature of the "%{crate}" crate.

%package     -n %{name}+v4_2-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_2-devel

This package contains library source intended for building other packages which
use the "v4_2" feature of the "%{crate}" crate.

%package     -n %{name}+v4_4-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_4-devel

This package contains library source intended for building other packages which
use the "v4_4" feature of the "%{crate}" crate.

%package     -n %{name}+v4_6-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_6-devel

This package contains library source intended for building other packages which
use the "v4_6" feature of the "%{crate}" crate.

%package     -n %{name}+v4_8-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+v4_8-devel

This package contains library source intended for building other packages which
use the "v4_8" feature of the "%{crate}" crate.

%package     -n %{name}+xml_validation-devel
Summary:        Rust bindings of the GTK 4 library
BuildArch:      noarch
%description -n %{name}+xml_validation-devel

This package contains library source intended for building other packages which
use the "xml_validation" feature of the "%{crate}" crate.

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
%files -n rust-gtk4_0.9-devel -f %{oreon_filedir}/rust-gtk4_0.9-devel.list

%changelog

%autochangelog
