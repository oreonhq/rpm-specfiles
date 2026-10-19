%global source0_hash 63af43ff4431e848fb47472a920f14fa71c24de13255a5692e93d4e90302acb0
%bcond check 1
%global debug_package %{nil}
%global crate expect-test
Name:           rust-expect-test
Version:        1.5.1
Release:        1%{?dist}
Summary:        Minimalistic snapshot testing library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/expect-test
Source0:        https://static.crates.io/crates/expect-test/expect-test-%{version}.crate
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
Summary:        Minimalistic snapshot testing library
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
%files -n rust-expect-test-devel -f %{oreon_filedir}/rust-expect-test-devel.list

%changelog

%autochangelog
