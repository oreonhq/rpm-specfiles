%global source0_hash d245f478577f809a851594d02313b640fb437e0bb33866753cff937863096954
%bcond check 0
%global debug_package %{nil}
%global crate unicode-ident
Name:           rust-unicode-ident
Version:        1.0.26
Release:        1%{?dist}
Summary:        Determine whether characters have the XID_Start or XID_Continue properties
License:        (MIT OR Apache-2.0) AND Unicode-3.0
URL:            https://crates.io/crates/unicode-ident
Source0:        https://static.crates.io/crates/unicode-ident/unicode-ident-%{version}.crate
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
Summary:        Determine whether characters have the XID_Start or XID_Continue properties
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
%files -n rust-unicode-ident-devel -f %{oreon_filedir}/rust-unicode-ident-devel.list

%changelog

%autochangelog
