%global source0_hash e2355d85b9a3786f481747ced0e0ff2ba35213a1f9bd406ed906554d7af805a1
%bcond check 1
%global debug_package %{nil}
%global crate os_str_bytes
Name:           rust-os_str_bytes6
Version:        6.6.1
Release:        1%{?dist}
Summary:        Convert between byte sequences and platform-native strings
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/os_str_bytes
Source0:        https://static.crates.io/crates/os_str_bytes/os_str_bytes-%{version}.crate
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
Summary:        Convert between byte sequences and platform-native strings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+checked_conversions-devel
Summary:        Convert between byte sequences and platform-native strings
BuildArch:      noarch
%description -n %{name}+checked_conversions-devel

This package contains library source intended for building other packages which
use the "checked_conversions" feature of the "%{crate}" crate.

%package     -n %{name}+conversions-devel
Summary:        Convert between byte sequences and platform-native strings
BuildArch:      noarch
%description -n %{name}+conversions-devel

This package contains library source intended for building other packages which
use the "conversions" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        Convert between byte sequences and platform-native strings
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+raw_os_str-devel
Summary:        Convert between byte sequences and platform-native strings
BuildArch:      noarch
%description -n %{name}+raw_os_str-devel

This package contains library source intended for building other packages which
use the "raw_os_str" feature of the "%{crate}" crate.

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
%files -n rust-os_str_bytes6-devel -f %{oreon_filedir}/rust-os_str_bytes6-devel.list

%changelog

%autochangelog
