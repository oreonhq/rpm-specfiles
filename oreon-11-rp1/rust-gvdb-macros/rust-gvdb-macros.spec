%global source0_hash da74c814e031bedf9606a4403e70a1904443ae91c32618852d5126c34690ffbf
%bcond check 1
%global debug_package %{nil}
%global crate gvdb-macros
Name:           rust-gvdb-macros
Version:        0.1.16
Release:        1%{?dist}
Summary:        Convenience macros for gvdb
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gvdb-macros
Source0:        https://static.crates.io/crates/gvdb-macros/gvdb-macros-%{version}.crate
Patch:          gvdb-macros-fix-metadata.diff
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
Summary:        Convenience macros for gvdb
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
%files -n rust-gvdb-macros-devel -f %{oreon_filedir}/rust-gvdb-macros-devel.list

%changelog

%autochangelog
