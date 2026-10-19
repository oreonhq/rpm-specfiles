%global source0_hash 61b9e2a29ff01e8bb526a571ad06c10ed72aae80d5999ed204f7971f99f19974
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate duct
Name:           rust-duct
Version:        1.1.2
Release:        1%{?dist}
Summary:        Library for running child processes
License:        MIT
URL:            https://crates.io/crates/duct
Source0:        https://static.crates.io/crates/duct/duct-%{version}.crate
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
Summary:        Library for running child processes
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
%files -n rust-duct-devel -f %{oreon_filedir}/rust-duct-devel.list

%changelog

%autochangelog
