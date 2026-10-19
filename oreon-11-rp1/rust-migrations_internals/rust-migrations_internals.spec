%global source0_hash 36c791ecdf977c99f45f23280405d7723727470f6689a5e6dbf513ac547ae10d
%bcond check 1
%global debug_package %{nil}
%global crate migrations_internals
Name:           rust-migrations_internals
Version:        2.3.0
Release:        1%{?dist}
Summary:        Internal implementation of diesels migration mechanism
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/migrations_internals
Source0:        https://static.crates.io/crates/migrations_internals/migrations_internals-%{version}.crate
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
Summary:        Internal implementation of diesels migration mechanism
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
%files -n rust-migrations_internals-devel -f %{oreon_filedir}/rust-migrations_internals-devel.list

%changelog

%autochangelog
