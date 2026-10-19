%global source0_hash d2960fd49513e54e029f3abc7e8565f4e0b131dfbb97cc2b8c47fbe58fb1b16f
%bcond check 0
%global debug_package %{nil}
%global crate invalidstring
Name:           rust-invalidstring
Version:        0.1.3
Release:        1%{?dist}
Summary:        Just for testing invalid string data
License:        MIT
URL:            https://crates.io/crates/invalidstring
Source0:        https://static.crates.io/crates/invalidstring/invalidstring-%{version}.crate
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
Summary:        Just for testing invalid string data
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
%files -n rust-invalidstring-devel -f %{oreon_filedir}/rust-invalidstring-devel.list

%changelog

%autochangelog
