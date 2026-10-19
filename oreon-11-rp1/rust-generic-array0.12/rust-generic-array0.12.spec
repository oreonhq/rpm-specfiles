%global source0_hash ffdf9f34f1447443d37393cc6c2b8313aebddcd96906caf34e54c68d8e57d7bd
%bcond check 0
%global debug_package %{nil}
%global crate generic-array
Name:           rust-generic-array0.12
Version:        0.12.4
Release:        1%{?dist}
Summary:        Generic types implementing functionality of arrays
License:        MIT
URL:            https://crates.io/crates/generic-array
Source0:        https://static.crates.io/crates/generic-array/generic-array-%{version}.crate
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
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Generic types implementing functionality of arrays
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-generic-array0.12-devel -f %{oreon_filedir}/rust-generic-array0.12-devel.list

%changelog

%autochangelog
