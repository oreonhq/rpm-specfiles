%global source0_hash e0242819d153cba4b4b05a5a8f2a7e9bbf97b6055b2a002b395c96b5ff3c0222
%bcond check 0
%global debug_package %{nil}
%global crate instant
Name:           rust-instant
Version:        0.1.13
Release:        1%{?dist}
Summary:        Unmaintained, consider using web-time instead - A partial replacement...
License:        BSD-3-Clause
URL:            https://crates.io/crates/instant
Source0:        https://static.crates.io/crates/instant/instant-%{version}.crate
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

%package     -n %{name}+inaccurate-devel
Summary:        Unmaintained, consider using web-time instead - A partial replacement...
BuildArch:      noarch
%description -n %{name}+inaccurate-devel

This package contains library source intended for building other packages which
use the "inaccurate" feature of the "%{crate}" crate.

%package     -n %{name}+now-devel
Summary:        Unmaintained, consider using web-time instead - A partial replacement...
BuildArch:      noarch
%description -n %{name}+now-devel

This package contains library source intended for building other packages which
use the "now" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-bindgen-devel
Summary:        Unmaintained, consider using web-time instead - A partial replacement...
BuildArch:      noarch
%description -n %{name}+wasm-bindgen-devel

This package contains library source intended for building other packages which
use the "wasm-bindgen" feature of the "%{crate}" crate.

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
%files -n rust-instant-devel -f %{oreon_filedir}/rust-instant-devel.list

%changelog

%autochangelog
