%global source0_hash d8449ffffce7c124d479d122a2d1a8e9bea4b5a0dd578aabbe722de623d6556e
%bcond check 0
%global debug_package %{nil}
%global crate simplematch
Name:           rust-simplematch
Version:        0.3.1
Release:        1%{?dist}
Summary:        Fast wildcard pattern matching for strings and bytes with a simple api
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/simplematch
Source0:        https://static.crates.io/crates/simplematch/simplematch-%{version}.crate
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
Summary:        Fast wildcard pattern matching for strings and bytes with a simple api
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast wildcard pattern matching for strings and bytes with a simple api
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-simplematch-devel -f %{oreon_filedir}/rust-simplematch-devel.list

%changelog

%autochangelog
