%global source0_hash 89d3a777c4afd632e8964d7de070b3aede81a2c116cef6e048f5a9acf0cdda3d
%bcond check 1
%global debug_package %{nil}
%global crate rbspy-testdata
Name:           rust-rbspy-testdata
Version:        0.2.2
Release:        1%{?dist}
Summary:        Test data for rbspy
License:        MIT
URL:            https://crates.io/crates/rbspy-testdata
Source0:        https://static.crates.io/crates/rbspy-testdata/rbspy-testdata-%{version}.crate
ExcludeArch:    %{ix86}
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
Summary:        Test data for rbspy
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
%files -n rust-rbspy-testdata-devel -f %{oreon_filedir}/rust-rbspy-testdata-devel.list

%changelog

%autochangelog
