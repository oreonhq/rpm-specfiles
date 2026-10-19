%global source0_hash eb856b9c558971c3f13ab692358926da710b046932a4e087aedcc35b040d7dff
%bcond check 1
%global debug_package %{nil}
%global crate graphene-rs
Name:           rust-graphene-rs
Version:        0.22.8
Release:        1%{?dist}
Summary:        Rust bindings for the Graphene library
License:        MIT
URL:            https://crates.io/crates/graphene-rs
Source0:        https://static.crates.io/crates/graphene-rs/graphene-rs-%{version}.crate
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
Summary:        Rust bindings for the Graphene library
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
%files -n rust-graphene-rs-devel -f %{oreon_filedir}/rust-graphene-rs-devel.list

%changelog

%autochangelog
