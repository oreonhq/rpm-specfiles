%global source0_hash b2b03ff07a220d0d0ec9a1f0f238951b7967a5a2e96aefcd21a117b1083415e9
%bcond check 0
%global debug_package %{nil}
%global crate opener
Name:           rust-opener
Version:        0.8.5
Release:        1%{?dist}
Summary:        Open a file or link using the system default program.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/opener
Source0:        https://static.crates.io/crates/opener/opener-%{version}.crate
Patch:          opener-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/default) = %{version}
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+reveal-devel
Summary:        Open a file or link using the system default program.
BuildArch:      noarch
%description -n %{name}+reveal-devel

This package contains library source intended for building other packages which
use the "reveal" feature of the "%{crate}" crate.

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
%files -n rust-opener-devel -f %{oreon_filedir}/rust-opener-devel.list

%changelog

%autochangelog
