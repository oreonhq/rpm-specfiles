%global source0_hash 96d9ea5ee7dc59a2244fa486d8f00472f8d3e4c8c5f7f24a8551559ef3f3530e
%bcond check 1
%global debug_package %{nil}
%global crate gettid
Name:           rust-gettid
Version:        0.1.4
Release:        1%{?dist}
Summary:        Helper to get an integer ID for the current thread
License:        0BSD
URL:            https://crates.io/crates/gettid
Source0:        https://static.crates.io/crates/gettid/gettid-%{version}.crate
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
Summary:        Helper to get an integer ID for the current thread
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
%files -n rust-gettid-devel -f %{oreon_filedir}/rust-gettid-devel.list

%changelog

%autochangelog
