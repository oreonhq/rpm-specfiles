%global source0_hash 2cd66269887534af4b0c3e3337404591daa8dc8b9b2b3db71f9523beb4bafb41
%bcond check 0
%global debug_package %{nil}
%global crate fn-error-context
Name:           rust-fn-error-context
Version:        0.2.1
Release:        1%{?dist}
Summary:        An attribute macro to add context to errors from a function.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fn-error-context
Source0:        https://static.crates.io/crates/fn-error-context/fn-error-context-%{version}.crate
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
Summary:        An attribute macro to add context to errors from a function.
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
%files -n rust-fn-error-context-devel -f %{oreon_filedir}/rust-fn-error-context-devel.list

%changelog

%autochangelog
