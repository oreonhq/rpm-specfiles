%global source0_hash 2b8c4a4445d81357df8b1a650d0d0d6fbbbfe99d064aa5e02f3e4022061476d8
%bcond check 0
%global debug_package %{nil}
%global crate state
Name:           rust-state
Version:        0.6.0
Release:        1%{?dist}
Summary:        A library for safe and effortless global and thread-local state manag...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/state
Source0:        https://static.crates.io/crates/state/state-%{version}.crate
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

%package     -n %{name}+tls-devel
Summary:        A library for safe and effortless global and thread-local state manag...
BuildArch:      noarch
%description -n %{name}+tls-devel

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

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
%files -n rust-state-devel -f %{oreon_filedir}/rust-state-devel.list

%changelog

%autochangelog
