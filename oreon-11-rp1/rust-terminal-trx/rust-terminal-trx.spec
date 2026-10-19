%global source0_hash 3b3f27d9a8a177e57545481faec87acb45c6e854ed1e5a3658ad186c106f38ed
%bcond check 1
%global debug_package %{nil}
%global crate terminal-trx
Name:           rust-terminal-trx
Version:        0.2.6
Release:        1%{?dist}
Summary:        Handle to the terminal of the current process
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/terminal-trx
Source0:        https://static.crates.io/crates/terminal-trx/terminal-trx-%{version}.crate
Patch:          terminal-trx-fix-metadata-auto.diff
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
Summary:        Handle to the terminal of the current process
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
%files -n rust-terminal-trx-devel -f %{oreon_filedir}/rust-terminal-trx-devel.list

%changelog

%autochangelog
