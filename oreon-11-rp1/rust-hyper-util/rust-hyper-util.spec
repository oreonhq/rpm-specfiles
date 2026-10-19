%global source0_hash 96547c2556ec9d12fb1578c4eaf448b04993e7fb79cbaad930a656880a6bdfa0
%bcond check 0
%global debug_package %{nil}
%global crate hyper-util
Name:           rust-hyper-util
Version:        0.1.20
Release:        1%{?dist}
Summary:        hyper utilities
License:        MIT
URL:            https://crates.io/crates/hyper-util
Source0:        https://static.crates.io/crates/hyper-util/hyper-util-%{version}.crate
Patch:          hyper-util-fix-metadata-auto.diff
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
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__internal_happy_eyeballs_tests-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+__internal_happy_eyeballs_tests-devel

This package contains library source intended for building other packages which
use the "__internal_happy_eyeballs_tests" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+client-legacy-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+client-legacy-devel

This package contains library source intended for building other packages which
use the "client-legacy" feature of the "%{crate}" crate.

%package     -n %{name}+client-pool-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+client-pool-devel

This package contains library source intended for building other packages which
use the "client-pool" feature of the "%{crate}" crate.

%package     -n %{name}+client-proxy-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+client-proxy-devel

This package contains library source intended for building other packages which
use the "client-proxy" feature of the "%{crate}" crate.

%package     -n %{name}+client-proxy-system-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+client-proxy-system-devel

This package contains library source intended for building other packages which
use the "client-proxy-system" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+http1-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+http1-devel

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+server-auto-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+server-auto-devel

This package contains library source intended for building other packages which
use the "server-auto" feature of the "%{crate}" crate.

%package     -n %{name}+server-graceful-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+server-graceful-devel

This package contains library source intended for building other packages which
use the "server-graceful" feature of the "%{crate}" crate.

%package     -n %{name}+service-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+service-devel

This package contains library source intended for building other packages which
use the "service" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        hyper utilities
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-hyper-util-devel -f %{oreon_filedir}/rust-hyper-util-devel.list

%changelog

%autochangelog
