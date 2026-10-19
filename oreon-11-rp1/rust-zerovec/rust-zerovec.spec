%global source0_hash bb0464e17806c1d976d5cba29399c7f08e516e279e2ba493f63123b5fca67dd8
%bcond check 0
%global debug_package %{nil}
%global crate zerovec
Name:           rust-zerovec
Version:        0.11.8
Release:        1%{?dist}
Summary:        Zero-copy vector backed by a byte array
License:        Unicode-3.0
URL:            https://crates.io/crates/zerovec
Source0:        https://static.crates.io/crates/zerovec/zerovec-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+databake-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+databake-devel

This package contains library source intended for building other packages which
use the "databake" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+hashmap-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+hashmap-devel

This package contains library source intended for building other packages which
use the "hashmap" feature of the "%{crate}" crate.

%package     -n %{name}+schemars-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+schemars-devel

This package contains library source intended for building other packages which
use the "schemars" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+yoke-devel
Summary:        Zero-copy vector backed by a byte array
BuildArch:      noarch
%description -n %{name}+yoke-devel

This package contains library source intended for building other packages which
use the "yoke" feature of the "%{crate}" crate.

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
%files -n rust-zerovec-devel -f %{oreon_filedir}/rust-zerovec-devel.list

%changelog

%autochangelog
