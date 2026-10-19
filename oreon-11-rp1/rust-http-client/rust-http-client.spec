%global source0_hash 1947510dc91e2bf586ea5ffb412caad7673264e14bb39fb9078da114a94ce1a5
%bcond check 0
%global debug_package %{nil}
%global crate http-client
Name:           rust-http-client
Version:        6.5.3
Release:        1%{?dist}
Summary:        Types and traits for http clients.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/http-client
Source0:        https://static.crates.io/crates/http-client/http-client-%{version}.crate
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
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-h1-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+async-h1-devel

This package contains library source intended for building other packages which
use the "async-h1" feature of the "%{crate}" crate.

%package     -n %{name}+async-native-tls-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+async-native-tls-devel

This package contains library source intended for building other packages which
use the "async-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async-tls-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+async-tls-devel

This package contains library source intended for building other packages which
use the "async-tls" feature of the "%{crate}" crate.

%package     -n %{name}+curl_client-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+curl_client-devel

This package contains library source intended for building other packages which
use the "curl_client" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

%package     -n %{name}+deadpool-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+deadpool-devel

This package contains library source intended for building other packages which
use the "deadpool" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+h1_client-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+h1_client-devel

This package contains library source intended for building other packages which
use the "h1_client" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+hyper-devel

This package contains library source intended for building other packages which
use the "hyper" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-tls-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+hyper-tls-devel

This package contains library source intended for building other packages which
use the "hyper-tls" feature of the "%{crate}" crate.

%package     -n %{name}+hyper_client-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+hyper_client-devel

This package contains library source intended for building other packages which
use the "hyper_client" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+native_client-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+native_client-devel

This package contains library source intended for building other packages which
use the "native_client" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls_crate-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+rustls_crate-devel

This package contains library source intended for building other packages which
use the "rustls_crate" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-config-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+unstable-config-devel

This package contains library source intended for building other packages which
use the "unstable-config" feature of the "%{crate}" crate.

%package     -n %{name}+wasm_client-devel
Summary:        Types and traits for http clients.
BuildArch:      noarch
%description -n %{name}+wasm_client-devel

This package contains library source intended for building other packages which
use the "wasm_client" feature of the "%{crate}" crate.

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
%files -n rust-http-client-devel -f %{oreon_filedir}/rust-http-client-devel.list

%changelog

%autochangelog
