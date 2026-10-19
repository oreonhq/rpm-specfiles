%global source0_hash cb9050999a1e032f4313788ac5a6d06e897a4f672f1de2ed98683001fc1abf56
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-cliprdr
Name:           rust-ironrdp-cliprdr
Version:        0.7.0
Release:        1%{?dist}
Summary:        CLIPRDR static channel for clipboard implemented as described in MS-RDPECLIP
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-cliprdr
Source0:        https://static.crates.io/crates/ironrdp-cliprdr/ironrdp-cliprdr-%{version}.crate
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
Summary:        CLIPRDR static channel for clipboard implemented as described in MS-RDPECLIP
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
%files -n rust-ironrdp-cliprdr-devel -f %{oreon_filedir}/rust-ironrdp-cliprdr-devel.list

%changelog

%autochangelog
