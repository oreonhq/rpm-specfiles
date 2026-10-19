%global source0_hash 16de123c2e6c90ce3b573b7330de19be649080ec612033d397d72da265f1bd8b
%bcond check 1
%global debug_package %{nil}
%global crate glib
Name:           rust-glib0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        Rust bindings for the GLib library
License:        MIT
URL:            https://crates.io/crates/glib
Source0:        https://static.crates.io/crates/glib/glib-%{version}.crate
Patch:          glib-fix-metadata.diff
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
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+compiletests-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+compiletests-devel

This package contains library source intended for building other packages which
use the "compiletests" feature of the "%{crate}" crate.

%package     -n %{name}+gio-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+gio-devel

This package contains library source intended for building other packages which
use the "gio" feature of the "%{crate}" crate.

%package     -n %{name}+gio-sys-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+gio-sys-devel

This package contains library source intended for building other packages which
use the "gio-sys" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+log_macros-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+log_macros-devel

This package contains library source intended for building other packages which
use the "log_macros" feature of the "%{crate}" crate.

%package     -n %{name}+rs-log-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+rs-log-devel

This package contains library source intended for building other packages which
use the "rs-log" feature of the "%{crate}" crate.

%package     -n %{name}+v2_58-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_58-devel

This package contains library source intended for building other packages which
use the "v2_58" feature of the "%{crate}" crate.

%package     -n %{name}+v2_60-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_60-devel

This package contains library source intended for building other packages which
use the "v2_60" feature of the "%{crate}" crate.

%package     -n %{name}+v2_62-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_62-devel

This package contains library source intended for building other packages which
use the "v2_62" feature of the "%{crate}" crate.

%package     -n %{name}+v2_64-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_64-devel

This package contains library source intended for building other packages which
use the "v2_64" feature of the "%{crate}" crate.

%package     -n %{name}+v2_66-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_66-devel

This package contains library source intended for building other packages which
use the "v2_66" feature of the "%{crate}" crate.

%package     -n %{name}+v2_68-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_68-devel

This package contains library source intended for building other packages which
use the "v2_68" feature of the "%{crate}" crate.

%package     -n %{name}+v2_70-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_70-devel

This package contains library source intended for building other packages which
use the "v2_70" feature of the "%{crate}" crate.

%package     -n %{name}+v2_72-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_72-devel

This package contains library source intended for building other packages which
use the "v2_72" feature of the "%{crate}" crate.

%package     -n %{name}+v2_74-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_74-devel

This package contains library source intended for building other packages which
use the "v2_74" feature of the "%{crate}" crate.

%package     -n %{name}+v2_76-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_76-devel

This package contains library source intended for building other packages which
use the "v2_76" feature of the "%{crate}" crate.

%package     -n %{name}+v2_78-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_78-devel

This package contains library source intended for building other packages which
use the "v2_78" feature of the "%{crate}" crate.

%package     -n %{name}+v2_80-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_80-devel

This package contains library source intended for building other packages which
use the "v2_80" feature of the "%{crate}" crate.

%package     -n %{name}+v2_82-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_82-devel

This package contains library source intended for building other packages which
use the "v2_82" feature of the "%{crate}" crate.

%package     -n %{name}+v2_84-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_84-devel

This package contains library source intended for building other packages which
use the "v2_84" feature of the "%{crate}" crate.

%package     -n %{name}+v2_86-devel
Summary:        Rust bindings for the GLib library
BuildArch:      noarch
%description -n %{name}+v2_86-devel

This package contains library source intended for building other packages which
use the "v2_86" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip structured_log
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-glib0.21-devel -f %{oreon_filedir}/rust-glib0.21-devel.list

%changelog

%autochangelog
