%global source0_hash 746873a384ad60adc5db74471dfaba74bd278afbdcfd81db93fafcdfc8b5ca0c
%bcond check 0
%global debug_package %{nil}
%global crate maybe-async
Name:           rust-maybe-async
Version:        0.2.11
Release:        1%{?dist}
Summary:        A procedure macro to unify SYNC and ASYNC implementation
License:        MIT
URL:            https://crates.io/crates/maybe-async
Source0:        https://static.crates.io/crates/maybe-async/maybe-async-%{version}.crate
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
Summary:        A procedure macro to unify SYNC and ASYNC implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+is_sync-devel
Summary:        A procedure macro to unify SYNC and ASYNC implementation
BuildArch:      noarch
%description -n %{name}+is_sync-devel

This package contains library source intended for building other packages which
use the "is_sync" feature of the "%{crate}" crate.

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
%files -n rust-maybe-async-devel -f %{oreon_filedir}/rust-maybe-async-devel.list

%changelog

%autochangelog
