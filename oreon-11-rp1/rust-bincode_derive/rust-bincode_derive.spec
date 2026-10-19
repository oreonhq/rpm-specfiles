%global source0_hash bf95709a440f45e986983918d0e8a1f30a9b1df04918fc828670606804ac3c09
%bcond check 0
%global debug_package %{nil}
%global crate bincode_derive
Name:           rust-bincode_derive
Version:        2.0.1
Release:        1%{?dist}
Summary:        Implementation of #[derive(Encode, Decode)] for bincode
License:        MIT
URL:            https://crates.io/crates/bincode_derive
Source0:        https://static.crates.io/crates/bincode_derive/bincode_derive-%{version}.crate
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
Summary:        Implementation of #[derive(Encode, Decode)] for bincode
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
%files -n rust-bincode_derive-devel -f %{oreon_filedir}/rust-bincode_derive-devel.list

%changelog

%autochangelog
