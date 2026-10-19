%global source0_hash dd5ad065e2697e98764f2738793904ff0aaa672707d0ee1592dfb4c47800962a
%bcond check 1
%global debug_package %{nil}
%global crate zlink
Name:           rust-zlink
Version:        0.4.0
Release:        1%{?dist}
Summary:        Async Varlink API
License:        MIT
URL:            https://crates.io/crates/zlink
Source0:        https://static.crates.io/crates/zlink/zlink-%{version}.crate
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
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+idl-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+idl-devel

This package contains library source intended for building other packages which
use the "idl" feature of the "%{crate}" crate.

%package     -n %{name}+idl-parse-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+idl-parse-devel

This package contains library source intended for building other packages which
use the "idl-parse" feature of the "%{crate}" crate.

%package     -n %{name}+introspection-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+introspection-devel

This package contains library source intended for building other packages which
use the "introspection" feature of the "%{crate}" crate.

%package     -n %{name}+proxy-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+proxy-devel

This package contains library source intended for building other packages which
use the "proxy" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+service-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+service-devel

This package contains library source intended for building other packages which
use the "service" feature of the "%{crate}" crate.

%package     -n %{name}+smol-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+smol-devel

This package contains library source intended for building other packages which
use the "smol" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Async Varlink API
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f smol,tokio
%install
%cargo_install -f smol,tokio
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f smol,tokio
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-zlink-devel -f %{oreon_filedir}/rust-zlink-devel.list

%changelog

%autochangelog
