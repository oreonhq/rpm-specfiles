%global source0_hash 7cc2191ec1fd850e3ede4cf09ccfd40a33df561111f73e96e1b7c3f9eee31328
%bcond check 0
%global debug_package %{nil}
%global crate range_map_vec
Name:           rust-range_map_vec
Version:        0.2.0
Release:        1%{?dist}
Summary:        Implementation of a range map data structure backed by a Vec
License:        MIT
URL:            https://crates.io/crates/range_map_vec
Source0:        https://static.crates.io/crates/range_map_vec/range_map_vec-%{version}.crate
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
Summary:        Implementation of a range map data structure backed by a Vec
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
%files -n rust-range_map_vec-devel -f %{oreon_filedir}/rust-range_map_vec-devel.list

%changelog

%autochangelog
