%global source0_hash 6f11ff5c25c172608d5b85e2fb43ee9a6d683a7f4ab7f96ae07b3d8b590368fd
%bcond check 1
%global debug_package %{nil}
%global crate termsize
Name:           rust-termsize
Version:        0.1.9
Release:        1%{?dist}
Summary:        Retrieves terminal size
License:        MIT
URL:            https://crates.io/crates/termsize
Source0:        https://static.crates.io/crates/termsize/termsize-%{version}.crate
Patch:          termsize-fix-metadata-auto.diff
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
Summary:        Retrieves terminal size
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
%files -n rust-termsize-devel -f %{oreon_filedir}/rust-termsize-devel.list

%changelog

%autochangelog
