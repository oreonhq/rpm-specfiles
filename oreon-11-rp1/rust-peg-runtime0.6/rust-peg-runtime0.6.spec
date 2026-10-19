%global source1_hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
%global source0_hash 9555b1514d2d99d78150d3c799d4c357a3e2c2a8062cd108e93a06d9057629c5
%bcond check 0
%global debug_package %{nil}
%global crate peg-runtime
Name:           rust-peg-runtime0.6
Version:        0.6.3
Release:        1%{?dist}
Summary:        Runtime support for rust-peg grammars
License:        MIT
URL:            https://crates.io/crates/peg-runtime
Source0:        https://static.crates.io/crates/peg-runtime/peg-runtime-%{version}.crate
Source1:        https://github.com/kevinmehall/rust-peg/raw/%{version}/LICENSE
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
Summary:        Runtime support for rust-peg grammars
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-peg-runtime0.6-devel -f %{oreon_filedir}/rust-peg-runtime0.6-devel.list

%changelog

%autochangelog
