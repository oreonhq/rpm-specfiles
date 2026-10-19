%global source3_hash 10e619056312012c40e4900844f3f892551ee716bbd44eeecb7d6ba2682b6dec
%global source2_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash 31eb5aad58f01a5288d0da978d5ee443150025ea10497a812e6fdf3734276953
%bcond check 0
%global debug_package %{nil}
%global crate hecs-macros
Name:           rust-hecs-macros
Version:        0.11.1
Release:        1%{?dist}
Summary:        Procedural macro definitions for hecs
License:        Apache-2.0
URL:            https://crates.io/crates/hecs-macros
Source0:        https://static.crates.io/crates/hecs-macros/hecs-macros-%{version}.crate
Source2:        https://github.com/Ralith/hecs/raw/refs/tags/v0.10.5/LICENSE-APACHE
Source3:        https://github.com/Ralith/hecs/raw/refs/tags/v0.10.5/LICENSE-MIT
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
Summary:        Procedural macro definitions for hecs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} %{SOURCE3} .
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
%files -n rust-hecs-macros-devel -f %{oreon_filedir}/rust-hecs-macros-devel.list

%changelog

%autochangelog
