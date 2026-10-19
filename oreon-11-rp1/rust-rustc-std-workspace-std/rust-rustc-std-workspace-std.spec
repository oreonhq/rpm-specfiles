%global source0_hash aba676a20abe46e5b0f1b0deae474aaaf31407e6c71147159890574599da04ef
%bcond check 0
%global debug_package %{nil}
%global crate rustc-std-workspace-std
Name:           rust-rustc-std-workspace-std
Version:        1.0.1
Release:        1%{?dist}
Summary:        Workaround for rustbuild
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc-std-workspace-std
Source0:        https://static.crates.io/crates/rustc-std-workspace-std/rustc-std-workspace-std-%{version}.crate
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
Summary:        Workaround for rustbuild
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
%files -n rust-rustc-std-workspace-std-devel -f %{oreon_filedir}/rust-rustc-std-workspace-std-devel.list

%changelog

%autochangelog
