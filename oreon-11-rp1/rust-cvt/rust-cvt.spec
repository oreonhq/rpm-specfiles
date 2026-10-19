%global source0_hash d2ae9bf77fbf2d39ef573205d554d87e86c12f1994e9ea335b0651b9b278bcf1
%bcond check 0
%global debug_package %{nil}
%global crate cvt
Name:           rust-cvt
Version:        0.1.2
Release:        1%{?dist}
Summary:        Expose the cvt function from Rust libstd.
License:        Apache-2.0
URL:            https://crates.io/crates/cvt
Source0:        https://static.crates.io/crates/cvt/cvt-%{version}.crate
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
Summary:        Expose the cvt function from Rust libstd.
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
%files -n rust-cvt-devel -f %{oreon_filedir}/rust-cvt-devel.list

%changelog

%autochangelog
