%global source0_hash 876a53fff98e03a936a674b29568b0e605f06b29372c2489ff4de23f1949743d
%bcond check 0
%global debug_package %{nil}
%global crate num-derive
Name:           rust-num-derive0.3
Version:        0.3.3
Release:        1%{?dist}
Summary:        Numeric syntax extensions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-derive
Source0:        https://static.crates.io/crates/num-derive/num-derive-%{version}.crate
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

%package     -n %{name}+full-syntax-devel
Summary:        Numeric syntax extensions
BuildArch:      noarch
%description -n %{name}+full-syntax-devel

This package contains library source intended for building other packages which
use the "full-syntax" feature of the "%{crate}" crate.

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
%files -n rust-num-derive0.3-devel -f %{oreon_filedir}/rust-num-derive0.3-devel.list

%changelog

%autochangelog
