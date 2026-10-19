%global source0_hash 1b7e40a16222e557795012311211f161390babaf7fe6bb945748b6456a6aaf39
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_sync
Name:           rust-uu_sync
Version:        0.12.0
Release:        1%{?dist}
Summary:        sync ~ (uutils) synchronize cache writes to storage
License:        MIT
URL:            https://crates.io/crates/uu_sync
Source0:        https://static.crates.io/crates/uu_sync/uu_sync-%{version}.crate
Patch:          uu_sync-fix-metadata-auto.diff
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
Summary:        sync ~ (uutils) synchronize cache writes to storage
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
%files -n rust-uu_sync-devel -f %{oreon_filedir}/rust-uu_sync-devel.list

%changelog

%autochangelog
