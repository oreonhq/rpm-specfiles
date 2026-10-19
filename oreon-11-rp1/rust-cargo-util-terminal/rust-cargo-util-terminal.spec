%global source0_hash 82be174c17e22a0366a1a0929e0306e0d53f120d159416b00f35e9708e7b2940
%bcond check 1
%global debug_package %{nil}
%global crate cargo-util-terminal
Name:           rust-cargo-util-terminal
Version:        0.1.2
Release:        1%{?dist}
Summary:        Cargo's terminal rendering
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo-util-terminal
Source0:        https://static.crates.io/crates/cargo-util-terminal/cargo-util-terminal-%{version}.crate
Patch:          cargo-util-terminal-fix-metadata-auto.diff
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
Summary:        Cargo's terminal rendering
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
%files -n rust-cargo-util-terminal-devel -f %{oreon_filedir}/rust-cargo-util-terminal-devel.list

%changelog

%autochangelog
