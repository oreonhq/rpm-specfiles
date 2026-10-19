%global source0_hash 49eedcbbb31f4e9f46566c543c0fb00b8f87ff9d88ba1a011aa262a5a1a2a505
%bcond check 0
%global debug_package %{nil}
%global crate ivf
Name:           rust-ivf
Version:        0.1.4
Release:        1%{?dist}
Summary:        Simple ivf muxer
License:        BSD-2-Clause
URL:            https://crates.io/crates/ivf
Source0:        https://static.crates.io/crates/ivf/ivf-%{version}.crate
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
Summary:        Simple ivf muxer
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
%files -n rust-ivf-devel -f %{oreon_filedir}/rust-ivf-devel.list

%changelog

%autochangelog
