%global source0_hash c34fda576c83213fdb886c81759def114b3596309a5d51e1fc5e59ec178658b3
%bcond check 1
%global debug_package %{nil}
%global crate onefetch-manifest
Name:           rust-onefetch-manifest
Version:        2.27.1
Release:        1%{?dist}
Summary:        Detect and parse manifest files
License:        MIT
URL:            https://crates.io/crates/onefetch-manifest
Source0:        https://static.crates.io/crates/onefetch-manifest/onefetch-manifest-%{version}.crate
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
Summary:        Detect and parse manifest files
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

%cargo_test -- -- --skip should_detect_and_parse_cargo_manifest
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-onefetch-manifest-devel -f %{oreon_filedir}/rust-onefetch-manifest-devel.list

%changelog

%autochangelog
