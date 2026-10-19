%global source0_hash 52cd9d68cf7efc6ddfaaee42e7288d3a99d613d4b50f76ce9827ae0c6e14f938
%bcond check 0
%global debug_package %{nil}
%global crate csv
Name:           rust-csv
Version:        1.4.0
Release:        1%{?dist}
Summary:        Fast CSV parsing with support for serde.
License:        Unlicense OR MIT
URL:            https://crates.io/crates/csv
Source0:        https://static.crates.io/crates/csv/csv-%{version}.crate
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
Summary:        Fast CSV parsing with support for serde.
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
%files -n rust-csv-devel -f %{oreon_filedir}/rust-csv-devel.list

%changelog

%autochangelog
