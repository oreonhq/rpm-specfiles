%global source0_hash 6d95021344f9715868259d6b500aa0fb2a3b53c39b5c88fc45814355e53ce83a
%bcond check 1
%global debug_package %{nil}
%global crate devicemapper
Name:           rust-devicemapper
Version:        0.34.8
Release:        1%{?dist}
Summary:        Library for using Linux device mapper
License:        MPL-2.0
URL:            https://crates.io/crates/devicemapper
Source0:        https://static.crates.io/crates/devicemapper/devicemapper-%{version}.crate
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
Summary:        Library for using Linux device mapper
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+disable_cargo_metadata-devel
Summary:        Library for using Linux device mapper
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

%{cargo_test -- -- %{shrink:
    --skip sudo_
    --skip loop_
    --skip udevsync_
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-devicemapper-devel -f %{oreon_filedir}/rust-devicemapper-devel.list

%changelog

%autochangelog
