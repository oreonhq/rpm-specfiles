%global source0_hash d67af77d68a931ecd5cbd8a3b5987d63a1d1d1278f7f6a60ae33db485cdebb69
%bcond check 1
%global debug_package %{nil}
%global crate ar
Name:           rust-ar
Version:        0.9.0
Release:        1%{?dist}
Summary:        Library for encoding/decoding Unix archive files
License:        MIT
URL:            https://crates.io/crates/ar
Source0:        https://static.crates.io/crates/ar/ar-%{version}.crate
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
Summary:        Library for encoding/decoding Unix archive files
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
%files -n rust-ar-devel -f %{oreon_filedir}/rust-ar-devel.list

%changelog

%autochangelog
