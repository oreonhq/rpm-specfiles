%global source0_hash ade8366b8bd5ba243f0a58f036cc0ca8a2f069cff1a2351ef1cac6b083e16fc0
%bcond check 0
%global debug_package %{nil}
%global crate cached_proc_macro_types
Name:           rust-cached_proc_macro_types
Version:        0.1.1
Release:        1%{?dist}
Summary:        Generic cache implementations and simplified function memoization
License:        MIT
URL:            https://crates.io/crates/cached_proc_macro_types
Source0:        https://static.crates.io/crates/cached_proc_macro_types/cached_proc_macro_types-%{version}.crate
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
Summary:        Generic cache implementations and simplified function memoization
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
%files -n rust-cached_proc_macro_types-devel -f %{oreon_filedir}/rust-cached_proc_macro_types-devel.list

%changelog

%autochangelog
