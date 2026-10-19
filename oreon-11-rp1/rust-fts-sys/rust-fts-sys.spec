%global source0_hash 9c03259139c9b098dd92241b046fedfeebcd6b000d491c821b24ced28558a9c2
%bcond check 1
%global debug_package %{nil}
%global crate fts-sys
Name:           rust-fts-sys
Version:        0.2.17
Release:        1%{?dist}
Summary:        File hierarchy traversal functions (FTS)
License:        MIT
URL:            https://crates.io/crates/fts-sys
Source0:        https://static.crates.io/crates/fts-sys/fts-sys-%{version}.crate
Patch:          fts-sys-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  glibc-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       glibc-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        File hierarchy traversal functions (FTS)
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
%files -n rust-fts-sys-devel -f %{oreon_filedir}/rust-fts-sys-devel.list

%changelog

%autochangelog
