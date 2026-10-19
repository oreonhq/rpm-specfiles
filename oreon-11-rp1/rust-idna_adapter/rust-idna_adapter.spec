%global source0_hash cb68373c0d6620ef8105e855e7745e18b0d00d3bdb07fb532e434244cdb9a714
%bcond check 0
%global debug_package %{nil}
%global crate idna_adapter
Name:           rust-idna_adapter
Version:        1.2.2
Release:        1%{?dist}
Summary:        Back end adapter for idna
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/idna_adapter
Source0:        https://static.crates.io/crates/idna_adapter/idna_adapter-%{version}.crate
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

%package     -n %{name}+compiled_data-devel
Summary:        Back end adapter for idna
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

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
%files -n rust-idna_adapter-devel -f %{oreon_filedir}/rust-idna_adapter-devel.list

%changelog

%autochangelog
