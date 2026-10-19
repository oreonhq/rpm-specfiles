%global source0_hash c2d12fe70b2c1b4401038055f90f151b78208de1f9f89a7dbfd41587a10c3eea
%bcond check 0
%global debug_package %{nil}
%global crate sqlx-sqlite
Name:           rust-sqlx-sqlite
Version:        0.8.6
Release:        1%{?dist}
Summary:        SQLite driver implementation for SQLx
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-sqlite
Source0:        https://static.crates.io/crates/sqlx-sqlite/sqlx-sqlite-%{version}.crate
Patch:          sqlx-sqlite-fix-metadata.diff
Patch2:         rust-sqlx-sqlite-0.8.6-Gate_deserealize.patch
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
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+any-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+any-devel

This package contains library source intended for building other packages which
use the "any" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+migrate-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+migrate-devel

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%package     -n %{name}+offline-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+offline-devel

This package contains library source intended for building other packages which
use the "offline" feature of the "%{crate}" crate.

%package     -n %{name}+preupdate-hook-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+preupdate-hook-devel

This package contains library source intended for building other packages which
use the "preupdate-hook" feature of the "%{crate}" crate.

%package     -n %{name}+regexp-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+regexp-devel

This package contains library source intended for building other packages which
use the "regexp" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+unbundled-devel
Summary:        SQLite driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+unbundled-devel

This package contains library source intended for building other packages which
use the "unbundled" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        SQLite driver implementation for SQLx
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

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-sqlx-sqlite-devel -f %{oreon_filedir}/rust-sqlx-sqlite-devel.list

%changelog

%autochangelog
