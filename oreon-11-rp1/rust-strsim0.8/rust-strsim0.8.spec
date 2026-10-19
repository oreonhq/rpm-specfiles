%global source0_hash 8ea5119cdb4c55b55d432abb513a0429384878c15dde60cc77b1c99de1a95a6a
%bcond check 0
%global debug_package %{nil}
%global crate strsim
Name:           rust-strsim0.8
Version:        0.8.0
Release:        1%{?dist}
Summary:        Implementations of string similarity metrics.
License:        MIT
URL:            https://crates.io/crates/strsim
Source0:        https://static.crates.io/crates/strsim/strsim-%{version}.crate
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
Summary:        Implementations of string similarity metrics.
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
%files -n rust-strsim0.8-devel -f %{oreon_filedir}/rust-strsim0.8-devel.list

%changelog

%autochangelog
