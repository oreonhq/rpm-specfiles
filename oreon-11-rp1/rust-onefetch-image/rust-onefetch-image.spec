%global source0_hash 7f8974346c206a318154120d1662eb9f6883b3ccea96ef781c5225e222c5685b
%bcond check 1
%global debug_package %{nil}
%global crate onefetch-image
Name:           rust-onefetch-image
Version:        2.27.1
Release:        1%{?dist}
Summary:        Display images in the terminal
License:        MIT
URL:            https://crates.io/crates/onefetch-image
Source0:        https://static.crates.io/crates/onefetch-image/onefetch-image-%{version}.crate
Patch:          onefetch-image-fix-metadata.diff
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
Summary:        Display images in the terminal
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
%files -n rust-onefetch-image-devel -f %{oreon_filedir}/rust-onefetch-image-devel.list

%changelog

%autochangelog
