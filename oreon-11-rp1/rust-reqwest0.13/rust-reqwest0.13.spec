%global source0_hash 219c5811de6525e5416c7d5d53bb656d3afdbc6c5af816e0802bcfa42dbdc1c3
%bcond check 0
%global debug_package %{nil}
%global crate reqwest
Name:           rust-reqwest0.13
Version:        0.13.4
Release:        1%{?dist}
Summary:        higher level HTTP client library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/reqwest
Source0:        https://static.crates.io/crates/reqwest/reqwest-%{version}.crate
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
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__native-tls-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__native-tls-devel

This package contains library source intended for building other packages which
use the "__native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+__native-tls-alpn-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__native-tls-alpn-devel

This package contains library source intended for building other packages which
use the "__native-tls-alpn" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__rustls-devel

This package contains library source intended for building other packages which
use the "__rustls" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-aws-lc-rs-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__rustls-aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "__rustls-aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+__tls-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+__tls-devel

This package contains library source intended for building other packages which
use the "__tls" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+brotli-devel

This package contains library source intended for building other packages which
use the "brotli" feature of the "%{crate}" crate.

%package     -n %{name}+charset-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+charset-devel

This package contains library source intended for building other packages which
use the "charset" feature of the "%{crate}" crate.

%package     -n %{name}+cookies-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+cookies-devel

This package contains library source intended for building other packages which
use the "cookies" feature of the "%{crate}" crate.

%package     -n %{name}+default-tls-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+default-tls-devel

This package contains library source intended for building other packages which
use the "default-tls" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+form-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+form-devel

This package contains library source intended for building other packages which
use the "form" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+hickory-dns-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+hickory-dns-devel

This package contains library source intended for building other packages which
use the "hickory-dns" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+http3-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+http3-devel

This package contains library source intended for building other packages which
use the "http3" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+mime_guess-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+mime_guess-devel

This package contains library source intended for building other packages which
use the "mime_guess" feature of the "%{crate}" crate.

%package     -n %{name}+multipart-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+multipart-devel

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-no-alpn-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+native-tls-no-alpn-devel

This package contains library source intended for building other packages which
use the "native-tls-no-alpn" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-vendored-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+native-tls-vendored-devel

This package contains library source intended for building other packages which
use the "native-tls-vendored" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-vendored-no-alpn-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+native-tls-vendored-no-alpn-devel

This package contains library source intended for building other packages which
use the "native-tls-vendored-no-alpn" feature of the "%{crate}" crate.

%package     -n %{name}+query-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+query-devel

This package contains library source intended for building other packages which
use the "query" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-no-provider-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+rustls-no-provider-devel

This package contains library source intended for building other packages which
use the "rustls-no-provider" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_urlencoded-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+serde_urlencoded-devel

This package contains library source intended for building other packages which
use the "serde_urlencoded" feature of the "%{crate}" crate.

%package     -n %{name}+socks-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+socks-devel

This package contains library source intended for building other packages which
use the "socks" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%package     -n %{name}+system-proxy-devel
Summary:        higher level HTTP client library
BuildArch:      noarch
%description -n %{name}+system-proxy-devel

This package contains library source intended for building other packages which
use the "system-proxy" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        higher level HTTP client library
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
%files -n rust-reqwest0.13-devel -f %{oreon_filedir}/rust-reqwest0.13-devel.list

%changelog

%autochangelog
