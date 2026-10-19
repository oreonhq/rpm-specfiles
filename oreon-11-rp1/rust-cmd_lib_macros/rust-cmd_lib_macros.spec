%global source0_hash bd39b5c2657c1a0064aa5d73636dac4a217edeeb6c5f8a5f52c123a758462ece
%bcond check 0
%global debug_package %{nil}
%global crate cmd_lib_macros
Name:           rust-cmd_lib_macros
Version:        2.0.1
Release:        1%{?dist}
Summary:        Common rust commandline macros and utils for shell script like tasks
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cmd_lib_macros
Source0:        https://static.crates.io/crates/cmd_lib_macros/cmd_lib_macros-%{version}.crate
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
Summary:        Common rust commandline macros and utils for shell script like tasks
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
%files -n rust-cmd_lib_macros-devel -f %{oreon_filedir}/rust-cmd_lib_macros-devel.list

%changelog

%autochangelog
