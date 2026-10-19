%global source0_hash 007d8adb5ddab6f8e3f491ac63566a7d5002cc7ed73901f72057943fa71ae1ae
%bcond check 0
%global debug_package %{nil}
%global crate pulldown-cmark-escape
Name:           rust-pulldown-cmark-escape
Version:        0.11.0
Release:        1%{?dist}
Summary:        An escape library for HTML created in the pulldown-cmark project
License:        MIT
URL:            https://crates.io/crates/pulldown-cmark-escape
Source0:        https://static.crates.io/crates/pulldown-cmark-escape/pulldown-cmark-escape-%{version}.crate
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

%package     -n %{name}+simd-devel
Summary:        An escape library for HTML created in the pulldown-cmark project
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

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
%files -n rust-pulldown-cmark-escape-devel -f %{oreon_filedir}/rust-pulldown-cmark-escape-devel.list

%changelog

%autochangelog
