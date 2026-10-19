%global source0_hash c57924a81864dddafba92e1bf92f9bf82f97096c44489548a60e888e1547549b
%bcond check 1
%global debug_package %{nil}
%global crate proptest-derive
Name:           rust-proptest-derive
Version:        0.8.0
Release:        1%{?dist}
Summary:        Custom-derive for the Arbitrary trait of proptest
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proptest-derive
Source0:        https://static.crates.io/crates/proptest-derive/proptest-derive-%{version}.crate
Patch:          proptest-derive-fix-metadata.diff
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
Summary:        Custom-derive for the Arbitrary trait of proptest
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+boxed_union-devel
Summary:        Custom-derive for the Arbitrary trait of proptest
BuildArch:      noarch
%description -n %{name}+boxed_union-devel

This package contains library source intended for building other packages which
use the "boxed_union" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -v tests/compiletest.rs
rm -vr tests/compile-fail/
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
%files -n rust-proptest-derive-devel -f %{oreon_filedir}/rust-proptest-derive-devel.list

%changelog

%autochangelog
