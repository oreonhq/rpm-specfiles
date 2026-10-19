%global source0_hash 916a94e407b54f9034d71dd748234cd1e516ced6284009906ae246f177eafe5a
%bcond check 0
%global debug_package %{nil}
%global crate des
Name:           rust-des0.9
Version:        0.9.0
Release:        1%{?dist}
Summary:        DES and Triple DES (3DES, TDES) block ciphers implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/des
Source0:        https://static.crates.io/crates/des/des-%{version}.crate
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

%package     -n %{name}+zeroize-devel
Summary:        DES and Triple DES (3DES, TDES) block ciphers implementation
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-des0.9-devel -f %{oreon_filedir}/rust-des0.9-devel.list

%changelog

%autochangelog
