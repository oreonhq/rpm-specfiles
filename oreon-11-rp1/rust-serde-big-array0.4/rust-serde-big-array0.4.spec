%global source0_hash 3323f09a748af288c3dc2474ea6803ee81f118321775bffa3ac8f7e65c5e90e7
%bcond check 0
%global debug_package %{nil}
%global crate serde-big-array
Name:           rust-serde-big-array0.4
Version:        0.4.1
Release:        1%{?dist}
Summary:        Big array helper for serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde-big-array
Source0:        https://static.crates.io/crates/serde-big-array/serde-big-array-%{version}.crate
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
Summary:        Big array helper for serde
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
%files -n rust-serde-big-array0.4-devel -f %{oreon_filedir}/rust-serde-big-array0.4-devel.list

%changelog

%autochangelog
