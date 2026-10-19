%global source0_hash cf4363accdf6ef7ba861871d2d521ab7418a04aaaed919fadb022af71d379b12
%bcond check 0
%global debug_package %{nil}
%global crate gix-command
Name:           rust-gix-command0.9
Version:        0.9.2
Release:        1%{?dist}
Summary:        A crate of the gitoxide project handling internal git command execution
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-command
Source0:        https://static.crates.io/crates/gix-command/gix-command-%{version}.crate
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
Summary:        A crate of the gitoxide project handling internal git command execution
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
%files -n rust-gix-command0.9-devel -f %{oreon_filedir}/rust-gix-command0.9-devel.list

%changelog

%autochangelog
