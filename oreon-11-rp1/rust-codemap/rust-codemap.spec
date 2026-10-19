%global source0_hash b9e769b5c8c8283982a987c6e948e540254f1058d5a74b8794914d4ef5fc2a24
%bcond check 1
%global debug_package %{nil}
%global crate codemap
Name:           rust-codemap
Version:        0.1.3
Release:        1%{?dist}
Summary:        Data structure for efficiently storing source code position and span information
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/codemap
Source0:        https://static.crates.io/crates/codemap/codemap-%{version}.crate
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
Summary:        Data structure for efficiently storing source code position and span information
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
%files -n rust-codemap-devel -f %{oreon_filedir}/rust-codemap-devel.list

%changelog

%autochangelog
