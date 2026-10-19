%global source0_hash 704a3c26996a80471189265814dbc2c257598b96b8a7feae2d31ace646bb9782
%bcond check 0
%global debug_package %{nil}
%global crate csv-core
Name:           rust-csv-core
Version:        0.1.13
Release:        1%{?dist}
Summary:        Bare bones CSV parsing with no_std support.
License:        Unlicense OR MIT
URL:            https://crates.io/crates/csv-core
Source0:        https://static.crates.io/crates/csv-core/csv-core-%{version}.crate
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
Summary:        Bare bones CSV parsing with no_std support.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Bare bones CSV parsing with no_std support.
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

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
%files -n rust-csv-core-devel -f %{oreon_filedir}/rust-csv-core-devel.list

%changelog

%autochangelog
