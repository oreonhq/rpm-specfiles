%global source0_hash 7660d28d24a831d690228a275d544654a30f3b167a8e491cf31af5fe5058b546
%bcond check 0
%global debug_package %{nil}
%global crate iso7816-tlv
Name:           rust-iso7816-tlv
Version:        0.4.4
Release:        1%{?dist}
Summary:        tools and utilities for handling TLV data as defined in ISO/IEC 7816-4
License:        ISC
URL:            https://crates.io/crates/iso7816-tlv
Source0:        https://static.crates.io/crates/iso7816-tlv/iso7816-tlv-%{version}.crate
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
Summary:        tools and utilities for handling TLV data as defined in ISO/IEC 7816-4
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
%files -n rust-iso7816-tlv-devel -f %{oreon_filedir}/rust-iso7816-tlv-devel.list

%changelog

%autochangelog
