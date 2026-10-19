%global source0_hash fb2d1b8f4548dbf5e1f7818512e9c406860678f29c300cdf0ebac72d1a3a1671
%bcond check 0
%global debug_package %{nil}
%global crate tokio-executor
Name:           rust-tokio-executor
Version:        0.1.10
Release:        1%{?dist}
Summary:        Future execution primitives
License:        MIT
URL:            https://crates.io/crates/tokio-executor
Source0:        https://static.crates.io/crates/tokio-executor/tokio-executor-%{version}.crate
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
Summary:        Future execution primitives
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
%files -n rust-tokio-executor-devel -f %{oreon_filedir}/rust-tokio-executor-devel.list

%changelog

%autochangelog
