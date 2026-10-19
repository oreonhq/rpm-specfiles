%global source0_hash 7490cfa5ec963746568740651ac6781f701c9c5ea257c58e057f3ba8cf69e8da
%bcond check 0
%global debug_package %{nil}
%global crate tracing-attributes
Name:           rust-tracing-attributes
Version:        0.1.31
Release:        1%{?dist}
Summary:        Procedural macro attributes for automatically instrumenting functions.
License:        MIT
URL:            https://crates.io/crates/tracing-attributes
Source0:        https://static.crates.io/crates/tracing-attributes/tracing-attributes-%{version}.crate
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
Summary:        Procedural macro attributes for automatically instrumenting functions.
BuildArch:    noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-await-devel
Summary:        Procedural macro attributes for automatically instrumenting functions.
BuildArch:      noarch
%description -n %{name}+async-await-devel

This package contains library source intended for building other packages which
use the "async-await" feature of the "%{crate}" crate.

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
%files -n rust-tracing-attributes-devel -f %{oreon_filedir}/rust-tracing-attributes-devel.list

%changelog

%autochangelog
