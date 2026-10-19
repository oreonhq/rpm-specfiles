%global source0_hash 301e07b2f92a4c78e05cade02eddc42f3088ec1059cdfdb701909754de5d4d1d
%bcond check 1
%global debug_package %{nil}
%global crate serde-prefix-all
Name:           rust-serde-prefix-all
Version:        0.1.0
Release:        1%{?dist}
Summary:        Attribute macro to add a prefix to all struct fields & enum variants
License:        MIT
URL:            https://crates.io/crates/serde-prefix-all
Source0:        https://static.crates.io/crates/serde-prefix-all/serde-prefix-all-%{version}.crate
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
Summary:        Attribute macro to add a prefix to all struct fields & enum variants
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
%files -n rust-serde-prefix-all-devel -f %{oreon_filedir}/rust-serde-prefix-all-devel.list

%changelog

%autochangelog
