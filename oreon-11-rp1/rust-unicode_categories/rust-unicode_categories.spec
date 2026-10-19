%global source0_hash 39ec24b3121d976906ece63c9daad25b85969647682eee313cb5779fdd69e14e
%bcond check 0
%global debug_package %{nil}
%global crate unicode_categories
Name:           rust-unicode_categories
Version:        0.1.1
Release:        1%{?dist}
Summary:        Query Unicode category membership for chars
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode_categories
Source0:        https://static.crates.io/crates/unicode_categories/unicode_categories-%{version}.crate
Patch:          unicode_categories-fix-metadata.diff
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
Summary:        Query Unicode category membership for chars
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-unicode_categories-devel -f %{oreon_filedir}/rust-unicode_categories-devel.list

%changelog

%autochangelog
