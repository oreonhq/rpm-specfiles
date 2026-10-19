%global source0_hash 2e99fb7a497b1e3339bc746195567ed8d3e24945ecd636e3619d20b9de9e9149
%bcond check 0
%global debug_package %{nil}
%global crate libsqlite3-sys
Name:           rust-libsqlite3-sys
Version:        0.30.1
Release:        2%{?dist}
Summary:        Native bindings to the libsqlite3 library
License:        MIT
URL:            https://crates.io/crates/libsqlite3-sys
Source0:        https://static.crates.io/crates/libsqlite3-sys/libsqlite3-sys-%{version}.crate
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
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+buildtime_bindgen-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+buildtime_bindgen-devel

This package contains library source intended for building other packages which
use the "buildtime_bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+bundled-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+bundled-devel

This package contains library source intended for building other packages which
use the "bundled" feature of the "%{crate}" crate.

%package     -n %{name}+bundled-sqlcipher-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+bundled-sqlcipher-devel

This package contains library source intended for building other packages which
use the "bundled-sqlcipher" feature of the "%{crate}" crate.

%package     -n %{name}+bundled-sqlcipher-vendored-openssl-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+bundled-sqlcipher-vendored-openssl-devel

This package contains library source intended for building other packages which
use the "bundled-sqlcipher-vendored-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+bundled-windows-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+bundled-windows-devel

This package contains library source intended for building other packages which
use the "bundled-windows" feature of the "%{crate}" crate.

%package     -n %{name}+bundled_bindings-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+bundled_bindings-devel

This package contains library source intended for building other packages which
use the "bundled_bindings" feature of the "%{crate}" crate.

%package     -n %{name}+in_gecko-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+in_gecko-devel

This package contains library source intended for building other packages which
use the "in_gecko" feature of the "%{crate}" crate.

%package     -n %{name}+loadable_extension-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+loadable_extension-devel

This package contains library source intended for building other packages which
use the "loadable_extension" feature of the "%{crate}" crate.

%package     -n %{name}+min_sqlite_version_3_14_0-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+min_sqlite_version_3_14_0-devel

This package contains library source intended for building other packages which
use the "min_sqlite_version_3_14_0" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-sys-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+openssl-sys-devel

This package contains library source intended for building other packages which
use the "openssl-sys" feature of the "%{crate}" crate.

%package     -n %{name}+preupdate_hook-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+preupdate_hook-devel

This package contains library source intended for building other packages which
use the "preupdate_hook" feature of the "%{crate}" crate.

%package     -n %{name}+session-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+session-devel

This package contains library source intended for building other packages which
use the "session" feature of the "%{crate}" crate.

%package     -n %{name}+sqlcipher-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+sqlcipher-devel

This package contains library source intended for building other packages which
use the "sqlcipher" feature of the "%{crate}" crate.

%package     -n %{name}+unlock_notify-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+unlock_notify-devel

This package contains library source intended for building other packages which
use the "unlock_notify" feature of the "%{crate}" crate.

%package     -n %{name}+wasm32-wasi-vfs-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+wasm32-wasi-vfs-devel

This package contains library source intended for building other packages which
use the "wasm32-wasi-vfs" feature of the "%{crate}" crate.

%package     -n %{name}+with-asan-devel
Summary:        Native bindings to the libsqlite3 library
BuildArch:      noarch
%description -n %{name}+with-asan-devel

This package contains library source intended for building other packages which
use the "with-asan" feature of the "%{crate}" crate.

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
%files -n rust-libsqlite3-sys-devel -f %{oreon_filedir}/rust-libsqlite3-sys-devel.list

%changelog

%autochangelog
