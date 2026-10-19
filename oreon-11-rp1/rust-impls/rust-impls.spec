%global source0_hash 7a46645bbd70538861a90d0f26c31537cdf1e44aae99a794fb75a664b70951bc
%bcond check 0
%global debug_package %{nil}
%global crate impls
Name:           rust-impls
Version:        1.0.3
Release:        1%{?dist}
Summary:        Determine if a type implements a logical trait expression
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/impls
Source0:        https://static.crates.io/crates/impls/impls-%{version}.crate
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
Summary:        Determine if a type implements a logical trait expression
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
%files -n rust-impls-devel -f %{oreon_filedir}/rust-impls-devel.list

%changelog

%autochangelog
