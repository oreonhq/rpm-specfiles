%global source0_hash ed7dc68daa7498a43e4d68e0eb078427e10c38fbcfbb1e42d955f1fa2140d814
%bcond check 0
%global debug_package %{nil}
%global crate ratatui-macros
Name:           rust-ratatui-macros
Version:        0.7.2
Release:        1%{?dist}
Summary:        Macros for Ratatui
License:        MIT
URL:            https://crates.io/crates/ratatui-macros
Source0:        https://static.crates.io/crates/ratatui-macros/ratatui-macros-%{version}.crate
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
Summary:        Macros for Ratatui
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
%files -n rust-ratatui-macros-devel -f %{oreon_filedir}/rust-ratatui-macros-devel.list

%changelog

%autochangelog
