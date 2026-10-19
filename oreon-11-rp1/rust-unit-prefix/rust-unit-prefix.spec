%global source0_hash 81e544489bf3d8ef66c953931f56617f423cd4b5494be343d9b9d3dda037b9a3
%bcond check 1
%global debug_package %{nil}
%global crate unit-prefix
Name:           rust-unit-prefix
Version:        0.5.2
Release:        1%{?dist}
Summary:        Format numbers with metric and binary unit prefixes
License:        MIT
URL:            https://crates.io/crates/unit-prefix
Source0:        https://static.crates.io/crates/unit-prefix/unit-prefix-%{version}.crate
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
Summary:        Format numbers with metric and binary unit prefixes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Format numbers with metric and binary unit prefixes
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-unit-prefix-devel -f %{oreon_filedir}/rust-unit-prefix-devel.list

%changelog

%autochangelog
