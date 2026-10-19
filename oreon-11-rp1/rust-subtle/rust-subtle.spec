%global source0_hash 13c2bddecc57b384dee18652358fb23172facb8a2c51ccc10d74c157bdea3292
%bcond check 1
%global debug_package %{nil}
%global crate subtle
Name:           rust-subtle
Version:        2.6.1
Release:        1%{?dist}
Summary:        Pure-Rust traits and utilities for constant-time cryptographic
License:        BSD-3-Clause
URL:            https://crates.io/crates/subtle
Source0:        https://static.crates.io/crates/subtle/subtle-%{version}.crate
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
Summary:        Pure-Rust traits and utilities for constant-time cryptographic
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+const-generics-devel
Summary:        Pure-Rust traits and utilities for constant-time cryptographic
BuildArch:      noarch
%description -n %{name}+const-generics-devel

This package contains library source intended for building other packages which
use the "const-generics" feature of the "%{crate}" crate.

%package     -n %{name}+core_hint_black_box-devel
Summary:        Pure-Rust traits and utilities for constant-time cryptographic
BuildArch:      noarch
%description -n %{name}+core_hint_black_box-devel

This package contains library source intended for building other packages which
use the "core_hint_black_box" feature of the "%{crate}" crate.

%package     -n %{name}+i128-devel
Summary:        Pure-Rust traits and utilities for constant-time cryptographic
BuildArch:      noarch
%description -n %{name}+i128-devel

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Pure-Rust traits and utilities for constant-time cryptographic
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure-Rust traits and utilities for constant-time cryptographic
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
%files -n rust-subtle-devel -f %{oreon_filedir}/rust-subtle-devel.list

%changelog

%autochangelog
