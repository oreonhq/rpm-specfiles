%global source10_hash c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
%global source0_hash f9d757602a7ef2b6025c0da77e6d2e23fbdef35930fa466b15ffbf0a3f13acf7
%bcond check 1
%global debug_package %{nil}
%global crate reqsign-volcengine-tos
Name:           rust-reqsign-volcengine-tos
Version:        3.0.0
Release:        1%{?dist}
Summary:        Volcengine TOS signing implementation for reqsign
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign-volcengine-tos
Source0:        https://static.crates.io/crates/reqsign-volcengine-tos/reqsign-volcengine-tos-%{version}.crate
Source10:       https://github.com/apache/opendal-reqsign/raw/refs/tags/v0.20.0/LICENSE
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
Summary:        Volcengine TOS signing implementation for reqsign
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' .
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
%files -n rust-reqsign-volcengine-tos-devel -f %{oreon_filedir}/rust-reqsign-volcengine-tos-devel.list

%changelog

%autochangelog
