%global source0_hash 7d6ada348dbc2703cbe7637b2dda05cff84d3da2819c24abcb305dd613e0ba2e
%bcond check 1
%global debug_package %{nil}
%global crate lsp-server
Name:           rust-lsp-server
Version:        0.7.9
Release:        1%{?dist}
Summary:        Generic LSP server scaffold
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lsp-server
Source0:        https://static.crates.io/crates/lsp-server/lsp-server-%{version}.crate
Patch:          lsp-server-fix-metadata.diff
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
Summary:        Generic LSP server scaffold
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
%files -n rust-lsp-server-devel -f %{oreon_filedir}/rust-lsp-server-devel.list

%changelog

%autochangelog
