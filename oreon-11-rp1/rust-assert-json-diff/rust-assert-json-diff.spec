%global source0_hash 47e4f2b81832e72834d7518d8487a0396a28cc408186a2e8854c0f98011faf12
%bcond check 0
%global debug_package %{nil}
%global crate assert-json-diff
Name:           rust-assert-json-diff
Version:        2.0.2
Release:        1%{?dist}
Summary:        Easily compare two JSON values and get great output
License:        MIT
URL:            https://crates.io/crates/assert-json-diff
Source0:        https://static.crates.io/crates/assert-json-diff/assert-json-diff-%{version}.crate
Patch:          assert-json-diff-fix-metadata.diff
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
Summary:        Easily compare two JSON values and get great output
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
%files -n rust-assert-json-diff-devel -f %{oreon_filedir}/rust-assert-json-diff-devel.list

%changelog

%autochangelog
