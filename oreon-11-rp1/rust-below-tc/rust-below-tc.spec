%global source2_hash 8c6db340475136df3c1201d458fa5755698eace76e510471ecc9d857d6083dac
%global source0_hash 552d75d66dd902086220890c844bbd670e62a3b6c05d1d07a916f6bb184b7af0
%bcond check 1
%global debug_package %{nil}
%global crate below-tc
Name:           rust-below-tc
Version:        0.9.0
Release:        1%{?dist}
Summary:        TC crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-tc
Source0:        https://static.crates.io/crates/below-tc/below-tc-%{version}.crate
Source2:        https://raw.githubusercontent.com/facebookincubator/below/refs/tags/v0.9.0/LICENSE
Patch:          below-tc-fix-metadata.diff
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
Summary:        TC crate for below
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE2} .
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
%files -n rust-below-tc-devel -f %{oreon_filedir}/rust-below-tc-devel.list

%changelog

%autochangelog
