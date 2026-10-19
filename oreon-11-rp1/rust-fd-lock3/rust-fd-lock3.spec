%global source0_hash ef033ed5e9bad94e55838ca0ca906db0e043f517adda0c8b79c7a8c66c93c1b5
%bcond check 0
%global debug_package %{nil}
%global crate fd-lock
Name:           rust-fd-lock3
Version:        3.0.13
Release:        1%{?dist}
Summary:        Advisory cross-platform lock on a file using a file descriptor to it
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fd-lock
Source0:        https://static.crates.io/crates/fd-lock/fd-lock-%{version}.crate
Patch:          fd-lock-fix-metadata-auto.diff
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
Summary:        Advisory cross-platform lock on a file using a file descriptor to it
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
%files -n rust-fd-lock3-devel -f %{oreon_filedir}/rust-fd-lock3-devel.list

%changelog

%autochangelog
