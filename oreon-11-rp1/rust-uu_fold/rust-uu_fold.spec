%global source0_hash 8098e158f38287fe1144c3e7337856c6ac6e6f45c9924e75592d45e78dc467e6
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_fold
Name:           rust-uu_fold
Version:        0.7.0
Release:        1%{?dist}
Summary:        fold ~ (uutils) wrap each line of input
License:        MIT
URL:            https://crates.io/crates/uu_fold
Source0:        https://static.crates.io/crates/uu_fold/uu_fold-%{version}.crate
Patch:          uu_fold-fix-metadata.diff
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
Summary:        fold ~ (uutils) wrap each line of input
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
%files -n rust-uu_fold-devel -f %{oreon_filedir}/rust-uu_fold-devel.list

%changelog

%autochangelog
