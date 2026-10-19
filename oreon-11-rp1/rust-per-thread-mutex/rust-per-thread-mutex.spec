%global source0_hash b20d1aaa7fcf3cd5a7b4506c38594d25e122ad45dec6da7f85bac52f3a3e562c
%bcond check 1
%global debug_package %{nil}
%global crate per-thread-mutex
Name:           rust-per-thread-mutex
Version:        0.1.4
Release:        1%{?dist}
Summary:        Synchronization lock designed for wrapping thread-unsafe C libraries
License:        MPL-2.0
URL:            https://crates.io/crates/per-thread-mutex
Source0:        https://static.crates.io/crates/per-thread-mutex/per-thread-mutex-%{version}.crate
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
Summary:        Synchronization lock designed for wrapping thread-unsafe C libraries
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
%files -n rust-per-thread-mutex-devel -f %{oreon_filedir}/rust-per-thread-mutex-devel.list

%changelog

%autochangelog
