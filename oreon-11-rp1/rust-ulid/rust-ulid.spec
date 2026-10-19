%global source0_hash 470dbf6591da1b39d43c14523b2b469c86879a53e8b758c8e090a470fe7b1fbe
%bcond check 1
%global debug_package %{nil}
%global crate ulid
Name:           rust-ulid
Version:        1.2.1
Release:        1%{?dist}
Summary:        Universally Unique Lexicographically Sortable Identifier implementation
License:        MIT
URL:            https://crates.io/crates/ulid
Source0:        https://static.crates.io/crates/ulid/ulid-%{version}.crate
Patch:          ulid-fix-metadata-auto.diff
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
Summary:        Universally Unique Lexicographically Sortable Identifier implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Universally Unique Lexicographically Sortable Identifier implementation
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        Universally Unique Lexicographically Sortable Identifier implementation
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Universally Unique Lexicographically Sortable Identifier implementation
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Universally Unique Lexicographically Sortable Identifier implementation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Universally Unique Lexicographically Sortable Identifier implementation
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

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
%files -n rust-ulid-devel -f %{oreon_filedir}/rust-ulid-devel.list

%changelog

%autochangelog
