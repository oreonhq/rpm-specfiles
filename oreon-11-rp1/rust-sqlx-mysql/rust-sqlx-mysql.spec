%global source0_hash aa003f0038df784eb8fecbbac13affe3da23b45194bd57dba231c8f48199c526
%bcond check 1
%global debug_package %{nil}
%global crate sqlx-mysql
Name:           rust-sqlx-mysql
Version:        0.8.6
Release:        1%{?dist}
Summary:        MySQL driver implementation for SQLx
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-mysql
Source0:        https://static.crates.io/crates/sqlx-mysql/sqlx-mysql-%{version}.crate
Patch:          sqlx-mysql-fix-metadata.diff
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
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+any-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+any-devel

This package contains library source intended for building other packages which
use the "any" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+migrate-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+migrate-devel

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%package     -n %{name}+offline-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+offline-devel

This package contains library source intended for building other packages which
use the "offline" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        MySQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a -- -- --skip options::MySqlConnectOptions
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-sqlx-mysql-devel -f %{oreon_filedir}/rust-sqlx-mysql-devel.list

%changelog

%autochangelog
