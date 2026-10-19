%global source0_hash 29790946404f91d9c5d06f9874efddea1dc06c5efe94541a7d6863108e3a5e4b
%bcond_without check
%global debug_package %{nil}
%global crate walkdir
Name:           rust-walkdir
Version:        2.5.0
Release:        1%{?dist}
Summary:        Recursively walk a directory
License:        Unlicense OR MIT
URL:            https://crates.io/crates/walkdir
Source0:        https://static.crates.io/crates/walkdir/walkdir-%{version}.crate
Patch:          walkdir-fix-metadata-auto.diff
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
Summary:        Recursively walk a directory
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
%files -n rust-walkdir-devel -f %{oreon_filedir}/rust-walkdir-devel.list

%changelog

%autochangelog
