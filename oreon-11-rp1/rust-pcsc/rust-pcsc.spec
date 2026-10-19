%global source0_hash 7dd833ecf8967e65934c49d3521a175929839bf6d0e497f3bd0d3a2ca08943da
%bcond check 0
%global debug_package %{nil}
%global crate pcsc
Name:           rust-pcsc
Version:        2.9.0
Release:        1%{?dist}
Summary:        Bindings to the PC/SC API for smart card communication
License:        MIT
URL:            https://crates.io/crates/pcsc
Source0:        https://static.crates.io/crates/pcsc/pcsc-%{version}.crate
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
Summary:        Bindings to the PC/SC API for smart card communication
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
%files -n rust-pcsc-devel -f %{oreon_filedir}/rust-pcsc-devel.list

%changelog

%autochangelog
