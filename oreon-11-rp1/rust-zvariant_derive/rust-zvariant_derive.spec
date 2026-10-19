%global source0_hash 38a708216a18780796770bfe3f4739c7c83a3e8f789b755534bbbc06e4e23e12
%bcond check 0
%global debug_package %{nil}
%global crate zvariant_derive
Name:           rust-zvariant_derive
Version:        5.13.1
Release:        1%{?dist}
Summary:        D-Bus & GVariant encoding & decoding
License:        MIT
URL:            https://crates.io/crates/zvariant_derive
Source0:        https://static.crates.io/crates/zvariant_derive/zvariant_derive-%{version}.crate
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
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gvariant-devel
Summary:        D-Bus & GVariant encoding & decoding
BuildArch:      noarch
%description -n %{name}+gvariant-devel

This package contains library source intended for building other packages which
use the "gvariant" feature of the "%{crate}" crate.

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
%files -n rust-zvariant_derive-devel -f %{oreon_filedir}/rust-zvariant_derive-devel.list

%changelog

%autochangelog
