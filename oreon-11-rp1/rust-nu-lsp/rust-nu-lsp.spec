%global source0_hash 10c2a3b8d307c003dfb95ac8e05861539858f8c221a6bba7b5a5dd1dc9827b14
%bcond check 1
%global debug_package %{nil}
%global crate nu-lsp
Name:           rust-nu-lsp
Version:        0.99.1
Release:        1%{?dist}
Summary:        Nushell's integrated LSP server
License:        MIT
URL:            https://crates.io/crates/nu-lsp
Source0:        https://static.crates.io/crates/nu-lsp/nu-lsp-%{version}.crate
Patch:          nu-lsp-fix-metadata.diff
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
Summary:        Nushell's integrated LSP server
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
%files -n rust-nu-lsp-devel -f %{oreon_filedir}/rust-nu-lsp-devel.list

%changelog

%autochangelog
