%global source0_hash 4cfcf7e2740e6fc6d4d688b4ef00650406bb94adf4731e43c096c3a19fe40840
%bcond check 0
%global debug_package %{nil}
%global crate tower-http
Name:           rust-tower-http
Version:        0.6.11
Release:        1%{?dist}
Summary:        Tower middleware and utilities for HTTP clients and servers
License:        MIT
URL:            https://crates.io/crates/tower-http
Source0:        https://static.crates.io/crates/tower-http/tower-http-%{version}.crate
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
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+add-extension-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+add-extension-devel

This package contains library source intended for building other packages which
use the "add-extension" feature of the "%{crate}" crate.

%package     -n %{name}+async-compression-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+async-compression-devel

This package contains library source intended for building other packages which
use the "async-compression" feature of the "%{crate}" crate.

%package     -n %{name}+auth-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+auth-devel

This package contains library source intended for building other packages which
use the "auth" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+catch-panic-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+catch-panic-devel

This package contains library source intended for building other packages which
use the "catch-panic" feature of the "%{crate}" crate.

%package     -n %{name}+compression-br-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+compression-br-devel

This package contains library source intended for building other packages which
use the "compression-br" feature of the "%{crate}" crate.

%package     -n %{name}+compression-deflate-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+compression-deflate-devel

This package contains library source intended for building other packages which
use the "compression-deflate" feature of the "%{crate}" crate.

%package     -n %{name}+compression-full-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+compression-full-devel

This package contains library source intended for building other packages which
use the "compression-full" feature of the "%{crate}" crate.

%package     -n %{name}+compression-gzip-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+compression-gzip-devel

This package contains library source intended for building other packages which
use the "compression-gzip" feature of the "%{crate}" crate.

%package     -n %{name}+compression-zstd-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+compression-zstd-devel

This package contains library source intended for building other packages which
use the "compression-zstd" feature of the "%{crate}" crate.

%package     -n %{name}+cors-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+cors-devel

This package contains library source intended for building other packages which
use the "cors" feature of the "%{crate}" crate.

%package     -n %{name}+decompression-br-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+decompression-br-devel

This package contains library source intended for building other packages which
use the "decompression-br" feature of the "%{crate}" crate.

%package     -n %{name}+decompression-deflate-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+decompression-deflate-devel

This package contains library source intended for building other packages which
use the "decompression-deflate" feature of the "%{crate}" crate.

%package     -n %{name}+decompression-full-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+decompression-full-devel

This package contains library source intended for building other packages which
use the "decompression-full" feature of the "%{crate}" crate.

%package     -n %{name}+decompression-gzip-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+decompression-gzip-devel

This package contains library source intended for building other packages which
use the "decompression-gzip" feature of the "%{crate}" crate.

%package     -n %{name}+decompression-zstd-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+decompression-zstd-devel

This package contains library source intended for building other packages which
use the "decompression-zstd" feature of the "%{crate}" crate.

%package     -n %{name}+follow-redirect-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+follow-redirect-devel

This package contains library source intended for building other packages which
use the "follow-redirect" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+httpdate-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+httpdate-devel

This package contains library source intended for building other packages which
use the "httpdate" feature of the "%{crate}" crate.

%package     -n %{name}+limit-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+limit-devel

This package contains library source intended for building other packages which
use the "limit" feature of the "%{crate}" crate.

%package     -n %{name}+map-request-body-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+map-request-body-devel

This package contains library source intended for building other packages which
use the "map-request-body" feature of the "%{crate}" crate.

%package     -n %{name}+map-response-body-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+map-response-body-devel

This package contains library source intended for building other packages which
use the "map-response-body" feature of the "%{crate}" crate.

%package     -n %{name}+metrics-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+metrics-devel

This package contains library source intended for building other packages which
use the "metrics" feature of the "%{crate}" crate.

%package     -n %{name}+mime-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+mime-devel

This package contains library source intended for building other packages which
use the "mime" feature of the "%{crate}" crate.

%package     -n %{name}+mime_guess-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+mime_guess-devel

This package contains library source intended for building other packages which
use the "mime_guess" feature of the "%{crate}" crate.

%package     -n %{name}+normalize-path-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+normalize-path-devel

This package contains library source intended for building other packages which
use the "normalize-path" feature of the "%{crate}" crate.

%package     -n %{name}+on-early-drop-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+on-early-drop-devel

This package contains library source intended for building other packages which
use the "on-early-drop" feature of the "%{crate}" crate.

%package     -n %{name}+percent-encoding-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+percent-encoding-devel

This package contains library source intended for building other packages which
use the "percent-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+propagate-header-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+propagate-header-devel

This package contains library source intended for building other packages which
use the "propagate-header" feature of the "%{crate}" crate.

%package     -n %{name}+redirect-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+redirect-devel

This package contains library source intended for building other packages which
use the "redirect" feature of the "%{crate}" crate.

%package     -n %{name}+request-id-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+request-id-devel

This package contains library source intended for building other packages which
use the "request-id" feature of the "%{crate}" crate.

%package     -n %{name}+sensitive-headers-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+sensitive-headers-devel

This package contains library source intended for building other packages which
use the "sensitive-headers" feature of the "%{crate}" crate.

%package     -n %{name}+set-header-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+set-header-devel

This package contains library source intended for building other packages which
use the "set-header" feature of the "%{crate}" crate.

%package     -n %{name}+set-status-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+set-status-devel

This package contains library source intended for building other packages which
use the "set-status" feature of the "%{crate}" crate.

%package     -n %{name}+timeout-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+timeout-devel

This package contains library source intended for building other packages which
use the "timeout" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%package     -n %{name}+tower-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+tower-devel

This package contains library source intended for building other packages which
use the "tower" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+util-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+util-devel

This package contains library source intended for building other packages which
use the "util" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+validate-request-devel
Summary:        Tower middleware and utilities for HTTP clients and servers
BuildArch:      noarch
%description -n %{name}+validate-request-devel

This package contains library source intended for building other packages which
use the "validate-request" feature of the "%{crate}" crate.

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
%files -n rust-tower-http-devel -f %{oreon_filedir}/rust-tower-http-devel.list

%changelog

%autochangelog
