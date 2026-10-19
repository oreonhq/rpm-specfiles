%global source0_hash cdac492cc61879b5f1c87160cd9f0de405786c6668d9b351c152f4ff8b959976
%bcond check 0
%global debug_package %{nil}
%global crate rusqlite-macros
Name:           rust-rusqlite-macros
Version:        0.4.3
Release:        1%{?dist}
Summary:        Private implementation detail of rusqlite crate
License:        MIT
URL:            https://crates.io/crates/rusqlite-macros
Source0:        https://static.crates.io/crates/rusqlite-macros/rusqlite-macros-%{version}.crate
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
Summary:        Private implementation detail of rusqlite crate
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
%files -n rust-rusqlite-macros-devel -f %{oreon_filedir}/rust-rusqlite-macros-devel.list

%changelog

%autochangelog
