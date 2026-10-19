%global source0_hash ed3955f1a9c7c0c15e092f9c887db08b1fc683305fdf6eb6684f22555355e202
%bcond check 0
%global debug_package %{nil}
%global crate num-derive
Name:           rust-num-derive
Version:        0.4.2
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

%package     -n %{name}+default-devel
Summary:        Numeric syntax extensions
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
%files -n rust-num-derive-devel -f %{oreon_filedir}/rust-num-derive-devel.list

%changelog

%autochangelog
