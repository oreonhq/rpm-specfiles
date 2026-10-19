%global source0_hash 5c8573b60d07b5b5cecadc1f978c9b71d5504151e703cbb0439ee4ad301338f3
%bcond check 0
%global debug_package %{nil}
%global crate dsa
Name:           rust-dsa
Version:        0.7.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Digital Signature Algorithm (DSA) as...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/dsa
Source0:        https://static.crates.io/crates/dsa/dsa-%{version}.crate
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

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the Digital Signature Algorithm (DSA) as...
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
%files -n rust-dsa-devel -f %{oreon_filedir}/rust-dsa-devel.list

%changelog

%autochangelog
