%global source0_hash d16e986e12a0b63c17fe7df3569ed524da77d258a900863034571fd08f7553ac
%bcond check 1
%global debug_package %{nil}
%global crate fb_procfs
Name:           rust-fb_procfs0.7
Version:        0.7.1
Release:        1%{?dist}
Summary:        For reading procfs
License:        Apache-2.0
URL:            https://crates.io/crates/fb_procfs
Source0:        https://static.crates.io/crates/fb_procfs/fb_procfs-%{version}.crate
Patch:          fb_procfs-fix-metadata.diff
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
Summary:        For reading procfs
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
%files -n rust-fb_procfs0.7-devel -f %{oreon_filedir}/rust-fb_procfs0.7-devel.list

%changelog

%autochangelog
