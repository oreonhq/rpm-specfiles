%global source0_hash 082e6cfc1b3983196dcde93ee98fdd2378892d6dea96fe8ce21c470346491ef7
%bcond check 1
%global debug_package %{nil}
%global crate below-dump
%global unsupported_arches %{ix86}
Name:           rust-below-dump
Version:        0.9.0
Release:        1%{?dist}
Summary:        Dump crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-dump
Source0:        https://static.crates.io/crates/below-dump/below-dump-%{version}.crate
Patch:          below-dump-fix-metadata.diff
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
Summary:        Dump crate for below
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifnarch %{unsupported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifnarch %{unsupported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-below-dump-devel -f %{oreon_filedir}/rust-below-dump-devel.list

%changelog

%autochangelog
