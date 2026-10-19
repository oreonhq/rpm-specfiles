%global source0_hash da6a89ba31723d185fd7413b98c576a575f356d9b84729d8ecb6ead60000a5b6
%bcond check 0
%global debug_package %{nil}
%global crate sm3
Name:           rust-sm3
Version:        0.5.0
Release:        1%{?dist}
Summary:        SM3 (OSCCA GM/T 0004-2012) hash function
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sm3
Source0:        https://static.crates.io/crates/sm3/sm3-%{version}.crate
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
Summary:        SM3 (OSCCA GM/T 0004-2012) hash function
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
%files -n rust-sm3-devel -f %{oreon_filedir}/rust-sm3-devel.list

%changelog

%autochangelog
