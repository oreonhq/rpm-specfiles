%global source0_hash c11532d9d241904f095185f35dcdaf930b1427a94d5b01d7002d74ba19b44cc4
%bcond check 1
%global debug_package %{nil}
%global crate simple-bytes
Name:           rust-simple-bytes
Version:        0.2.14
Release:        1%{?dist}
Summary:        Small and easy crate to mutate or read u8 slices
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/simple-bytes
Source0:        https://static.crates.io/crates/simple-bytes/simple-bytes-%{version}.crate
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
Summary:        Small and easy crate to mutate or read u8 slices
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
%files -n rust-simple-bytes-devel -f %{oreon_filedir}/rust-simple-bytes-devel.list

%changelog

%autochangelog
