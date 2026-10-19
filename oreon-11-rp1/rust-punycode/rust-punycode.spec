%global source0_hash e9e1dcb320d6839f6edb64f7a4a59d39b30480d4d1765b56873f7c858538a5fe
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate punycode
Name:           rust-punycode
Version:        0.4.1
Release:        1%{?dist}
Summary:        Functions to decode and encode Punycode
License:        MIT
URL:            https://crates.io/crates/punycode
Source0:        https://static.crates.io/crates/punycode/punycode-%{version}.crate
Patch:          punycode-fix-metadata.diff
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
Summary:        Functions to decode and encode Punycode
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
%files -n rust-punycode-devel -f %{oreon_filedir}/rust-punycode-devel.list

%changelog

%autochangelog
