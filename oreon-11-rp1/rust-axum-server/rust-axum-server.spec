%global source0_hash c1ab4a3ec9ea8a657c72d99a03a824af695bd0fb5ec639ccbd9cd3543b41a5f9
%bcond check 1
%global debug_package %{nil}
%global crate axum-server
Name:           rust-axum-server
Version:        0.7.3
Release:        1%{?dist}
Summary:        High level server designed to be used with axum framework
License:        MIT
URL:            https://crates.io/crates/axum-server
Source0:        https://static.crates.io/crates/axum-server/axum-server-%{version}.crate
Patch:          axum-server-fix-metadata.diff
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
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc-swap-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+arc-swap-devel

This package contains library source intended for building other packages which
use the "arc-swap" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-sys-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+openssl-sys-devel

This package contains library source intended for building other packages which
use the "openssl-sys" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-pemfile-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+rustls-pemfile-devel

This package contains library source intended for building other packages which
use the "rustls-pemfile" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-pki-types-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+rustls-pki-types-devel

This package contains library source intended for building other packages which
use the "rustls-pki-types" feature of the "%{crate}" crate.

%package     -n %{name}+tls-openssl-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+tls-openssl-devel

This package contains library source intended for building other packages which
use the "tls-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+tls-rustls-devel

This package contains library source intended for building other packages which
use the "tls-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-no-provider-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+tls-rustls-no-provider-devel

This package contains library source intended for building other packages which
use the "tls-rustls-no-provider" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-openssl-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+tokio-openssl-devel

This package contains library source intended for building other packages which
use the "tokio-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-devel
Summary:        High level server designed to be used with axum framework
BuildArch:      noarch
%description -n %{name}+tokio-rustls-devel

This package contains library source intended for building other packages which
use the "tokio-rustls" feature of the "%{crate}" crate.

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
%files -n rust-axum-server-devel -f %{oreon_filedir}/rust-axum-server-devel.list

%changelog

%autochangelog
