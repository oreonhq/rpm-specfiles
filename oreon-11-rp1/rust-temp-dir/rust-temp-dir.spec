%global source0_hash 83176759e9416cf81ee66cb6508dbfe9c96f20b8b56265a39917551c23c70964
%bcond check 0
%global debug_package %{nil}
%global crate temp-dir
Name:           rust-temp-dir
Version:        0.1.16
Release:        1%{?dist}
Summary:        Simple temporary directory with cleanup
License:        Apache-2.0
URL:            https://crates.io/crates/temp-dir
Source0:        https://static.crates.io/crates/temp-dir/temp-dir-%{version}.crate
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
Summary:        Simple temporary directory with cleanup
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
%files -n rust-temp-dir-devel -f %{oreon_filedir}/rust-temp-dir-devel.list

%changelog

%autochangelog
