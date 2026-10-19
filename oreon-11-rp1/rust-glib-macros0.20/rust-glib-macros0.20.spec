%global source0_hash e8084af62f09475a3f529b1629c10c429d7600ee1398ae12dd3bf175d74e7145
%bcond check 0
%global debug_package %{nil}
%global crate glib-macros
Name:           rust-glib-macros0.20
Version:        0.20.12
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
%files -n rust-glib-macros0.20-devel -f %{oreon_filedir}/rust-glib-macros0.20-devel.list

%changelog

%autochangelog
