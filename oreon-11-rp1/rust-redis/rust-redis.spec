%global source0_hash 2acbc41a996f7652b2ddd9dfd98cc4ff602cfd742ae35382f07f608405ab50ed
%bcond check 1
%global debug_package %{nil}
%global crate redis
Name:           rust-redis
Version:        1.7.0
Release:        1%{?dist}
Summary:        Driver for Rust
License:        BSD-3-Clause AND MIT
URL:            https://crates.io/crates/redis
Source0:        https://static.crates.io/crates/redis/redis-%{version}.crate
Patch:          redis-fix-metadata.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  valkey-compat-redis
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+acl-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+acl-devel

This package contains library source intended for building other packages which
use the "acl" feature of the "%{crate}" crate.

%package     -n %{name}+ahash-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+ahash-devel

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%package     -n %{name}+aio-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+aio-devel

This package contains library source intended for building other packages which
use the "aio" feature of the "%{crate}" crate.

%package     -n %{name}+arc-swap-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+arc-swap-devel

This package contains library source intended for building other packages which
use the "arc-swap" feature of the "%{crate}" crate.

%package     -n %{name}+async-native-tls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+async-native-tls-devel

This package contains library source intended for building other packages which
use the "async-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-comp-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+async-std-comp-devel

This package contains library source intended for building other packages which
use the "async-std-comp" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-native-tls-comp-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+async-std-native-tls-comp-devel

This package contains library source intended for building other packages which
use the "async-std-native-tls-comp" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-tls-comp-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+async-std-tls-comp-devel

This package contains library source intended for building other packages which
use the "async-std-tls-comp" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+cluster-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+cluster-devel

This package contains library source intended for building other packages which
use the "cluster" feature of the "%{crate}" crate.

%package     -n %{name}+cluster-async-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+cluster-async-devel

This package contains library source intended for building other packages which
use the "cluster-async" feature of the "%{crate}" crate.

%package     -n %{name}+connection-manager-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+connection-manager-devel

This package contains library source intended for building other packages which
use the "connection-manager" feature of the "%{crate}" crate.

%package     -n %{name}+crc16-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+crc16-devel

This package contains library source intended for building other packages which
use the "crc16" feature of the "%{crate}" crate.

%package     -n %{name}+disable-client-setinfo-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+disable-client-setinfo-devel

This package contains library source intended for building other packages which
use the "disable-client-setinfo" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+geospatial-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+geospatial-devel

This package contains library source intended for building other packages which
use the "geospatial" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+keep-alive-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+keep-alive-devel

This package contains library source intended for building other packages which
use the "keep-alive" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-lite-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+pin-project-lite-devel

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%package     -n %{name}+r2d2-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+r2d2-devel

This package contains library source intended for building other packages which
use the "r2d2" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-pemfile-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+rustls-pemfile-devel

This package contains library source intended for building other packages which
use the "rustls-pemfile" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-pki-types-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+rustls-pki-types-devel

This package contains library source intended for building other packages which
use the "rustls-pki-types" feature of the "%{crate}" crate.

%package     -n %{name}+script-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+script-devel

This package contains library source intended for building other packages which
use the "script" feature of the "%{crate}" crate.

%package     -n %{name}+sentinel-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+sentinel-devel

This package contains library source intended for building other packages which
use the "sentinel" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sha1_smol-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+sha1_smol-devel

This package contains library source intended for building other packages which
use the "sha1_smol" feature of the "%{crate}" crate.

%package     -n %{name}+socket2-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+socket2-devel

This package contains library source intended for building other packages which
use the "socket2" feature of the "%{crate}" crate.

%package     -n %{name}+streams-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+streams-devel

This package contains library source intended for building other packages which
use the "streams" feature of the "%{crate}" crate.

%package     -n %{name}+tcp_nodelay-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tcp_nodelay-devel

This package contains library source intended for building other packages which
use the "tcp_nodelay" feature of the "%{crate}" crate.

%package     -n %{name}+tls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tls-devel

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%package     -n %{name}+tls-native-tls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tls-native-tls-devel

This package contains library source intended for building other packages which
use the "tls-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tls-rustls-devel

This package contains library source intended for building other packages which
use the "tls-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-insecure-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tls-rustls-insecure-devel

This package contains library source intended for building other packages which
use the "tls-rustls-insecure" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-webpki-roots-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tls-rustls-webpki-roots-devel

This package contains library source intended for building other packages which
use the "tls-rustls-webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-comp-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-comp-devel

This package contains library source intended for building other packages which
use the "tokio-comp" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-native-tls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-native-tls-devel

This package contains library source intended for building other packages which
use the "tokio-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-native-tls-comp-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-native-tls-comp-devel

This package contains library source intended for building other packages which
use the "tokio-native-tls-comp" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-retry-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-retry-devel

This package contains library source intended for building other packages which
use the "tokio-retry" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-rustls-devel

This package contains library source intended for building other packages which
use the "tokio-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-comp-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-rustls-comp-devel

This package contains library source intended for building other packages which
use the "tokio-rustls-comp" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Driver for Rust
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Driver for Rust
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
%files -n rust-redis-devel -f %{oreon_filedir}/rust-redis-devel.list

%changelog

%autochangelog
