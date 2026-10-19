%global source0_hash 30c56b407dc31cd2a6301b616069b922e204311f54d5890ecaf62090ec1a13a6
%bcond check 1
%global crate btrd
Name:           rust-btrd
Version:        0.5.3
Release:        1%{?dist}
Summary:        Btrfs debugger
License:        GPL-2.0-only
URL:            https://crates.io/crates/btrd
Source0:        https://static.crates.io/crates/btrd/btrd-%{version}.crate
Patch:          btrd-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Btrfs debugger
License:        %{shrink:
    GPL-2.0-only
    AND MIT
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Btrfs debugger
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
%files -n btrd -f %{oreon_filedir}/btrd.list
%files -n rust-btrd-devel -f %{oreon_filedir}/rust-btrd-devel.list

%changelog

%autochangelog
