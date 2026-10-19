%global source0_hash 217698eaf96b4a3f0bc4f3662aaa55bdf913cd54d7204591faa790070c6d0853
%bcond check 0
%global debug_package %{nil}
%global crate crc-catalog
Name:           rust-crc-catalog
Version:        2.5.0
Release:        1%{?dist}
Summary:        Catalog of CRC algorithms (generated from http://reveng.sourceforge.n...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crc-catalog
Source0:        https://static.crates.io/crates/crc-catalog/crc-catalog-%{version}.crate
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
Summary:        Catalog of CRC algorithms (generated from http://reveng.sourceforge.n...
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
%files -n rust-crc-catalog-devel -f %{oreon_filedir}/rust-crc-catalog-devel.list

%changelog

%autochangelog
