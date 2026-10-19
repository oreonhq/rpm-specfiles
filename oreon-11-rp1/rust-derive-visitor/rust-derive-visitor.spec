%global source0_hash d47165df83b9707cbada3216607a5d66125b6a66906de0bc1216c0669767ca9e
%bcond check 0
%global debug_package %{nil}
%global crate derive-visitor
Name:           rust-derive-visitor
Version:        0.4.0
Release:        1%{?dist}
Summary:        Derive visitor pattern for arbitrary data structures
License:        MIT
URL:            https://crates.io/crates/derive-visitor
Source0:        https://static.crates.io/crates/derive-visitor/derive-visitor-%{version}.crate
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

%package     -n %{name}+std-types-drive-devel
Summary:        Derive visitor pattern for arbitrary data structures
BuildArch:      noarch
%description -n %{name}+std-types-drive-devel

This package contains library source intended for building other packages which
use the "std-types-drive" feature of the "%{crate}" crate.

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
%files -n rust-derive-visitor-devel -f %{oreon_filedir}/rust-derive-visitor-devel.list

%changelog

%autochangelog
