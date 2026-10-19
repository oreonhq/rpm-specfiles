%global source0_hash 09f2bd6146b97ae3359fa0cc6d6b376d9539582c7b4220f041a33ec24c226199
%bcond check 0
%global debug_package %{nil}
%global crate axum-core
Name:           rust-axum-core0.4
Version:        0.4.5
Release:        1%{?dist}
Summary:        Core types and traits for axum
License:        MIT
URL:            https://crates.io/crates/axum-core
Source0:        https://static.crates.io/crates/axum-core/axum-core-%{version}.crate
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

%package     -n %{name}+__private_docs-devel
Summary:        Core types and traits for axum
BuildArch:      noarch
%description -n %{name}+__private_docs-devel

This package contains library source intended for building other packages which
use the "__private_docs" feature of the "%{crate}" crate.

%package     -n %{name}+tower-http-devel
Summary:        Core types and traits for axum
BuildArch:      noarch
%description -n %{name}+tower-http-devel

This package contains library source intended for building other packages which
use the "tower-http" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Core types and traits for axum
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-axum-core0.4-devel -f %{oreon_filedir}/rust-axum-core0.4-devel.list

%changelog

%autochangelog
