%global source0_hash 0bf256ce5efdfa370213c1dabab5935a12e49f2c58d15e9eac2870d3b4f27263
%bcond check 0
%global debug_package %{nil}
%global crate sync_wrapper
Name:           rust-sync_wrapper
Version:        1.0.2
Release:        1%{?dist}
Summary:        A tool for enlisting the compiler's help in proving the absence of co...
License:        Apache-2.0
URL:            https://crates.io/crates/sync_wrapper
Source0:        https://static.crates.io/crates/sync_wrapper/sync_wrapper-%{version}.crate
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

%package     -n %{name}+futures-devel
Summary:        A tool for enlisting the compiler's help in proving the absence of co...
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        A tool for enlisting the compiler's help in proving the absence of co...
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

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
%files -n rust-sync_wrapper-devel -f %{oreon_filedir}/rust-sync_wrapper-devel.list

%changelog

%autochangelog
