%global source0_hash c5b9c0c5345041b6734f89e7642995f479c1740c7c91075f0602e042ec55b268
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_od
Name:           rust-uu_od
Version:        0.7.0
Release:        1%{?dist}
Summary:        od ~ (uutils) display formatted representation of input
License:        MIT
URL:            https://crates.io/crates/uu_od
Source0:        https://static.crates.io/crates/uu_od/uu_od-%{version}.crate
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
Summary:        od ~ (uutils) display formatted representation of input
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
%files -n rust-uu_od-devel -f %{oreon_filedir}/rust-uu_od-devel.list

%changelog

%autochangelog
