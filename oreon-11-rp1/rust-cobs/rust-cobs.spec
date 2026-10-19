%global source0_hash dd93fd2c1b27acd030440c9dbd9d14c1122aad622374fe05a670b67a4bc034be
%bcond check 0
%global debug_package %{nil}
%global crate cobs
Name:           rust-cobs
Version:        0.5.1
Release:        1%{?dist}
Summary:        This is an implementation of the Consistent Overhead Byte Stuffing (C...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cobs
Source0:        https://static.crates.io/crates/cobs/cobs-%{version}.crate
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
Summary:        This is an implementation of the Consistent Overhead Byte Stuffing (C...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        This is an implementation of the Consistent Overhead Byte Stuffing (C...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-devel
Summary:        This is an implementation of the Consistent Overhead Byte Stuffing (C...
BuildArch:      noarch
%description -n %{name}+defmt-devel

This package contains library source intended for building other packages which
use the "defmt" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        This is an implementation of the Consistent Overhead Byte Stuffing (C...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        This is an implementation of the Consistent Overhead Byte Stuffing (C...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        This is an implementation of the Consistent Overhead Byte Stuffing (C...
BuildArch:      noarch
%description -n %{name}+use_std-devel

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

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
%files -n rust-cobs-devel -f %{oreon_filedir}/rust-cobs-devel.list

%changelog

%autochangelog
