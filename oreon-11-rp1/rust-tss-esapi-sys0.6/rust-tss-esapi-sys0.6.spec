%global source0_hash a7f972672926a3d3d18ecc04524720e4d20b7d1664a3fb73dbf7d4274196dbd9
%bcond check 0
%global debug_package %{nil}
%global crate tss-esapi-sys
Name:           rust-tss-esapi-sys0.6
Version:        0.6.0
Release:        1%{?dist}
Summary:        FFI wrapper around TSS 2.0 Enhanced System API
License:        Apache-2.0
URL:            https://crates.io/crates/tss-esapi-sys
Source0:        https://static.crates.io/crates/tss-esapi-sys/tss-esapi-sys-%{version}.crate
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

%package     -n %{name}+generate-bindings-devel
Summary:        FFI wrapper around TSS 2.0 Enhanced System API
BuildArch:      noarch
%description -n %{name}+generate-bindings-devel

This package contains library source intended for building other packages which
use the "generate-bindings" feature of the "%{crate}" crate.

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
%files -n rust-tss-esapi-sys0.6-devel -f %{oreon_filedir}/rust-tss-esapi-sys0.6-devel.list

%changelog

%autochangelog
