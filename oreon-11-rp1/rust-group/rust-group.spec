%global source0_hash 7fd1a1c7a5206c5b7a3f5a0d7ccd3ff85d0c8f5133d62a02680255b0004af5f4
%bcond check 0
%global debug_package %{nil}
%global crate group
Name:           rust-group
Version:        0.14.0
Release:        1%{?dist}
Summary:        Elliptic curve group traits and utilities
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/group
Source0:        https://static.crates.io/crates/group/group-%{version}.crate
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
Summary:        Elliptic curve group traits and utilities
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Elliptic curve group traits and utilities
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+memuse-devel
Summary:        Elliptic curve group traits and utilities
BuildArch:      noarch
%description -n %{name}+memuse-devel

This package contains library source intended for building other packages which
use the "memuse" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Elliptic curve group traits and utilities
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rand_xorshift-devel
Summary:        Elliptic curve group traits and utilities
BuildArch:      noarch
%description -n %{name}+rand_xorshift-devel

This package contains library source intended for building other packages which
use the "rand_xorshift" feature of the "%{crate}" crate.

%package     -n %{name}+tests-devel
Summary:        Elliptic curve group traits and utilities
BuildArch:      noarch
%description -n %{name}+tests-devel

This package contains library source intended for building other packages which
use the "tests" feature of the "%{crate}" crate.

%package     -n %{name}+wnaf-memuse-devel
Summary:        Elliptic curve group traits and utilities
BuildArch:      noarch
%description -n %{name}+wnaf-memuse-devel

This package contains library source intended for building other packages which
use the "wnaf-memuse" feature of the "%{crate}" crate.

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
%files -n rust-group-devel -f %{oreon_filedir}/rust-group-devel.list

%changelog

%autochangelog
