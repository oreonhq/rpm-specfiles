%global source0_hash 914b1a6776c4c929a602fafd8bc742e06365d4bcbe48c30f9cca5824f70dc9dd
%bcond check 0
%global debug_package %{nil}
%global crate version_check
Name:           rust-version_check0.1
Version:        0.1.5
Release:        1%{?dist}
Summary:        Tiny crate to check the version of the installed/running rustc.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/version_check
Source0:        https://static.crates.io/crates/version_check/version_check-%{version}.crate
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
Summary:        Tiny crate to check the version of the installed/running rustc.
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
%files -n rust-version_check0.1-devel -f %{oreon_filedir}/rust-version_check0.1-devel.list

%changelog

%autochangelog
