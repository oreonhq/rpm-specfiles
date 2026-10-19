%global source0_hash f9871f38b67853c358b8190f77b9f878eb27d933a950f1045b244c4559a9f5f0
%bcond check 1
%global debug_package %{nil}
%global crate glib-build-tools
Name:           rust-glib-build-tools
Version:        0.22.8
Release:        1%{?dist}
Summary:        Rust bindings for the Gio library, build script utils crate
License:        MIT
URL:            https://crates.io/crates/glib-build-tools
Source0:        https://static.crates.io/crates/glib-build-tools/glib-build-tools-%{version}.crate
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
Summary:        Rust bindings for the Gio library, build script utils crate
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
%files -n rust-glib-build-tools-devel -f %{oreon_filedir}/rust-glib-build-tools-devel.list

%changelog

%autochangelog
