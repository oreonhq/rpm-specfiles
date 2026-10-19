%global source0_hash dffa08d8cdb97709f15a9cf1bc0edd439a96e8c1d05687272b430b7a3cd8a64b
%bcond check 0
%global debug_package %{nil}
%global crate pcx
Name:           rust-pcx
Version:        0.2.5
Release:        1%{?dist}
Summary:        Library for reading & writing PCX images
License:        MIT OR Apache-2.0 OR WTFPL
URL:            https://crates.io/crates/pcx
Source0:        https://static.crates.io/crates/pcx/pcx-%{version}.crate
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
Summary:        Library for reading & writing PCX images
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
%files -n rust-pcx-devel -f %{oreon_filedir}/rust-pcx-devel.list

%changelog

%autochangelog
