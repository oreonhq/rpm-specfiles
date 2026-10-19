%global source0_hash a65064ea4a457eaf07f2fba30b4c695bf43b721790e9530d26cb6f9019ff7502
%bcond check 0
%global debug_package %{nil}
%global crate actix-server
Name:           rust-actix-server
Version:        2.6.0
Release:        1%{?dist}
Summary:        General purpose TCP server built for the Actix ecosystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-server
Source0:        https://static.crates.io/crates/actix-server/actix-server-%{version}.crate
Patch:          actix-server-fix-metadata.diff
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
Summary:        General purpose TCP server built for the Actix ecosystem
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
%files -n rust-actix-server-devel -f %{oreon_filedir}/rust-actix-server-devel.list

%changelog

%autochangelog
