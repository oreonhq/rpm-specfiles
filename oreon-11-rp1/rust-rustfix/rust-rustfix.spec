%global source0_hash 4ab550bf03e3428c98b8e0354800a18f366f1f5f25544b908463b4634374f34f
%bcond check 0
%global debug_package %{nil}
%global crate rustfix
Name:           rust-rustfix
Version:        0.9.7
Release:        1%{?dist}
Summary:        Automatically apply the suggestions made by rustc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustfix
Source0:        https://static.crates.io/crates/rustfix/rustfix-%{version}.crate
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
Summary:        Automatically apply the suggestions made by rustc
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
%files -n rust-rustfix-devel -f %{oreon_filedir}/rust-rustfix-devel.list

%changelog

%autochangelog
