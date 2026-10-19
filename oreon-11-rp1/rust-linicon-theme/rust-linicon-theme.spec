%global source0_hash a4f8240c33bb08c5d8b8cdea87b683b05e61037aa76ff26bef40672cc6ecbb80
%bcond check 0
%global debug_package %{nil}
%global crate linicon-theme
Name:           rust-linicon-theme
Version:        1.2.0
Release:        1%{?dist}
Summary:        Get the user's current icon the on Linux
License:        MPL-2.0
URL:            https://crates.io/crates/linicon-theme
Source0:        https://static.crates.io/crates/linicon-theme/linicon-theme-%{version}.crate
Patch:          linicon-theme-fix-metadata.diff
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
Summary:        Get the user's current icon the on Linux
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
%files -n rust-linicon-theme-devel -f %{oreon_filedir}/rust-linicon-theme-devel.list

%changelog

%autochangelog
