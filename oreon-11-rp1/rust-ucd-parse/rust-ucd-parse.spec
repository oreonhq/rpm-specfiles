%global source0_hash c06ff81122fcbf4df4c1660b15f7e3336058e7aec14437c9f85c6b31a0f279b9
%bcond_without check
%global debug_package %{nil}
%global crate ucd-parse
Name:           rust-ucd-parse
Version:        0.1.13
Release:        1%{?dist}
Summary:        Library for parsing data files in the Unicode character database
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ucd-parse
Source0:        https://static.crates.io/crates/ucd-parse/ucd-parse-%{version}.crate
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
Summary:        Library for parsing data files in the Unicode character database
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
%files -n rust-ucd-parse-devel -f %{oreon_filedir}/rust-ucd-parse-devel.list

%changelog

%autochangelog
