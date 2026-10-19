%global source1_hash 6252f0c8d4a0df9b2dc0c6464cb2489dbe8859b0eb727e19c14e6af1ee432394
%global source0_hash 58f57ca1d128a43733fd71d583e837b1f22239a37ebea09cde11d8d9a9080f47
%bcond check 0
%global debug_package %{nil}
%global crate seahash
Name:           rust-seahash3
Version:        3.0.7
Release:        1%{?dist}
Summary:        Blazingly fast, portable hash function with proven statistical guarantees
License:        MIT
URL:            https://crates.io/crates/seahash
Source0:        https://static.crates.io/crates/seahash/seahash-%{version}.crate
Source1:        https://github.com/redox-os/tfs/raw/facbfb6/LICENSE
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
Summary:        Blazingly fast, portable hash function with proven statistical guarantees
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
%files -n rust-seahash3-devel -f %{oreon_filedir}/rust-seahash3-devel.list

%changelog

%autochangelog
