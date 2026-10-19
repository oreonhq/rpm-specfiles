%global source0_hash f11d34b07689c21889fc89bd7cc885b3244b0157bbededf4a1c159832cd0df05
%bcond check 0
%global debug_package %{nil}
%global crate cpio-archive
Name:           rust-cpio-archive
Version:        0.10.0
Release:        1%{?dist}
Summary:        Cpio archive reading and writing
License:        MPL-2.0
URL:            https://crates.io/crates/cpio-archive
Source0:        https://static.crates.io/crates/cpio-archive/cpio-archive-%{version}.crate
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
Summary:        Cpio archive reading and writing
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
%files -n rust-cpio-archive-devel -f %{oreon_filedir}/rust-cpio-archive-devel.list

%changelog

%autochangelog
