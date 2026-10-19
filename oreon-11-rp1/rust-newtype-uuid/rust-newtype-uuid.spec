%global source0_hash 5c012d14ef788ab066a347d19e3dda699916c92293b05b85ba2c76b8c82d2830
%bcond check 1
%global debug_package %{nil}
%global crate newtype-uuid
Name:           rust-newtype-uuid
Version:        1.3.2
Release:        1%{?dist}
Summary:        Newtype wrapper around UUIDs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/newtype-uuid
Source0:        https://static.crates.io/crates/newtype-uuid/newtype-uuid-%{version}.crate
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
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+proptest1-devel
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+proptest1-devel

This package contains library source intended for building other packages which
use the "proptest1" feature of the "%{crate}" crate.

%package     -n %{name}+schemars08-devel
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+schemars08-devel

This package contains library source intended for building other packages which
use the "schemars08" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+v4-devel
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+v4-devel

This package contains library source intended for building other packages which
use the "v4" feature of the "%{crate}" crate.

%package     -n %{name}+v7-devel
Summary:        Newtype wrapper around UUIDs
BuildArch:      noarch
%description -n %{name}+v7-devel

This package contains library source intended for building other packages which
use the "v7" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-newtype-uuid-devel -f %{oreon_filedir}/rust-newtype-uuid-devel.list

%changelog

%autochangelog
