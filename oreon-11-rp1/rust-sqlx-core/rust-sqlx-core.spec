%global source0_hash ee6798b1838b6a0f69c007c133b8df5866302197e404e8b6ee8ed3e3a5e68dc6
%bcond check 0
%global debug_package %{nil}
%global crate sqlx-core
Name:           rust-sqlx-core
Version:        0.8.6
Release:        1%{?dist}
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-core
Source0:        https://static.crates.io/crates/sqlx-core/sqlx-core-%{version}.crate
Patch:          sqlx-core-fix-metadata.diff
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
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_rt-async-std-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+_rt-async-std-devel

This package contains library source intended for building other packages which
use the "_rt-async-std" feature of the "%{crate}" crate.

%package     -n %{name}+_rt-tokio-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+_rt-tokio-devel

This package contains library source intended for building other packages which
use the "_rt-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-native-tls-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+_tls-native-tls-devel

This package contains library source intended for building other packages which
use the "_tls-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-none-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+_tls-none-devel

This package contains library source intended for building other packages which
use the "_tls-none" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-rustls-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+_tls-rustls-devel

This package contains library source intended for building other packages which
use the "_tls-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-rustls-ring-native-roots-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+_tls-rustls-ring-native-roots-devel

This package contains library source intended for building other packages which
use the "_tls-rustls-ring-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-rustls-ring-webpki-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+_tls-rustls-ring-webpki-devel

This package contains library source intended for building other packages which
use the "_tls-rustls-ring-webpki" feature of the "%{crate}" crate.

%package     -n %{name}+any-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+any-devel

This package contains library source intended for building other packages which
use the "any" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+bit-vec-devel

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%package     -n %{name}+bstr-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+bstr-devel

This package contains library source intended for building other packages which
use the "bstr" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+crc-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+crc-devel

This package contains library source intended for building other packages which
use the "crc" feature of the "%{crate}" crate.

%package     -n %{name}+ipnet-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+ipnet-devel

This package contains library source intended for building other packages which
use the "ipnet" feature of the "%{crate}" crate.

%package     -n %{name}+ipnetwork-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+ipnetwork-devel

This package contains library source intended for building other packages which
use the "ipnetwork" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+mac_address-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+mac_address-devel

This package contains library source intended for building other packages which
use the "mac_address" feature of the "%{crate}" crate.

%package     -n %{name}+migrate-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+migrate-devel

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+offline-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+offline-devel

This package contains library source intended for building other packages which
use the "offline" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-stream-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+tokio-stream-devel

This package contains library source intended for building other packages which
use the "tokio-stream" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Core of SQLx, the rust SQL toolkit. Not intended to be used directly
BuildArch:      noarch
%description -n %{name}+webpki-roots-devel

This package contains library source intended for building other packages which
use the "webpki-roots" feature of the "%{crate}" crate.

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
%files -n rust-sqlx-core-devel -f %{oreon_filedir}/rust-sqlx-core-devel.list

%changelog

%autochangelog
