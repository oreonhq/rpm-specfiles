%global source0_hash b6cf3aea8a5081171859ef57bc1606b1df6999df4f1110f8eef68b30098d1d3a
%bcond check 0
%global debug_package %{nil}
%global crate cap-primitives
Name:           rust-cap-primitives
Version:        3.4.5
Release:        1%{?dist}
Summary:        Capability-based primitives
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/cap-primitives
Source0:        https://static.crates.io/crates/cap-primitives/cap-primitives-%{version}.crate
Patch:          cap-primitives-fix-metadata-auto.diff
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

%package     -n %{name}+arbitrary-devel
Summary:        Capability-based primitives
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

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
%files -n rust-cap-primitives-devel -f %{oreon_filedir}/rust-cap-primitives-devel.list

%changelog

%autochangelog
