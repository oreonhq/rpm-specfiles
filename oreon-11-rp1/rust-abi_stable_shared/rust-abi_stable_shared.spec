%global source0_hash b2b5df7688c123e63f4d4d649cba63f2967ba7f7861b1664fca3f77d3dad2b63
%bcond check 0
%global debug_package %{nil}
%global crate abi_stable_shared
Name:           rust-abi_stable_shared
Version:        0.11.0
Release:        1%{?dist}
Summary:        Implementation detail of abi_stable.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/abi_stable_shared
Source0:        https://static.crates.io/crates/abi_stable_shared/abi_stable_shared-%{version}.crate
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
Summary:        Implementation detail of abi_stable.
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
%files -n rust-abi_stable_shared-devel -f %{oreon_filedir}/rust-abi_stable_shared-devel.list

%changelog

%autochangelog
