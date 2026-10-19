%global source0_hash b7ac824320a75a52197e8f2d787f6a38b6718bb6897a35142d749af3c0e8f4fe
%bcond check 0
%global debug_package %{nil}
%global crate flagset
Name:           rust-flagset
Version:        0.4.7
Release:        1%{?dist}
Summary:        Data types and a macro for generating enumeration-based bit flags
License:        Apache-2.0
URL:            https://crates.io/crates/flagset
Source0:        https://static.crates.io/crates/flagset/flagset-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        Data types and a macro for generating enumeration-based bit flags
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Data types and a macro for generating enumeration-based bit flags
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
%files -n rust-flagset-devel -f %{oreon_filedir}/rust-flagset-devel.list

%changelog

%autochangelog
