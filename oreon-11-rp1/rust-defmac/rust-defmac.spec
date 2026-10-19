%global source0_hash d5592fca31e96d8a748d03080b58be78c5383617aa4bd89e69f30607d8769891
%bcond check 0
%global debug_package %{nil}
%global crate defmac
Name:           rust-defmac
Version:        0.2.1
Release:        1%{?dist}
Summary:        Macro to define lambda-like macros inline
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/defmac
Source0:        https://static.crates.io/crates/defmac/defmac-%{version}.crate
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
Summary:        Macro to define lambda-like macros inline
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
%files -n rust-defmac-devel -f %{oreon_filedir}/rust-defmac-devel.list

%changelog

%autochangelog
