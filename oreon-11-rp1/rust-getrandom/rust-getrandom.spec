%global source0_hash 300e883d756b2e4ec94e02791f39b04b522276138852cfc41d9fb7e904106099
%bcond check 0
%global debug_package %{nil}
%global crate getrandom
Name:           rust-getrandom
Version:        0.4.3
Release:        1%{?dist}
Summary:        Small cross-platform library for retrieving random data from system source
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/getrandom
Source0:        https://static.crates.io/crates/getrandom/getrandom-%{version}.crate
Patch:          getrandom-fix-metadata-auto.diff
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
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+sys_rng-devel
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+sys_rng-devel

This package contains library source intended for building other packages which
use the "sys_rng" feature of the "%{crate}" crate.

%package     -n %{name}+wasm_js-devel
Summary:        Small cross-platform library for retrieving random data from system source
BuildArch:      noarch
%description -n %{name}+wasm_js-devel

This package contains library source intended for building other packages which
use the "wasm_js" feature of the "%{crate}" crate.

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
%files -n rust-getrandom-devel -f %{oreon_filedir}/rust-getrandom-devel.list

%changelog

%autochangelog
