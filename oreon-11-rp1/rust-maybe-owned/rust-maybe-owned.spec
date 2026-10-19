%global source0_hash 4facc753ae494aeb6e3c22f839b158aebd4f9270f55cd3c79906c45476c47ab4
%bcond check 0
%global debug_package %{nil}
%global crate maybe-owned
Name:           rust-maybe-owned
Version:        0.3.4
Release:        1%{?dist}
Summary:        provides a `MaybeOwned` (and `MaybeOwnedMut`) type similar to std's `...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/maybe-owned
Source0:        https://static.crates.io/crates/maybe-owned/maybe-owned-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        provides a `MaybeOwned` (and `MaybeOwnedMut`) type similar to std's `...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-maybe-owned-devel -f %{oreon_filedir}/rust-maybe-owned-devel.list

%changelog

%autochangelog
