%global source0_hash 6245d59a3e82a7fc217c5828a6692dbc6dfb63a0c8c90495621f7b9d79704a0e
%bcond check 0
%global debug_package %{nil}
%global crate convert_case
Name:           rust-convert_case0.4
Version:        0.4.0
Release:        1%{?dist}
Summary:        Convert strings into any case
License:        MIT
URL:            https://crates.io/crates/convert_case
Source0:        https://static.crates.io/crates/convert_case/convert_case-%{version}.crate
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

%package     -n %{name}+rand-devel
Summary:        Convert strings into any case
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+random-devel
Summary:        Convert strings into any case
BuildArch:      noarch
%description -n %{name}+random-devel

This package contains library source intended for building other packages which
use the "random" feature of the "%{crate}" crate.

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
%files -n rust-convert_case0.4-devel -f %{oreon_filedir}/rust-convert_case0.4-devel.list

%changelog

%autochangelog
