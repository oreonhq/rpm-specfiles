%global source0_hash 2afbb9b0aef60e4f0d2b18129b6c0dff035a6f7dbbd17c2f38c1432102ee223c
%bcond check 0
%global debug_package %{nil}
%global crate easy-parallel
Name:           rust-easy-parallel
Version:        3.3.1
Release:        1%{?dist}
Summary:        Run closures in parallel
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/easy-parallel
Source0:        https://static.crates.io/crates/easy-parallel/easy-parallel-%{version}.crate
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
Summary:        Run closures in parallel
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
%files -n rust-easy-parallel-devel -f %{oreon_filedir}/rust-easy-parallel-devel.list

%changelog

%autochangelog
