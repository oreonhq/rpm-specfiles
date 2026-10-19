%global source0_hash 6ef53697679d874d69f3160af80bc28de12730a985d57bdf2b47456ccb8b11f1
%bcond check 0
%global debug_package %{nil}
%global crate unicase_serde
Name:           rust-unicase_serde
Version:        0.1.0
Release:        1%{?dist}
Summary:        Serde Serialization and Deserialization for UniCase crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicase_serde
Source0:        https://static.crates.io/crates/unicase_serde/unicase_serde-%{version}.crate
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
Summary:        Serde Serialization and Deserialization for UniCase crate
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
%files -n rust-unicase_serde-devel -f %{oreon_filedir}/rust-unicase_serde-devel.list

%changelog

%autochangelog
