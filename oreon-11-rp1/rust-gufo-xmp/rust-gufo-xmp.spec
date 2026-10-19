%global source0_hash 903aaa13213b860bbad3565e62f3fbd1087ca9404692ebe53728654653470561
%bcond check 1
%global debug_package %{nil}
%global crate gufo-xmp
Name:           rust-gufo-xmp
Version:        0.5.0
Release:        1%{?dist}
Summary:        Reading and editing for XMP data
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/gufo-xmp
Source0:        https://static.crates.io/crates/gufo-xmp/gufo-xmp-%{version}.crate
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
Summary:        Reading and editing for XMP data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Reading and editing for XMP data
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

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
%files -n rust-gufo-xmp-devel -f %{oreon_filedir}/rust-gufo-xmp-devel.list

%changelog

%autochangelog
