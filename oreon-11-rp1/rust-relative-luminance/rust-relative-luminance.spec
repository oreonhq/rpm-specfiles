%global source0_hash 80010a7606585ed19af01ebd8ffed344b1bf9cdcfef6eb10100ab07421324f05
%bcond check 1
%global debug_package %{nil}
%global crate relative-luminance
Name:           rust-relative-luminance
Version:        1.0.0
Release:        1%{?dist}
Summary:        Utilities to manage relative luminance
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/relative-luminance
Source0:        https://static.crates.io/crates/relative-luminance/relative-luminance-%{version}.crate
Patch:          relative-luminance-fix-metadata.diff
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
Summary:        Utilities to manage relative luminance
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm examples/contrast.rs
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
%files -n rust-relative-luminance-devel -f %{oreon_filedir}/rust-relative-luminance-devel.list

%changelog

%autochangelog
