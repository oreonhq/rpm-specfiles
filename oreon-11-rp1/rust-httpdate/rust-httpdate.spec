%global source0_hash df3b46402a9d5adb4c86a0cf463f42e19994e3ee891101b1841f30a545cb49a9
%bcond check 0
%global debug_package %{nil}
%global crate httpdate
Name:           rust-httpdate
Version:        1.0.3
Release:        1%{?dist}
Summary:        HTTP date parsing and formatting
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/httpdate
Source0:        https://static.crates.io/crates/httpdate/httpdate-%{version}.crate
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
Summary:        HTTP date parsing and formatting
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
%files -n rust-httpdate-devel -f %{oreon_filedir}/rust-httpdate-devel.list

%changelog

%autochangelog
