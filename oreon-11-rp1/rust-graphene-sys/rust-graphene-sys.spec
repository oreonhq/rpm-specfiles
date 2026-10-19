%global source0_hash 97842c7543828f98aa5583aa54fcda28aa84fa2b0f8c556142177f7bbb638057
%bcond check 0
%global debug_package %{nil}
%global crate graphene-sys
Name:           rust-graphene-sys
Version:        0.22.9
Release:        1%{?dist}
Summary:        FFI bindings to libgraphene-1.0
License:        MIT
URL:            https://crates.io/crates/graphene-sys
Source0:        https://static.crates.io/crates/graphene-sys/graphene-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(graphene-gobject-1.0) >= 1.10
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libgraphene-1.0
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
%files -n rust-graphene-sys-devel -f %{oreon_filedir}/rust-graphene-sys-devel.list

%changelog

%autochangelog
