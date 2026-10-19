%global source0_hash 011cbb39cf7c1f62871aea3cc46e5817b0937b49e9447370c93cacbe93a766d8
%bcond check 1
%global debug_package %{nil}
%global crate strip-ansi-escapes
Name:           rust-strip-ansi-escapes0.1
Version:        0.1.1
Release:        1%{?dist}
Summary:        Strip ANSI escape sequences from byte streams
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/strip-ansi-escapes
Source0:        https://static.crates.io/crates/strip-ansi-escapes/strip-ansi-escapes-%{version}.crate
Patch:          strip-ansi-escapes-fix-metadata.diff
Patch10:        strip-ansi-escapes-0.1.1-vte-0.15.patch
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
%files -n rust-strip-ansi-escapes0.1-devel -f %{oreon_filedir}/rust-strip-ansi-escapes0.1-devel.list

%changelog

%autochangelog
