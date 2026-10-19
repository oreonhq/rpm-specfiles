%global source0_hash 2f9ed6b3789237c8a0c1c505af1c7eb2c560df6186f01b098c3a1064ea532f38
%bcond check 0
%global debug_package %{nil}
%global crate enumn
Name:           rust-enumn
Version:        0.1.14
Release:        1%{?dist}
Summary:        Convert number to enum
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/enumn
Source0:        https://static.crates.io/crates/enumn/enumn-%{version}.crate
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
Summary:        Convert number to enum
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
%files -n rust-enumn-devel -f %{oreon_filedir}/rust-enumn-devel.list

%changelog

%autochangelog
