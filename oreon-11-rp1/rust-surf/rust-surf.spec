%global source0_hash 718b1ae6b50351982dedff021db0def601677f2120938b070eadb10ba4038dd7
%bcond check 0
%global debug_package %{nil}
%global crate surf
Name:           rust-surf
Version:        2.3.2
Release:        1%{?dist}
Summary:        Surf the web - HTTP client framework
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/surf
Source0:        https://static.crates.io/crates/surf/surf-%{version}.crate
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
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-native-tls-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+async-native-tls-devel

This package contains library source intended for building other packages which
use the "async-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+curl-client-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+curl-client-devel

This package contains library source intended for building other packages which
use the "curl-client" feature of the "%{crate}" crate.

%package     -n %{name}+default-client-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+default-client-devel

This package contains library source intended for building other packages which
use the "default-client" feature of the "%{crate}" crate.

%package     -n %{name}+encoding-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+encoding-devel

This package contains library source intended for building other packages which
use the "encoding" feature of the "%{crate}" crate.

%package     -n %{name}+encoding_rs-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+encoding_rs-devel

This package contains library source intended for building other packages which
use the "encoding_rs" feature of the "%{crate}" crate.

%package     -n %{name}+h1-client-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+h1-client-devel

This package contains library source intended for building other packages which
use the "h1-client" feature of the "%{crate}" crate.

%package     -n %{name}+h1-client-no-tls-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+h1-client-no-tls-devel

This package contains library source intended for building other packages which
use the "h1-client-no-tls" feature of the "%{crate}" crate.

%package     -n %{name}+h1-client-rustls-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+h1-client-rustls-devel

This package contains library source intended for building other packages which
use the "h1-client-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-client-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+hyper-client-devel

This package contains library source intended for building other packages which
use the "hyper-client" feature of the "%{crate}" crate.

%package     -n %{name}+middleware-logger-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+middleware-logger-devel

This package contains library source intended for building other packages which
use the "middleware-logger" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+rustls_crate-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+rustls_crate-devel

This package contains library source intended for building other packages which
use the "rustls_crate" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-client-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+wasm-client-devel

This package contains library source intended for building other packages which
use the "wasm-client" feature of the "%{crate}" crate.

%package     -n %{name}+web-sys-devel
Summary:        Surf the web - HTTP client framework
BuildArch:      noarch
%description -n %{name}+web-sys-devel

This package contains library source intended for building other packages which
use the "web-sys" feature of the "%{crate}" crate.

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
%files -n rust-surf-devel -f %{oreon_filedir}/rust-surf-devel.list

%changelog

%autochangelog
