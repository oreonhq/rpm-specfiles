%global source2_hash da41592534f1b96e15c06a0d08d14393ccc76abbc70d15e582e11172ee583838
%global source0_hash f4f025b91216f15a2a32aa39669329a475733590a015835d1783549a56d09427
%bcond check 1
%global debug_package %{nil}
%global crate serde_tuple
Name:           rust-serde_tuple0.5
Version:        0.5.0
Release:        1%{?dist}
Summary:        De/serialize structs with named fields as array of values
License:        MIT
URL:            https://crates.io/crates/serde_tuple
Source0:        https://static.crates.io/crates/serde_tuple/serde_tuple-%{version}.crate
Source2:        https://github.com/kardeiz/serde_tuple/raw/96b8643/LICENSE
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
Summary:        De/serialize structs with named fields as array of values
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} .
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
%files -n rust-serde_tuple0.5-devel -f %{oreon_filedir}/rust-serde_tuple0.5-devel.list

%changelog

%autochangelog
