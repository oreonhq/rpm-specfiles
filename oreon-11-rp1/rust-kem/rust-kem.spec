%global source0_hash 01737161ba802849cfd486b5bd209d38ba4943494c249a8126005170c7621edd
%bcond check 0
%global debug_package %{nil}
%global crate kem
Name:           rust-kem
Version:        0.3.0
Release:        1%{?dist}
Summary:        Traits for Key Encapsulation Mechanisms (KEMs): public-key cryptosyst...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/kem
Source0:        https://static.crates.io/crates/kem/kem-%{version}.crate
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

%package     -n %{name}+getrandom-devel
Summary:        Traits for Key Encapsulation Mechanisms (KEMs): public-key cryptosyst...
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

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
%files -n rust-kem-devel -f %{oreon_filedir}/rust-kem-devel.list

%changelog

%autochangelog
