%global source0_hash bfd4b08ab6476df57ad80f0079524c6b98ca3a70b038fe9abfd5d44f9577ab1e
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_chcon
Name:           rust-uu_chcon
Version:        0.12.0
Release:        1%{?dist}
Summary:        chcon ~ (uutils) change file security context
License:        MIT
URL:            https://crates.io/crates/uu_chcon
Source0:        https://static.crates.io/crates/uu_chcon/uu_chcon-%{version}.crate
Patch:          uu_chcon-fix-metadata.diff
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
Summary:        chcon ~ (uutils) change file security context
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
%files -n rust-uu_chcon-devel -f %{oreon_filedir}/rust-uu_chcon-devel.list

%changelog

%autochangelog
