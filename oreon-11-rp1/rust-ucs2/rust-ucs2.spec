%global source0_hash df79298e11f316400c57ec268f3c2c29ac3c4d4777687955cd3d4f3a35ce7eba
%bcond check 1
%global debug_package %{nil}
%global crate ucs2
Name:           rust-ucs2
Version:        0.3.3
Release:        1%{?dist}
Summary:        UCS-2 decoding and encoding functions
License:        MPL-2.0
URL:            https://crates.io/crates/ucs2
Source0:        https://static.crates.io/crates/ucs2/ucs2-%{version}.crate
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
Summary:        UCS-2 decoding and encoding functions
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
%files -n rust-ucs2-devel -f %{oreon_filedir}/rust-ucs2-devel.list

%changelog

%autochangelog
