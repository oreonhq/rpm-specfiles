%global source0_hash 8225fa9cacbdd3c0eccaf5cab3f1920b70b02447ff67b4af1ca15873d2fa445f
%bcond check 0
%global debug_package %{nil}
%global crate wbmp
Name:           rust-wbmp
Version:        0.1.2
Release:        1%{?dist}
Summary:        WBMP encoder and decoder
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wbmp
Source0:        https://static.crates.io/crates/wbmp/wbmp-%{version}.crate
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
Summary:        WBMP encoder and decoder
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
%files -n rust-wbmp-devel -f %{oreon_filedir}/rust-wbmp-devel.list

%changelog

%autochangelog
