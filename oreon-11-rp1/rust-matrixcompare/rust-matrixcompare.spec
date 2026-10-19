%global source0_hash 37832ba820e47c93d66b4360198dccb004b43c74abc3ac1ce1fed54e65a80445
%bcond check 1
%global debug_package %{nil}
%global crate matrixcompare
Name:           rust-matrixcompare
Version:        0.3.0
Release:        1%{?dist}
Summary:        Tools for convenient comparison of matrices
License:        MIT
URL:            https://crates.io/crates/matrixcompare
Source0:        https://static.crates.io/crates/matrixcompare/matrixcompare-%{version}.crate
Patch:          matrixcompare-fix-metadata.diff
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
Summary:        Tools for convenient comparison of matrices
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        Tools for convenient comparison of matrices
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-support-devel
Summary:        Tools for convenient comparison of matrices
BuildArch:      noarch
%description -n %{name}+proptest-support-devel

This package contains library source intended for building other packages which
use the "proptest-support" feature of the "%{crate}" crate.

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
%files -n rust-matrixcompare-devel -f %{oreon_filedir}/rust-matrixcompare-devel.list

%changelog

%autochangelog
