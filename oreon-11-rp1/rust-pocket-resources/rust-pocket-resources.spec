%global source0_hash c135f38778ad324d9e9ee68690bac2c1a51f340fdf96ca13e2ab3914eb2e51d8
%bcond check 0
%global debug_package %{nil}
%global crate pocket-resources
Name:           rust-pocket-resources
Version:        0.3.2
Release:        1%{?dist}
Summary:        Include resources in your applications.
License:        MIT
URL:            https://crates.io/crates/pocket-resources
Source0:        https://static.crates.io/crates/pocket-resources/pocket-resources-%{version}.crate
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
Summary:        Include resources in your applications.
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
%files -n rust-pocket-resources-devel -f %{oreon_filedir}/rust-pocket-resources-devel.list

%changelog

%autochangelog
