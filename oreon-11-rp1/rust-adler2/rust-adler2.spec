%global source0_hash 320119579fcad9c21884f5c4861d16174d0e06250625266f50fe6898340abefa
%bcond check 1
%global debug_package %{nil}
%global crate adler2
Name:           rust-adler2
Version:        2.0.1
Release:        2%{?dist}
Summary:        Simple clean-room implementation of the Adler-32 checksum
License:        0BSD OR MIT OR Apache-2.0
URL:            https://crates.io/crates/adler2
Source0:        https://static.crates.io/crates/adler2/adler2-%{version}.crate
Patch:          adler2-fix-metadata.diff
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
Summary:        Simple clean-room implementation of the Adler-32 checksum
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Simple clean-room implementation of the Adler-32 checksum
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-adler2-devel -f %{oreon_filedir}/rust-adler2-devel.list

%changelog

%autochangelog
