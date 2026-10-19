%global source0_hash b838eba278d213a8beaf485bd313fd580ca4505a00d5871caeb1457c55322cae
%bcond check 1
%global debug_package %{nil}
%global crate rusqlite
Name:           rust-rusqlite0.31
Version:        0.31.0
Release:        1%{?dist}
Summary:        Ergonomic wrapper for SQLite
License:        MIT
URL:            https://crates.io/crates/rusqlite
Source0:        https://static.crates.io/crates/rusqlite/rusqlite-%{version}.crate
Patch:          rusqlite-fix-metadata.diff
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
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+array-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+array-devel

This package contains library source intended for building other packages which
use the "array" feature of the "%{crate}" crate.

%package     -n %{name}+backup-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+backup-devel

This package contains library source intended for building other packages which
use the "backup" feature of the "%{crate}" crate.

%package     -n %{name}+blob-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+blob-devel

This package contains library source intended for building other packages which
use the "blob" feature of the "%{crate}" crate.

%package     -n %{name}+buildtime_bindgen-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+buildtime_bindgen-devel

This package contains library source intended for building other packages which
use the "buildtime_bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+collation-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+collation-devel

This package contains library source intended for building other packages which
use the "collation" feature of the "%{crate}" crate.

%package     -n %{name}+column_decltype-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+column_decltype-devel

This package contains library source intended for building other packages which
use the "column_decltype" feature of the "%{crate}" crate.

%package     -n %{name}+csv-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+csv-devel

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%package     -n %{name}+csvtab-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+csvtab-devel

This package contains library source intended for building other packages which
use the "csvtab" feature of the "%{crate}" crate.

%package     -n %{name}+extra_check-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+extra_check-devel

This package contains library source intended for building other packages which
use the "extra_check" feature of the "%{crate}" crate.

%package     -n %{name}+functions-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+functions-devel

This package contains library source intended for building other packages which
use the "functions" feature of the "%{crate}" crate.

%package     -n %{name}+hooks-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+hooks-devel

This package contains library source intended for building other packages which
use the "hooks" feature of the "%{crate}" crate.

%package     -n %{name}+i128_blob-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+i128_blob-devel

This package contains library source intended for building other packages which
use the "i128_blob" feature of the "%{crate}" crate.

%package     -n %{name}+limits-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+limits-devel

This package contains library source intended for building other packages which
use the "limits" feature of the "%{crate}" crate.

%package     -n %{name}+load_extension-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+load_extension-devel

This package contains library source intended for building other packages which
use the "load_extension" feature of the "%{crate}" crate.

%package     -n %{name}+modern-full-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+modern-full-devel

This package contains library source intended for building other packages which
use the "modern-full" feature of the "%{crate}" crate.

%package     -n %{name}+modern_sqlite-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+modern_sqlite-devel

This package contains library source intended for building other packages which
use the "modern_sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+release_memory-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+release_memory-devel

This package contains library source intended for building other packages which
use the "release_memory" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+series-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+series-devel

This package contains library source intended for building other packages which
use the "series" feature of the "%{crate}" crate.

%package     -n %{name}+session-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+session-devel

This package contains library source intended for building other packages which
use the "session" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%package     -n %{name}+unlock_notify-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+unlock_notify-devel

This package contains library source intended for building other packages which
use the "unlock_notify" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+vtab-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+vtab-devel

This package contains library source intended for building other packages which
use the "vtab" feature of the "%{crate}" crate.

%package     -n %{name}+window-devel
Summary:        Ergonomic wrapper for SQLite
BuildArch:      noarch
%description -n %{name}+window-devel

This package contains library source intended for building other packages which
use the "window" feature of the "%{crate}" crate.

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
%files -n rust-rusqlite0.31-devel -f %{oreon_filedir}/rust-rusqlite0.31-devel.list

%changelog

%autochangelog
