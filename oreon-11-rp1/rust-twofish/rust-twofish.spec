%global source0_hash a78e83a30223c757c3947cd144a31014ff04298d8719ae10d03c31c0448c8013
%bcond check 0
%global debug_package %{nil}
%global crate twofish
Name:           rust-twofish
Version:        0.7.1
Release:        1%{?dist}
Summary:        Twofish block cipher
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/twofish
Source0:        https://static.crates.io/crates/twofish/twofish-%{version}.crate
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

%package     -n %{name}+zeroize-devel
Summary:        Twofish block cipher
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-twofish-devel -f %{oreon_filedir}/rust-twofish-devel.list

%changelog

%autochangelog
