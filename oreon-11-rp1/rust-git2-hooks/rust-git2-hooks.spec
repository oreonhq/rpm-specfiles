%global source0_hash 9e21a2c5eee3085f2b622805d4f4c878d9519bf70fa76bed0923b82a25f24199
%bcond check 0
%global debug_package %{nil}
%global crate git2-hooks
Name:           rust-git2-hooks
Version:        0.7.0
Release:        1%{?dist}
Summary:        Adds git hooks support based on git2-rs
License:        MIT
URL:            https://crates.io/crates/git2-hooks
Source0:        https://static.crates.io/crates/git2-hooks/git2-hooks-%{version}.crate
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
Summary:        Adds git hooks support based on git2-rs
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
%files -n rust-git2-hooks-devel -f %{oreon_filedir}/rust-git2-hooks-devel.list

%changelog

%autochangelog
