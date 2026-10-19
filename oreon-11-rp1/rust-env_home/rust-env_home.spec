%global source0_hash c7f84e12ccf0a7ddc17a6c41c93326024c42920d7ee630d04950e6926645c0fe
%bcond check 1
%global debug_package %{nil}
%global crate env_home
Name:           rust-env_home
Version:        0.1.0
Release:        1%{?dist}
Summary:        Get the user home directory in a cross-platform way
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/env_home
Source0:        https://static.crates.io/crates/env_home/env_home-%{version}.crate
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
Summary:        Get the user home directory in a cross-platform way
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
%files -n rust-env_home-devel -f %{oreon_filedir}/rust-env_home-devel.list

%changelog

%autochangelog
