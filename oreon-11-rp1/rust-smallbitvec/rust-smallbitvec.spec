%global source0_hash d31d263dd118560e1a492922182ab6ca6dc1d03a3bf54e7699993f31a4150e3f
%bcond check 1
%global debug_package %{nil}
%global crate smallbitvec
Name:           rust-smallbitvec
Version:        2.6.0
Release:        1%{?dist}
Summary:        Bit vector optimized for size and inline storage
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/smallbitvec
Source0:        https://static.crates.io/crates/smallbitvec/smallbitvec-%{version}.crate
Patch:          smallbitvec-fix-metadata.diff
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
Summary:        Bit vector optimized for size and inline storage
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
%files -n rust-smallbitvec-devel -f %{oreon_filedir}/rust-smallbitvec-devel.list

%changelog

%autochangelog
