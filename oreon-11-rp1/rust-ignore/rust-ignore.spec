%global source0_hash 00b69833ed729dc5aa7d19541d96d6cf8e9137194207a04916d658e43168402f
%bcond check 1
%global debug_package %{nil}
%global crate ignore
Name:           rust-ignore
Version:        0.4.33
Release:        2%{?dist}
Summary:        Fast library for efficiently matching ignore files
License:        Unlicense OR MIT
URL:            https://crates.io/crates/ignore
Source0:        https://static.crates.io/crates/ignore/ignore-%{version}.crate
Patch:          ignore-fix-metadata-auto.diff
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
Summary:        Fast library for efficiently matching ignore files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+simd-accel-devel
Summary:        Fast library for efficiently matching ignore files
BuildArch:      noarch
%description -n %{name}+simd-accel-devel

This package contains library source intended for building other packages which
use the "simd-accel" feature of the "%{crate}" crate.

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
%files -n rust-ignore-devel -f %{oreon_filedir}/rust-ignore-devel.list

%changelog

%autochangelog
