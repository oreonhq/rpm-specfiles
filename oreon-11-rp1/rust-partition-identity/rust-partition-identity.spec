%global source0_hash 9fa925f9becb532d758b0014b472c576869910929cf4c3f8054b386f19ab9e21
%bcond check 0
%global debug_package %{nil}
%global crate partition-identity
Name:           rust-partition-identity
Version:        0.3.0
Release:        1%{?dist}
Summary:        Find the ID of a device by its path, or find a device path by its ID
License:        MIT
URL:            https://crates.io/crates/partition-identity
Source0:        https://static.crates.io/crates/partition-identity/partition-identity-%{version}.crate
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
Summary:        Find the ID of a device by its path, or find a device path by its ID
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
%files -n rust-partition-identity-devel -f %{oreon_filedir}/rust-partition-identity-devel.list

%changelog

%autochangelog
