%global source0_hash 02d1a66277ed75f640d608235660df48c8e3c19f3b4edb6a263315626cc3c01d
%bcond check 1
%global debug_package %{nil}
%global crate ureq
Name:           rust-ureq
Version:        2.12.1
Release:        1%{?dist}
Summary:        Simple, safe HTTP client
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ureq
Source0:        https://static.crates.io/crates/ureq/ureq-%{version}.crate
Patch:          ureq-fix-metadata.diff
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
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+charset-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+charset-devel

This package contains library source intended for building other packages which
use the "charset" feature of the "%{crate}" crate.

%package     -n %{name}+cookies-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+cookies-devel

This package contains library source intended for building other packages which
use the "cookies" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+http-crate-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+http-crate-devel

This package contains library source intended for building other packages which
use the "http-crate" feature of the "%{crate}" crate.

%package     -n %{name}+http-interop-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+http-interop-devel

This package contains library source intended for building other packages which
use the "http-interop" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+native-certs-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+native-certs-devel

This package contains library source intended for building other packages which
use the "native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+proxy-from-env-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+proxy-from-env-devel

This package contains library source intended for building other packages which
use the "proxy-from-env" feature of the "%{crate}" crate.

%package     -n %{name}+socks-proxy-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+socks-proxy-devel

This package contains library source intended for building other packages which
use the "socks-proxy" feature of the "%{crate}" crate.

%package     -n %{name}+tls-devel
Summary:        Simple, safe HTTP client
BuildArch:      noarch
%description -n %{name}+tls-devel

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

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

%{cargo_test -- -- %{shrink:
    --skip error::tests::status_code_error_redirect
    --skip test::range::read_range_rustls
    --skip tests::connect_http_google
    --skip tests::connect_https_google_rustls
    --skip src/agent.rs
    --skip src/error.rs
    --skip src/lib.rs
    --skip src/request.rs
    --skip src/response.rs
    --skip ipv6_addr_in_dns_name
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ureq-devel -f %{oreon_filedir}/rust-ureq-devel.list

%changelog

%autochangelog
