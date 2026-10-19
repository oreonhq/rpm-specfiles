%global source0_hash 9940d5434caf74acfe135b92c913b12162193ec6d9c72aa3df2257f9818d2900
%bcond check 1
%global debug_package %{nil}
%global crate drop-tracker
Name:           rust-drop-tracker
Version:        0.2.0
Release:        1%{?dist}
Summary:        To check when a variable gets dropped
License:        BSD-3-Clause
URL:            https://crates.io/crates/drop-tracker
Source0:        https://static.crates.io/crates/drop-tracker/drop-tracker-%{version}.crate
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
Summary:        To check when a variable gets dropped
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
%files -n rust-drop-tracker-devel -f %{oreon_filedir}/rust-drop-tracker-devel.list

%changelog

%autochangelog
