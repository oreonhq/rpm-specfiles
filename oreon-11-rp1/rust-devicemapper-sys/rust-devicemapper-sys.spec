%global source0_hash 06421aaad10b53bd5d1fe004c26efddfaaeaa4438ff52b84a0f660b3c87d63e6
%bcond check 1
%global debug_package %{nil}
%global crate devicemapper-sys
Name:           rust-devicemapper-sys
Version:        0.3.3
Release:        1%{?dist}
Summary:        Low level bindings for devicemapper
License:        MPL-2.0
URL:            https://crates.io/crates/devicemapper-sys
Source0:        https://static.crates.io/crates/devicemapper-sys/devicemapper-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  device-mapper-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       device-mapper-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Low level bindings for devicemapper
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+disable_cargo_metadata-devel
Summary:        Low level bindings for devicemapper
BuildArch:      noarch
%description -n %{name}+disable_cargo_metadata-devel

This package contains library source intended for building other packages which
use the "disable_cargo_metadata" feature of the "%{crate}" crate.

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
%files -n rust-devicemapper-sys-devel -f %{oreon_filedir}/rust-devicemapper-sys-devel.list

%changelog

%autochangelog
