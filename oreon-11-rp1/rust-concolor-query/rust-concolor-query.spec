%global source0_hash 88d11d52c3d7ca2e6d0040212be9e4dbbcd78b6447f535b6b561f449427944cf
%bcond check 0
%global debug_package %{nil}
%global crate concolor-query
Name:           rust-concolor-query
Version:        0.3.3
Release:        1%{?dist}
Summary:        Look up colored console capabilities
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/concolor-query
Source0:        https://static.crates.io/crates/concolor-query/concolor-query-%{version}.crate
Patch:          concolor-query-fix-metadata-auto.diff
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
Summary:        Look up colored console capabilities
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
%files -n rust-concolor-query-devel -f %{oreon_filedir}/rust-concolor-query-devel.list

%changelog

%autochangelog
