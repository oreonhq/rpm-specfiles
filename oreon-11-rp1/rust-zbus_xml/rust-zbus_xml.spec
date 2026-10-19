%global source0_hash 589e9a02bfafb9754bb2340a9e3b38f389772684c63d9637e76b1870377bec29
%bcond check 1
%global debug_package %{nil}
%global crate zbus_xml
Name:           rust-zbus_xml
Version:        5.0.2
Release:        1%{?dist}
Summary:        API to handle D-Bus introspection XML
License:        MIT
URL:            https://crates.io/crates/zbus_xml
Source0:        https://static.crates.io/crates/zbus_xml/zbus_xml-%{version}.crate
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
Summary:        API to handle D-Bus introspection XML
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
%files -n rust-zbus_xml-devel -f %{oreon_filedir}/rust-zbus_xml-devel.list

%changelog

%autochangelog
