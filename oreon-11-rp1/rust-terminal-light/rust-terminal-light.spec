%global source0_hash a6f76be906d875a0ce764c52a055858c24847cb7dc674d3a5ad8cf7e3dd4ee9f
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate terminal-light
Name:           rust-terminal-light
Version:        1.8.0
Release:        1%{?dist}
Summary:        Tells you whether your terminal is dark or light
License:        MIT
URL:            https://crates.io/crates/terminal-light
Source0:        https://static.crates.io/crates/terminal-light/terminal-light-%{version}.crate
Patch:          terminal-light-fix-metadata.diff
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
Summary:        Tells you whether your terminal is dark or light
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
%files -n rust-terminal-light-devel -f %{oreon_filedir}/rust-terminal-light-devel.list

%changelog

%autochangelog
