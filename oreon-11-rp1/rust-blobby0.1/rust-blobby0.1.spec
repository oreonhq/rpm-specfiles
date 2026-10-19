%global source0_hash 6fe5f8c2940b65859ece4b3b2ba02d2b12c87cab455fd42dee2556a187bb2cf6
%bcond check 0
%global debug_package %{nil}
%global crate blobby
Name:           rust-blobby0.1
Version:        0.1.2
Release:        1%{?dist}
Summary:        Iterator over simple binary blob storage
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/blobby
Source0:        https://static.crates.io/crates/blobby/blobby-%{version}.crate
Patch:          blobby-fix-metadata.diff
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
Summary:        Iterator over simple binary blob storage
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
%files -n rust-blobby0.1-devel -f %{oreon_filedir}/rust-blobby0.1-devel.list

%changelog

%autochangelog
