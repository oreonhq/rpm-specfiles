%global source0_hash 9d864c8c36a90db0d23fbeb090c3c79f11e28b63263f8a3d99157ac3320963b4
%bcond check 1
%global crate yubibomb
Name:           rust-yubibomb
Version:        0.2.14
Release:        1%{?dist}
Summary:        Rust command line tool that prints out a 6-digit random number
License:        GPL-3.0-only
URL:            https://crates.io/crates/yubibomb
Source0:        https://static.crates.io/crates/yubibomb/yubibomb-%{version}.crate
Patch:          yubibomb-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Rust command line tool that prints out a 6-digit random number
License:        GPL-3.0-only AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust command line tool that prints out a 6-digit random number
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
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n yubibomb -f %{oreon_filedir}/yubibomb.list
%files -n rust-yubibomb-devel -f %{oreon_filedir}/rust-yubibomb-devel.list

%changelog

%autochangelog
