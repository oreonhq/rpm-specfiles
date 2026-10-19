%global source0_hash 5a895a7455441a857d100ca679bd24a92f91d28b5e3df63296792ac1af2eddde
%bcond check 1
%global debug_package %{nil}
%global crate relm4-macros
Name:           rust-relm4-macros
Version:        0.9.1
Release:        1%{?dist}
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/relm4-macros
Source0:        https://static.crates.io/crates/relm4-macros/relm4-macros-%{version}.crate
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
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+relm4-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+relm4-devel

This package contains library source intended for building other packages which
use the "relm4" feature of the "%{crate}" crate.

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
%files -n rust-relm4-macros-devel -f %{oreon_filedir}/rust-relm4-macros-devel.list

%changelog

%autochangelog
