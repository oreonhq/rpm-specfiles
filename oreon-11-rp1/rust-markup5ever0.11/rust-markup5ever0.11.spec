%global source0_hash 7a2629bb1404f3d34c2e921f21fd34ba00b206124c81f65c50b43b6aaefeb016
%bcond check 0
%global debug_package %{nil}
%global crate markup5ever
Name:           rust-markup5ever0.11
Version:        0.11.0
Release:        1%{?dist}
Summary:        Common code for xml5ever and html5ever
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/markup5ever
Source0:        https://static.crates.io/crates/markup5ever/markup5ever-%{version}.crate
Patch:          markup5ever-fix-metadata.diff
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
Summary:        Common code for xml5ever and html5ever
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
%files -n rust-markup5ever0.11-devel -f %{oreon_filedir}/rust-markup5ever0.11-devel.list

%changelog

%autochangelog
