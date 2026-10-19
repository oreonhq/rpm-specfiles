%global source0_hash 35e1d0bd9c575c52e59aad8e122a11786e852a154678d0c86e9e243d55273970
%bcond check 0
%global debug_package %{nil}
%global crate imperative
Name:           rust-imperative
Version:        1.0.7
Release:        1%{?dist}
Summary:        Check for imperative mood in text
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/imperative
Source0:        https://static.crates.io/crates/imperative/imperative-%{version}.crate
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
Summary:        Check for imperative mood in text
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
%files -n rust-imperative-devel -f %{oreon_filedir}/rust-imperative-devel.list

%changelog

%autochangelog
