%global source0_hash 700357d9fb22b5232a85e34a413c1a76ae649f532c31107e402dc84e9c03bfb2
%bcond check 0
%global debug_package %{nil}
%global crate descape
Name:           rust-descape
Version:        3.0.0
Release:        1%{?dist}
Summary:        Adds a single extension trait for &str to unescape any backslashes.
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/descape
Source0:        https://static.crates.io/crates/descape/descape-%{version}.crate
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

%package     -n %{name}+core_error-devel
Summary:        Adds a single extension trait for &str to unescape any backslashes.
BuildArch:      noarch
%description -n %{name}+core_error-devel

This package contains library source intended for building other packages which
use the "core_error" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Adds a single extension trait for &str to unescape any backslashes.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-descape-devel -f %{oreon_filedir}/rust-descape-devel.list

%changelog

%autochangelog
