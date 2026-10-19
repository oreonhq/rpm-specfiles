%global source0_hash f30360d7979f5e9c6e6cea48af192ea8fab4afb3cf72597154b8f08935bc9c7f
%bcond check 0
%global debug_package %{nil}
%global crate unsafe-any
Name:           rust-unsafe-any
Version:        0.4.2
Release:        1%{?dist}
Summary:        Traits and implementations for unchecked downcasting.
License:        MIT
URL:            https://crates.io/crates/unsafe-any
Source0:        https://static.crates.io/crates/unsafe-any/unsafe-any-%{version}.crate
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
Summary:        Traits and implementations for unchecked downcasting.
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
%files -n rust-unsafe-any-devel -f %{oreon_filedir}/rust-unsafe-any-devel.list

%changelog

%autochangelog
