%global source0_hash 60302e4db3a61da70c0cb7991976248362f30319e88850c487b9b95bbf059e00
%bcond check 0
%global debug_package %{nil}
%global crate maybe-uninit
Name:           rust-maybe-uninit
Version:        2.0.0
Release:        1%{?dist}
Summary:        MaybeUninit for friends of backwards compatibility
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/maybe-uninit
Source0:        https://static.crates.io/crates/maybe-uninit/maybe-uninit-%{version}.crate
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
Summary:        MaybeUninit for friends of backwards compatibility
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
%files -n rust-maybe-uninit-devel -f %{oreon_filedir}/rust-maybe-uninit-devel.list

%changelog

%autochangelog
