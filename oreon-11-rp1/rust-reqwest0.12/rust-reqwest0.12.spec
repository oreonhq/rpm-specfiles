%global source0_hash eddd3ca559203180a307f12d114c268abf583f59b03cb906fd0b3ff8646c1147
%bcond check 1
%global debug_package %{nil}
%global crate reqwest
Name:           rust-reqwest0.12
Version:        0.12.28
Release:        1%{?dist}
Summary:        Higher level HTTP client library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/reqwest
Source0:        https://static.crates.io/crates/reqwest/reqwest-%{version}.crate
Patch:          reqwest-fix-metadata-auto.diff
Patch:          reqwest-fix-metadata.diff
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
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__rustls-devel

This package contains library source intended for building other packages which
use the "__rustls" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-ring-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__rustls-ring-devel

This package contains library source intended for building other packages which
use the "__rustls-ring" feature of the "%{crate}" crate.

%package     -n %{name}+__tls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__tls-devel

This package contains library source intended for building other packages which
use the "__tls" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+brotli-devel

This package contains library source intended for building other packages which
use the "brotli" feature of the "%{crate}" crate.

%package     -n %{name}+charset-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+charset-devel

This package contains library source intended for building other packages which
use the "charset" feature of the "%{crate}" crate.

%package     -n %{name}+cookies-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+cookies-devel

This package contains library source intended for building other packages which
use the "cookies" feature of the "%{crate}" crate.

%package     -n %{name}+default-tls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+default-tls-devel

This package contains library source intended for building other packages which
use the "default-tls" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+h2-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+h2-devel

This package contains library source intended for building other packages which
use the "h2" feature of the "%{crate}" crate.

%package     -n %{name}+hickory-dns-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+hickory-dns-devel

This package contains library source intended for building other packages which
use the "hickory-dns" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+multipart-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+multipart-devel

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-alpn-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+native-tls-alpn-devel

This package contains library source intended for building other packages which
use the "native-tls-alpn" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-devel

This package contains library source intended for building other packages which
use the "rustls-tls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-manual-roots-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-manual-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-manual-roots" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-manual-roots-no-provider-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-manual-roots-no-provider-devel

This package contains library source intended for building other packages which
use the "rustls-tls-manual-roots-no-provider" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-native-roots-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-native-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-native-roots-no-provider-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-native-roots-no-provider-devel

This package contains library source intended for building other packages which
use the "rustls-tls-native-roots-no-provider" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-no-provider-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-no-provider-devel

This package contains library source intended for building other packages which
use the "rustls-tls-no-provider" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-webpki-roots-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-webpki-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-webpki-roots-no-provider-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-webpki-roots-no-provider-devel

This package contains library source intended for building other packages which
use the "rustls-tls-webpki-roots-no-provider" feature of the "%{crate}" crate.

%package     -n %{name}+socks-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+socks-devel

This package contains library source intended for building other packages which
use the "socks" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%package     -n %{name}+system-proxy-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+system-proxy-devel

This package contains library source intended for building other packages which
use the "system-proxy" feature of the "%{crate}" crate.

%package     -n %{name}+trust-dns-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+trust-dns-devel

This package contains library source intended for building other packages which
use the "trust-dns" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

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
%files -n rust-reqwest0.12-devel -f %{oreon_filedir}/rust-reqwest0.12-devel.list

%changelog

%autochangelog
