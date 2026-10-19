%global source0_hash 1563da1ed3e0b3bf3d74c9b85917ac9c56464d2f57242270c09c9e752f8021a0
%bcond check 0
%global debug_package %{nil}
%global crate icu_normalizer_data
Name:           rust-icu_normalizer_data
Version:        2.3.0
Release:        2%{?dist}
Summary:        Data for the icu_normalizer crate
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_normalizer_data
Source0:        https://static.crates.io/crates/icu_normalizer_data/icu_normalizer_data-%{version}.crate
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
Summary:        Data for the icu_normalizer crate
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
%files -n rust-icu_normalizer_data-devel -f %{oreon_filedir}/rust-icu_normalizer_data-devel.list

%changelog

%autochangelog
