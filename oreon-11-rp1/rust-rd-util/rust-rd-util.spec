%global source0_hash 7bc41ee67a18430bd6af994c5875398c12dc1746fe704edcf0a25c6b0075b13a
%bcond check 1
%global debug_package %{nil}
%global crate rd-util
Name:           rust-rd-util
Version:        2.2.5
Release:        1%{?dist}
Summary:        Utility collection library for resctl-demo
License:        Apache-2.0
URL:            https://crates.io/crates/rd-util
Source0:        https://static.crates.io/crates/rd-util/rd-util-%{version}.crate
Patch:          rd-util-fix-metadata.diff
Patch10:        rd-util-vergen-bump.patch
Patch11:        rd-util-cargo-fmt.patch
Patch12:        rd-util-vergen-improve.patch
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
Summary:        Utility collection library for resctl-demo
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
%files -n rust-rd-util-devel -f %{oreon_filedir}/rust-rd-util-devel.list

%changelog

%autochangelog
