%global source0_hash a74858bcfe44b22016cb49337d7b6f04618c58e5dbfdef61b06b8c434324a0bc
%bcond check 0
%global debug_package %{nil}
%global crate current_platform
Name:           rust-current_platform
Version:        0.2.0
Release:        1%{?dist}
Summary:        Find out what platform your code is running on
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/current_platform
Source0:        https://static.crates.io/crates/current_platform/current_platform-%{version}.crate
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
Summary:        Find out what platform your code is running on
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
%files -n rust-current_platform-devel -f %{oreon_filedir}/rust-current_platform-devel.list

%changelog

%autochangelog
