%global source0_hash 65043da274378d68241eb9a8f8f8aa54e349136f7b8e12f63e3ef44043cc30e1
%bcond check 0
%global debug_package %{nil}
%global crate hamming
Name:           rust-hamming
Version:        0.1.3
Release:        1%{?dist}
Summary:        Count ones, fast (aka popcount, hamming weight)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hamming
Source0:        https://static.crates.io/crates/hamming/hamming-%{version}.crate
Patch:          rust-hamming-deps.patch
Patch:          rust-hamming-quickcheck.patch
ExclusiveArch:  %{rust_arches}
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
Summary:        Count ones, fast (aka popcount, hamming weight)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Count ones, fast (aka popcount, hamming weight)
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-hamming-devel -f %{oreon_filedir}/rust-hamming-devel.list

%changelog

%autochangelog
