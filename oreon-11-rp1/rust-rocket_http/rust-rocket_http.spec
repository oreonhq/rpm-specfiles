%global source0_hash e274915a20ee3065f611c044bd63c40757396b6dbc057d6046aec27f14f882b9
%bcond check 0
%global debug_package %{nil}
%global crate rocket_http
Name:           rust-rocket_http
Version:        0.5.1
Release:        1%{?dist}
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rocket_http
Source0:        https://static.crates.io/crates/rocket_http/rocket_http-%{version}.crate
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
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+mtls-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+mtls-devel

This package contains library source intended for building other packages which
use the "mtls" feature of the "%{crate}" crate.

%package     -n %{name}+private-cookies-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+private-cookies-devel

This package contains library source intended for building other packages which
use the "private-cookies" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-pemfile-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+rustls-pemfile-devel

This package contains library source intended for building other packages which
use the "rustls-pemfile" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+serde_-devel

This package contains library source intended for building other packages which
use the "serde_" feature of the "%{crate}" crate.

%package     -n %{name}+tls-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+tls-devel

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+tokio-rustls-devel

This package contains library source intended for building other packages which
use the "tokio-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+uuid_-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+uuid_-devel

This package contains library source intended for building other packages which
use the "uuid_" feature of the "%{crate}" crate.

%package     -n %{name}+x509-parser-devel
Summary:        Types, traits, and parsers for HTTP requests, responses, and headers.
BuildArch:      noarch
%description -n %{name}+x509-parser-devel

This package contains library source intended for building other packages which
use the "x509-parser" feature of the "%{crate}" crate.

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
%files -n rust-rocket_http-devel -f %{oreon_filedir}/rust-rocket_http-devel.list

%changelog

%autochangelog
