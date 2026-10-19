%global source0_hash ab8ecd87370524b461f8557c119c405552c396ed91fc0a8eec68679eab26f94a
%bcond check 1
%global debug_package %{nil}
%global crate dlib
Name:           rust-dlib
Version:        0.5.3
Release:        1%{?dist}
Summary:        Helper macros for handling manually loading optional system libraries
License:        MIT
URL:            https://crates.io/crates/dlib
Source0:        https://static.crates.io/crates/dlib/dlib-%{version}.crate
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
Summary:        Helper macros for handling manually loading optional system libraries
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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-dlib-devel -f %{oreon_filedir}/rust-dlib-devel.list

%changelog

%autochangelog
