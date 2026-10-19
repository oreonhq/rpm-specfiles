%global source0_hash aa18ce2bc66555b3218614519ac839ddb759a7d6720732f979ef8d13be147ecd
%bcond check 1
%global debug_package %{nil}
%global crate enum_dispatch
Name:           rust-enum_dispatch
Version:        0.3.13
Release:        1%{?dist}
Summary:        Near drop-in replacement for dynamic-dispatched method calls
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/enum_dispatch
Source0:        https://static.crates.io/crates/enum_dispatch/enum_dispatch-%{version}.crate
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
Summary:        Near drop-in replacement for dynamic-dispatched method calls
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
%files -n rust-enum_dispatch-devel -f %{oreon_filedir}/rust-enum_dispatch-devel.list

%changelog

%autochangelog
