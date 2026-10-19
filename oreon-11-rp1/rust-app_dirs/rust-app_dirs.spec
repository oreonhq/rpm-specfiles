%global source0_hash e73a24bad9bd6a94d6395382a6c69fe071708ae4409f763c5475e14ee896313d
%bcond check 0
%global debug_package %{nil}
%global crate app_dirs
Name:           rust-app_dirs
Version:        1.2.1
Release:        1%{?dist}
Summary:        Put your app's data in the right place on every platform
License:        MIT
URL:            https://crates.io/crates/app_dirs
Source0:        https://static.crates.io/crates/app_dirs/app_dirs-%{version}.crate
Patch:          app_dirs-fix-metadata-auto.diff
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
Summary:        Put your app's data in the right place on every platform
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
%files -n rust-app_dirs-devel -f %{oreon_filedir}/rust-app_dirs-devel.list

%changelog

%autochangelog
