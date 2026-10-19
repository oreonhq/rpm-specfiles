%global source0_hash fe96480bed92df2b442a1a30df364e12d08eed03aeb061f2b8dc6afb2be91119
%bcond check 0
%global debug_package %{nil}
%global crate zbus_macros
Name:           rust-zbus_macros
Version:        5.18.0
Release:        1%{?dist}
Summary:        proc-macros for zbus
License:        MIT
URL:            https://crates.io/crates/zbus_macros
Source0:        https://static.crates.io/crates/zbus_macros/zbus_macros-%{version}.crate
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
Summary:        proc-macros for zbus
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-api-devel
Summary:        proc-macros for zbus
BuildArch:      noarch
%description -n %{name}+blocking-api-devel

This package contains library source intended for building other packages which
use the "blocking-api" feature of the "%{crate}" crate.

%package     -n %{name}+gvariant-devel
Summary:        proc-macros for zbus
BuildArch:      noarch
%description -n %{name}+gvariant-devel

This package contains library source intended for building other packages which
use the "gvariant" feature of the "%{crate}" crate.

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
%files -n rust-zbus_macros-devel -f %{oreon_filedir}/rust-zbus_macros-devel.list

%changelog

%autochangelog
