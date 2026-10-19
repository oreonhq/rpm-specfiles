%global source0_hash 8807c397789cbe02bbdb1a27ea5f345584132808697b2a3f957c829829ee4814
%bcond check 1
%global debug_package %{nil}
%global crate confy
Name:           rust-confy
Version:        2.0.0
Release:        1%{?dist}
Summary:        Boilerplate-free configuration management
License:        MIT OR X11 OR Apache-2.0
URL:            https://crates.io/crates/confy
Source0:        https://static.crates.io/crates/confy/confy-%{version}.crate
Patch:          confy-fix-metadata.diff
Patch:          0001-fix-compilation-error-in-doctests.patch
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
Summary:        Boilerplate-free configuration management
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
%files -n rust-confy-devel -f %{oreon_filedir}/rust-confy-devel.list

%changelog

%autochangelog
