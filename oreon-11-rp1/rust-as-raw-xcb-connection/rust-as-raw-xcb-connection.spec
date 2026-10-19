%global source0_hash 175571dd1d178ced59193a6fc02dde1b972eb0bc56c892cde9beeceac5bf0f6b
%bcond check 0
%global debug_package %{nil}
%global crate as-raw-xcb-connection
Name:           rust-as-raw-xcb-connection
Version:        1.0.1
Release:        1%{?dist}
Summary:        Trait to facilitate interoperatibility with libxcb C API
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/as-raw-xcb-connection
Source0:        https://static.crates.io/crates/as-raw-xcb-connection/as-raw-xcb-connection-%{version}.crate
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
Summary:        Trait to facilitate interoperatibility with libxcb C API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Trait to facilitate interoperatibility with libxcb C API
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

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
%files -n rust-as-raw-xcb-connection-devel -f %{oreon_filedir}/rust-as-raw-xcb-connection-devel.list

%changelog

%autochangelog
