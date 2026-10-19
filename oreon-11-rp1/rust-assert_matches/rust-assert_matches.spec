%global source0_hash 9b34d609dfbaf33d6889b2b7106d3ca345eacad44200913df5ba02bfd31d2ba9
%bcond_without check
%global debug_package %{nil}
%global crate assert_matches
Name:           rust-assert_matches
Version:        1.5.0
Release:        1%{?dist}
Summary:        Asserts that a value matches a pattern
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/assert_matches
Source0:        https://static.crates.io/crates/assert_matches/assert_matches-%{version}.crate
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
Summary:        Asserts that a value matches a pattern
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
%files -n rust-assert_matches-devel -f %{oreon_filedir}/rust-assert_matches-devel.list

%changelog

%autochangelog
