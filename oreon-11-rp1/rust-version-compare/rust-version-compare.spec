%global source0_hash 03c2856837ef78f57382f06b2b8563a2f512f7185d732608fd9176cb3b8edf0e
%bcond check 1
%global debug_package %{nil}
%global crate version-compare
Name:           rust-version-compare
Version:        0.2.1
Release:        1%{?dist}
Summary:        Rust library to easily compare version numbers
License:        MIT
URL:            https://crates.io/crates/version-compare
Source0:        https://static.crates.io/crates/version-compare/version-compare-%{version}.crate
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
Summary:        Rust library to easily compare version numbers
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
%files -n rust-version-compare-devel -f %{oreon_filedir}/rust-version-compare-devel.list

%changelog

%autochangelog
