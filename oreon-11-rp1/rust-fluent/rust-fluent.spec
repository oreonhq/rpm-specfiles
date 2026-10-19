%global source0_hash 8137a6d5a2c50d6b0ebfcb9aaa91a28154e0a70605f112d30cb0cd4a78670477
%bcond check 1
%global debug_package %{nil}
%global crate fluent
Name:           rust-fluent
Version:        0.17.0
Release:        1%{?dist}
Summary:        Localization system designed to support natural language translations
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/fluent
Source0:        https://static.crates.io/crates/fluent/fluent-%{version}.crate
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
Summary:        Localization system designed to support natural language translations
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
%files -n rust-fluent-devel -f %{oreon_filedir}/rust-fluent-devel.list

%changelog

%autochangelog
