%global source0_hash 35fb2e5f958ec131621fdd531e9fc186ed768cbe395337403ae56c17a74c68ec
%bcond check 0
%global debug_package %{nil}
%global crate pastey
Name:           rust-pastey
Version:        0.1.1
Release:        1%{?dist}
Summary:        Macros for all your token pasting needs. Successor of paste.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pastey
Source0:        https://static.crates.io/crates/pastey/pastey-%{version}.crate
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
Summary:        Macros for all your token pasting needs. Successor of paste.
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
%files -n rust-pastey-devel -f %{oreon_filedir}/rust-pastey-devel.list

%changelog

%autochangelog
