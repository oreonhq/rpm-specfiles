%global source0_hash f20d7c40e6d6fc2ff69ad8e8bac4d39a5fc1874402647ac92b620954d56d5c3e
%bcond check 0
%global debug_package %{nil}
%global crate run_script
Name:           rust-run_script
Version:        0.11.0
Release:        1%{?dist}
Summary:        Run shell scripts in rust
License:        Apache-2.0
URL:            https://crates.io/crates/run_script
Source0:        https://static.crates.io/crates/run_script/run_script-%{version}.crate
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
Summary:        Run shell scripts in rust
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
%files -n rust-run_script-devel -f %{oreon_filedir}/rust-run_script-devel.list

%changelog

%autochangelog
