%global source0_hash 2a8f8038e7e7969abb3f1b7c2a811225e9296da208539e0f79c5251d6cac0025
%bcond check 1
%global debug_package %{nil}
%global crate strip-ansi-escapes
Name:           rust-strip-ansi-escapes
Version:        0.2.1
Release:        1%{?dist}
Summary:        Strip ANSI escape sequences from byte streams
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/strip-ansi-escapes
Source0:        https://static.crates.io/crates/strip-ansi-escapes/strip-ansi-escapes-%{version}.crate
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
Summary:        Strip ANSI escape sequences from byte streams
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
%files -n rust-strip-ansi-escapes-devel -f %{oreon_filedir}/rust-strip-ansi-escapes-devel.list

%changelog

%autochangelog
