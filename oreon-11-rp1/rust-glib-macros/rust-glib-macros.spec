%global source0_hash c9597c68fa7bdf4154a3079642cd21c4dccac0b0bdd2897d82861523bf91e7b9
%bcond check 0
%global debug_package %{nil}
%global crate glib-macros
Name:           rust-glib-macros
Version:        0.22.9
Release:        1%{?dist}
Summary:        Rust bindings for the GLib library, proc macros crate
License:        MIT
URL:            https://crates.io/crates/glib-macros
Source0:        https://static.crates.io/crates/glib-macros/glib-macros-%{version}.crate
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
Summary:        Rust bindings for the GLib library, proc macros crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro-crate-devel
Summary:        Rust bindings for the GLib library, proc macros crate
BuildArch:      noarch
%description -n %{name}+proc-macro-crate-devel

This package contains library source intended for building other packages which
use the "proc-macro-crate" feature of the "%{crate}" crate.

%package     -n %{name}+proc_macro_crate-devel
Summary:        Rust bindings for the GLib library, proc macros crate
BuildArch:      noarch
%description -n %{name}+proc_macro_crate-devel

This package contains library source intended for building other packages which
use the "proc_macro_crate" feature of the "%{crate}" crate.

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
%files -n rust-glib-macros-devel -f %{oreon_filedir}/rust-glib-macros-devel.list

%changelog

%autochangelog
