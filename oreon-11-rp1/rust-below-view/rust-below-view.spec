%global source0_hash 9b71f83306cb0b758f450bcea03b7cc550ea18a0d1020057b502eec13ad2129f
%bcond check 1
%global debug_package %{nil}
%global crate below-view
%global unsupported_arches %{ix86}
Name:           rust-below-view
Version:        0.9.0
Release:        1%{?dist}
Summary:        View crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-view
Source0:        https://static.crates.io/crates/below-view/below-view-%{version}.crate
Patch:          below-view-fix-metadata.diff
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
Summary:        View crate for below
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifnarch %{unsupported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifnarch %{unsupported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-below-view-devel -f %{oreon_filedir}/rust-below-view-devel.list

%changelog

%autochangelog
