%global source0_hash b87bc54a4629b4294d0b3ef041b64c40c611097a677d9dc07b2c67739fe39dba
%bcond check 1
%global debug_package %{nil}
%global crate listenfd
Name:           rust-listenfd
Version:        1.0.2
Release:        1%{?dist}
Summary:        Simple library to work with listenfds passed from the outside
License:        Apache-2.0
URL:            https://crates.io/crates/listenfd
Source0:        https://static.crates.io/crates/listenfd/listenfd-%{version}.crate
Patch:          listenfd-fix-metadata-auto.diff
Patch:          listenfd-fix-metadata.diff
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
Summary:        Simple library to work with listenfds passed from the outside
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
%files -n rust-listenfd-devel -f %{oreon_filedir}/rust-listenfd-devel.list

%changelog

%autochangelog
