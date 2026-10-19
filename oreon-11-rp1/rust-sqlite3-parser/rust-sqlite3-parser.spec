%global source0_hash 05c85cc446125980d1b1f173f04199401506307fff106039b8a7b326b6cf749f
%bcond check 0
%global debug_package %{nil}
%global crate sqlite3-parser
Name:           rust-sqlite3-parser
Version:        0.16.0
Release:        1%{?dist}
Summary:        SQL parser (as understood by SQLite)
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sqlite3-parser
Source0:        https://static.crates.io/crates/sqlite3-parser/sqlite3-parser-%{version}.crate
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
Summary:        SQL parser (as understood by SQLite)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+NDEBUG-devel
Summary:        SQL parser (as understood by SQLite)
BuildArch:      noarch
%description -n %{name}+NDEBUG-devel

This package contains library source intended for building other packages which
use the "NDEBUG" feature of the "%{crate}" crate.

%package     -n %{name}+SQLITE_ENABLE_ORDERED_SET_AGGREGATES-devel
Summary:        SQL parser (as understood by SQLite)
BuildArch:      noarch
%description -n %{name}+SQLITE_ENABLE_ORDERED_SET_AGGREGATES-devel

This package contains library source intended for building other packages which
use the "SQLITE_ENABLE_ORDERED_SET_AGGREGATES" feature of the "%{crate}" crate.

%package     -n %{name}+YYCOVERAGE-devel
Summary:        SQL parser (as understood by SQLite)
BuildArch:      noarch
%description -n %{name}+YYCOVERAGE-devel

This package contains library source intended for building other packages which
use the "YYCOVERAGE" feature of the "%{crate}" crate.

%package     -n %{name}+YYNOERRORRECOVERY-devel
Summary:        SQL parser (as understood by SQLite)
BuildArch:      noarch
%description -n %{name}+YYNOERRORRECOVERY-devel

This package contains library source intended for building other packages which
use the "YYNOERRORRECOVERY" feature of the "%{crate}" crate.

%package     -n %{name}+YYTRACKMAXSTACKDEPTH-devel
Summary:        SQL parser (as understood by SQLite)
BuildArch:      noarch
%description -n %{name}+YYTRACKMAXSTACKDEPTH-devel

This package contains library source intended for building other packages which
use the "YYTRACKMAXSTACKDEPTH" feature of the "%{crate}" crate.

%package     -n %{name}+extra_checks-devel
Summary:        SQL parser (as understood by SQLite)
BuildArch:      noarch
%description -n %{name}+extra_checks-devel

This package contains library source intended for building other packages which
use the "extra_checks" feature of the "%{crate}" crate.

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
%files -n rust-sqlite3-parser-devel -f %{oreon_filedir}/rust-sqlite3-parser-devel.list

%changelog

%autochangelog
