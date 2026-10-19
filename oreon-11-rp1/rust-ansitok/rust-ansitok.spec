%global source0_hash c0a8acea8c2f1c60f0a92a8cd26bf96ca97db56f10bbcab238bbe0cceba659ee
%bcond check 1
%global debug_package %{nil}
%global crate ansitok
Name:           rust-ansitok
Version:        0.3.0
Release:        1%{?dist}
Summary:        Library for parsing ANSI Escape Codes
License:        MIT
URL:            https://crates.io/crates/ansitok
Source0:        https://static.crates.io/crates/ansitok/ansitok-%{version}.crate
Patch:          ansitok-fix-metadata.diff
Patch10:        ansitok-0.2.0-vte-0.15.patch
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
Summary:        Library for parsing ANSI Escape Codes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for parsing ANSI Escape Codes
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-ansitok-devel -f %{oreon_filedir}/rust-ansitok-devel.list

%changelog

%autochangelog
