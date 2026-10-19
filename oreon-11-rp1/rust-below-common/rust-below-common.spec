%global source0_hash c2130c90f5c21a67bf91a2316c95f0878a9bede81f140d3660b612ba7cc862f7
%bcond check 1
%global debug_package %{nil}
%global crate below-common
Name:           rust-below-common
Version:        0.9.0
Release:        1%{?dist}
Summary:        Common below code
License:        Apache-2.0
URL:            https://crates.io/crates/below-common
Source0:        https://static.crates.io/crates/below-common/below-common-%{version}.crate
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
Summary:        Common below code
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

%{cargo_test -- -- --exact %{shrink:
    --skip dateutil::tests::test_parse_date
    --skip dateutil::tests::test_parse_range
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-below-common-devel -f %{oreon_filedir}/rust-below-common-devel.list

%changelog

%autochangelog
