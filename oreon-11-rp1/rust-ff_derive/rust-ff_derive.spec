%global source0_hash 241afe8c15ffa21933eaefe8a563af36fd9fc98a3e8a044e8f7db52eb1fae3d8
%bcond check 0
%global debug_package %{nil}
%global crate ff_derive
Name:           rust-ff_derive
Version:        0.14.0
Release:        1%{?dist}
Summary:        Procedural macro library used to build custom prime field implementat...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ff_derive
Source0:        https://static.crates.io/crates/ff_derive/ff_derive-%{version}.crate
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

%package     -n %{name}+bits-devel
Summary:        Procedural macro library used to build custom prime field implementat...
BuildArch:      noarch
%description -n %{name}+bits-devel

This package contains library source intended for building other packages which
use the "bits" feature of the "%{crate}" crate.

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
%files -n rust-ff_derive-devel -f %{oreon_filedir}/rust-ff_derive-devel.list

%changelog

%autochangelog
