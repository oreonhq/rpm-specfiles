%global source0_hash f7201ee416d124d589a820111ba755930df8b75855321a9a1b87312a0597ec8f
%bcond check 0
%global debug_package %{nil}
%global crate configparser
Name:           rust-configparser2
Version:        2.1.0
Release:        1%{?dist}
Summary:        Simple configuration parsing utility with no dependencies
License:        MIT OR LGPL-3.0-or-later
URL:            https://crates.io/crates/configparser
Source0:        https://static.crates.io/crates/configparser/configparser-%{version}.crate
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
Summary:        Simple configuration parsing utility with no dependencies
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
chmod -x README.md CHANGELOG.md Cargo.toml.orig src/*.rs tests/*.rs
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
%files -n rust-configparser2-devel -f %{oreon_filedir}/rust-configparser2-devel.list

%changelog

%autochangelog
