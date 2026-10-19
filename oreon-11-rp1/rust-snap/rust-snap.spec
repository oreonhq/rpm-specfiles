%global source0_hash 199905e6153d6405f9728fe44daace35f8f837bbf830bb6e85fbd5828709a886
%bcond check 1
%global debug_package %{nil}
%global crate snap
Name:           rust-snap
Version:        1.1.2
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Snappy compression algorithm
License:        BSD-3-Clause
URL:            https://crates.io/crates/snap
Source0:        https://static.crates.io/crates/snap/snap-%{version}.crate
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
Summary:        Pure Rust implementation of the Snappy compression algorithm
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
%files -n rust-snap-devel -f %{oreon_filedir}/rust-snap-devel.list

%changelog

%autochangelog
