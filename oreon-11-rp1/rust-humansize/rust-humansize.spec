%global source0_hash 6cb51c9a029ddc91b07a787f1d86b53ccfa49b0e86688c946ebe8d3555685dd7
%bcond check 0
%global debug_package %{nil}
%global crate humansize
Name:           rust-humansize
Version:        2.1.3
Release:        1%{?dist}
Summary:        A configurable crate to easily represent sizes in a human-readable fo...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/humansize
Source0:        https://static.crates.io/crates/humansize/humansize-%{version}.crate
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

%package     -n %{name}+impl_style-devel
Summary:        A configurable crate to easily represent sizes in a human-readable fo...
BuildArch:      noarch
%description -n %{name}+impl_style-devel

This package contains library source intended for building other packages which
use the "impl_style" feature of the "%{crate}" crate.

%package     -n %{name}+no_alloc-devel
Summary:        A configurable crate to easily represent sizes in a human-readable fo...
BuildArch:      noarch
%description -n %{name}+no_alloc-devel

This package contains library source intended for building other packages which
use the "no_alloc" feature of the "%{crate}" crate.

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
%files -n rust-humansize-devel -f %{oreon_filedir}/rust-humansize-devel.list

%changelog

%autochangelog
