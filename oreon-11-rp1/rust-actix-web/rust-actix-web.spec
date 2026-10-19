%global source0_hash 1654a77ba142e37f049637a3e5685f864514af11fcbc51cb51eb6596afe5b8d6
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global crate actix-web
Name:           rust-actix-web
Version:        4.12.1
Release:        1%{?dist}
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-web
Source0:        https://static.crates.io/crates/actix-web/actix-web-%{version}.crate
Patch:          actix-web-fix-metadata.diff
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
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__compress-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+__compress-devel

This package contains library source intended for building other packages which
use the "__compress" feature of the "%{crate}" crate.

%package     -n %{name}+__tls-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+__tls-devel

This package contains library source intended for building other packages which
use the "__tls" feature of the "%{crate}" crate.

%package     -n %{name}+actix-tls-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+actix-tls-devel

This package contains library source intended for building other packages which
use the "actix-tls" feature of the "%{crate}" crate.

%package     -n %{name}+compat-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+compat-devel

This package contains library source intended for building other packages which
use the "compat" feature of the "%{crate}" crate.

%package     -n %{name}+compat-routing-macros-force-pub-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+compat-routing-macros-force-pub-devel

This package contains library source intended for building other packages which
use the "compat-routing-macros-force-pub" feature of the "%{crate}" crate.

%package     -n %{name}+compress-gzip-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+compress-gzip-devel

This package contains library source intended for building other packages which
use the "compress-gzip" feature of the "%{crate}" crate.

%package     -n %{name}+compress-zstd-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+compress-zstd-devel

This package contains library source intended for building other packages which
use the "compress-zstd" feature of the "%{crate}" crate.

%package     -n %{name}+cookies-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+cookies-devel

This package contains library source intended for building other packages which
use the "cookies" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%package     -n %{name}+secure-cookies-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+secure-cookies-devel

This package contains library source intended for building other packages which
use the "secure-cookies" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%package     -n %{name}+ws-devel
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust
BuildArch:      noarch
%description -n %{name}+ws-devel

This package contains library source intended for building other packages which
use the "ws" feature of the "%{crate}" crate.

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
%files -n rust-actix-web-devel -f %{oreon_filedir}/rust-actix-web-devel.list

%changelog

%autochangelog
