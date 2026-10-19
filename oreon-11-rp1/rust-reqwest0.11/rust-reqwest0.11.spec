%global source0_hash dd67538700a17451e7cba03ac727fb961abb7607553461627b97de0b89cf4a62
%bcond check 1
%global debug_package %{nil}
%global crate reqwest
Name:           rust-reqwest0.11
Version:        0.11.27
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

%package     -n %{name}+__internal_proxy_sys_no_cache-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__internal_proxy_sys_no_cache-devel

This package contains library source intended for building other packages which
use the "__internal_proxy_sys_no_cache" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__rustls-devel

This package contains library source intended for building other packages which
use the "__rustls" feature of the "%{crate}" crate.

%package     -n %{name}+__tls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__tls-devel

This package contains library source intended for building other packages which
use the "__tls" feature of the "%{crate}" crate.

%package     -n %{name}+async-compression-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+async-compression-devel

This package contains library source intended for building other packages which
use the "async-compression" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+cookie_crate-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+cookie_crate-devel

This package contains library source intended for building other packages which
use the "cookie_crate" feature of the "%{crate}" crate.

%package     -n %{name}+cookie_store-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+cookie_store-devel

This package contains library source intended for building other packages which
use the "cookie_store" feature of the "%{crate}" crate.

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

%package     -n %{name}+hickory-dns-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+hickory-dns-devel

This package contains library source intended for building other packages which
use the "hickory-dns" feature of the "%{crate}" crate.

%package     -n %{name}+hickory-resolver-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+hickory-resolver-devel

This package contains library source intended for building other packages which
use the "hickory-resolver" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-rustls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+hyper-rustls-devel

This package contains library source intended for building other packages which
use the "hyper-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-tls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+hyper-tls-devel

This package contains library source intended for building other packages which
use the "hyper-tls" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+mime_guess-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+mime_guess-devel

This package contains library source intended for building other packages which
use the "mime_guess" feature of the "%{crate}" crate.

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

%package     -n %{name}+native-tls-crate-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+native-tls-crate-devel

This package contains library source intended for building other packages which
use the "native-tls-crate" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

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

%package     -n %{name}+rustls-tls-native-roots-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-native-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-webpki-roots-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-tls-webpki-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

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

%package     -n %{name}+tokio-native-tls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+tokio-native-tls-devel

This package contains library source intended for building other packages which
use the "tokio-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+tokio-rustls-devel

This package contains library source intended for building other packages which
use the "tokio-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-socks-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+tokio-socks-devel

This package contains library source intended for building other packages which
use the "tokio-socks" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%package     -n %{name}+trust-dns-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+trust-dns-devel

This package contains library source intended for building other packages which
use the "trust-dns" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+webpki-roots-devel

This package contains library source intended for building other packages which
use the "webpki-roots" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm tests/brotli.rs
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip proxy::test::into_proxy_scheme::when_scheme_present::and_url_has_bad::invalid_domain_character
    --skip test_allowed_methods
    --skip test_badssl_modern
    --skip test_badssl_self_signed
    --skip test_tls_info
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-reqwest0.11-devel -f %{oreon_filedir}/rust-reqwest0.11-devel.list

%changelog

%autochangelog
