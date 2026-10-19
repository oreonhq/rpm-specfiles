%global source0_hash 7d5515a3834141de9eafb9717ad39eea8247b5674e6066c404e8c4b365d2a29e
%bcond check 0
%global debug_package %{nil}
%global crate ctutils
Name:           rust-ctutils
Version:        0.4.2
Release:        1%{?dist}
Summary:        Constant-time utility library with selection and equality testing sup...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ctutils
Source0:        https://static.crates.io/crates/ctutils/ctutils-%{version}.crate
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
Summary:        Constant-time utility library with selection and equality testing sup...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+subtle-devel
Summary:        Constant-time utility library with selection and equality testing sup...
BuildArch:      noarch
%description -n %{name}+subtle-devel

This package contains library source intended for building other packages which
use the "subtle" feature of the "%{crate}" crate.

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
%files -n rust-ctutils-devel -f %{oreon_filedir}/rust-ctutils-devel.list

%changelog

%autochangelog
