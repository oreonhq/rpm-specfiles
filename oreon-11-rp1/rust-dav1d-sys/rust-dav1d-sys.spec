%global source0_hash c3c91aea6668645415331133ed6f8ddf0e7f40160cd97a12d59e68716a58704b
%bcond check 0
%global debug_package %{nil}
%global crate dav1d-sys
Name:           rust-dav1d-sys
Version:        0.8.3
Release:        1%{?dist}
Summary:        FFI bindings to dav1d
License:        MIT
URL:            https://crates.io/crates/dav1d-sys
Source0:        https://static.crates.io/crates/dav1d-sys/dav1d-sys-%{version}.crate
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
Summary:        FFI bindings to dav1d
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
%files -n rust-dav1d-sys-devel -f %{oreon_filedir}/rust-dav1d-sys-devel.list

%changelog

%autochangelog
