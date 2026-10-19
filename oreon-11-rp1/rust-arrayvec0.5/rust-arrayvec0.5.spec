%global source0_hash 23b62fc65de8e4e7f52534fb52b0f3ed04746ae267519eef2a83941e8085068b
%bcond check 0
%global debug_package %{nil}
%global crate arrayvec
Name:           rust-arrayvec0.5
Version:        0.5.2
Release:        1%{?dist}
Summary:        A vector with fixed capacity, backed by an array (it can be stored on...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/arrayvec
Source0:        https://static.crates.io/crates/arrayvec/arrayvec-%{version}.crate
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
Summary:        A vector with fixed capacity, backed by an array (it can be stored on...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+array-sizes-129-255-devel
Summary:        A vector with fixed capacity, backed by an array (it can be stored on...
BuildArch:      noarch
%description -n %{name}+array-sizes-129-255-devel

This package contains library source intended for building other packages which
use the "array-sizes-129-255" feature of the "%{crate}" crate.

%package     -n %{name}+array-sizes-33-128-devel
Summary:        A vector with fixed capacity, backed by an array (it can be stored on...
BuildArch:      noarch
%description -n %{name}+array-sizes-33-128-devel

This package contains library source intended for building other packages which
use the "array-sizes-33-128" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A vector with fixed capacity, backed by an array (it can be stored on...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A vector with fixed capacity, backed by an array (it can be stored on...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-const-fn-devel
Summary:        A vector with fixed capacity, backed by an array (it can be stored on...
BuildArch:      noarch
%description -n %{name}+unstable-const-fn-devel

This package contains library source intended for building other packages which
use the "unstable-const-fn" feature of the "%{crate}" crate.

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
%files -n rust-arrayvec0.5-devel -f %{oreon_filedir}/rust-arrayvec0.5-devel.list

%changelog

%autochangelog
