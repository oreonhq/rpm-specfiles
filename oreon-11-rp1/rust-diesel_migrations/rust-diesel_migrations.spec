%global source0_hash 28d0f4a98124ba6d4ca75da535f65984badec16a003b6e2f94a01e31a79490b8
%bcond check 1
%global debug_package %{nil}
%global crate diesel_migrations
Name:           rust-diesel_migrations
Version:        2.3.2
Release:        1%{?dist}
Summary:        Migration management for diesel
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/diesel_migrations
Source0:        https://static.crates.io/crates/diesel_migrations/diesel_migrations-%{version}.crate
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
Summary:        Migration management for diesel
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+mysql-devel
Summary:        Migration management for diesel
BuildArch:      noarch
%description -n %{name}+mysql-devel

This package contains library source intended for building other packages which
use the "mysql" feature of the "%{crate}" crate.

%package     -n %{name}+postgres-devel
Summary:        Migration management for diesel
BuildArch:      noarch
%description -n %{name}+postgres-devel

This package contains library source intended for building other packages which
use the "postgres" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        Migration management for diesel
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

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
%files -n rust-diesel_migrations-devel -f %{oreon_filedir}/rust-diesel_migrations-devel.list

%changelog

%autochangelog
