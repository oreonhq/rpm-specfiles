%global source0_hash 021de5b5c26efd544c694cef9b8a9abe8633481bf3be1ea145a18a740818b291
%bcond check 0
%global debug_package %{nil}
%global crate sval_nested
Name:           rust-sval_nested
Version:        2.20.0
Release:        1%{?dist}
Summary:        A recursive variant of sval
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_nested
Source0:        https://static.crates.io/crates/sval_nested/sval_nested-%{version}.crate
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
Summary:        A recursive variant of sval
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A recursive variant of sval
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+no_debug_assertions-devel
Summary:        A recursive variant of sval
BuildArch:      noarch
%description -n %{name}+no_debug_assertions-devel

This package contains library source intended for building other packages which
use the "no_debug_assertions" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A recursive variant of sval
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
%files -n rust-sval_nested-devel -f %{oreon_filedir}/rust-sval_nested-devel.list

%changelog

%autochangelog
