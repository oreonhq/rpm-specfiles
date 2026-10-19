%global source0_hash 3640c1c38b8e4e43584d8df18be5fc6b0aa314ce6ebf51b53313d4306cca8e46
%bcond check 0
%global debug_package %{nil}
%global crate is-terminal
Name:           rust-is-terminal
Version:        0.4.17
Release:        1%{?dist}
Summary:        Test whether a given stream is a terminal
License:        MIT
URL:            https://crates.io/crates/is-terminal
Source0:        https://static.crates.io/crates/is-terminal/is-terminal-%{version}.crate
Patch:          is-terminal-fix-metadata-auto.diff
Patch:          is-terminal-fix-metadata.diff
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
Summary:        Test whether a given stream is a terminal
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

%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-is-terminal-devel -f %{oreon_filedir}/rust-is-terminal-devel.list

%changelog

%autochangelog
