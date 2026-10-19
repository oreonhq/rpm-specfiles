%global source0_hash 04d6d3dc0ccd22a30619df68ce347c844d8adb49b822f42660d9a92e6ae14540
%bcond check 1
%global debug_package %{nil}
%global crate gufo-webp
Name:           rust-gufo-webp
Version:        0.5.0
Release:        1%{?dist}
Summary:        Data structure for WebP images
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/gufo-webp
Source0:        https://static.crates.io/crates/gufo-webp/gufo-webp-%{version}.crate
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
Summary:        Data structure for WebP images
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
%files -n rust-gufo-webp-devel -f %{oreon_filedir}/rust-gufo-webp-devel.list

%changelog

%autochangelog
