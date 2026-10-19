%global source0_hash f6b464fbc74e149a392436b17d523f769e057cb6877f6a5c4618bc6f11800548
%bcond check 1
%global debug_package %{nil}
%global crate pkg-config
Name:           rust-pkg-config
Version:        0.3.34
Release:        1%{?dist}
Summary:        Library to run the pkg-config system tool
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pkg-config
Source0:        https://static.crates.io/crates/pkg-config/pkg-config-%{version}.crate
# oreon:deps
BuildRequires:  /usr/bin/pkg-config
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       /usr/bin/pkg-config
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Library to run the pkg-config system tool
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
%files -n rust-pkg-config-devel -f %{oreon_filedir}/rust-pkg-config-devel.list

%changelog

%autochangelog
