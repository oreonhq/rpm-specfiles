%global source0_hash fe18fb60dc696039e738717b76eaea21e7a4489bbb1885020b43c94236d7e98a
%bcond check 0
%global debug_package %{nil}
%global crate zbus
Name:           rust-zbus
Version:        5.18.0
Release:        1%{?dist}
Summary:        API for D-Bus communication
License:        MIT
URL:            https://crates.io/crates/zbus
Source0:        https://static.crates.io/crates/zbus/zbus-%{version}.crate
Patch:          zbus-fix-metadata-auto.diff
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
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-executor-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+async-executor-devel

This package contains library source intended for building other packages which
use the "async-executor" feature of the "%{crate}" crate.

%package     -n %{name}+async-fs-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+async-fs-devel

This package contains library source intended for building other packages which
use the "async-fs" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+async-lock-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+async-lock-devel

This package contains library source intended for building other packages which
use the "async-lock" feature of the "%{crate}" crate.

%package     -n %{name}+async-process-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+async-process-devel

This package contains library source intended for building other packages which
use the "async-process" feature of the "%{crate}" crate.

%package     -n %{name}+async-task-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+async-task-devel

This package contains library source intended for building other packages which
use the "async-task" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-api-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+blocking-api-devel

This package contains library source intended for building other packages which
use the "blocking-api" feature of the "%{crate}" crate.

%package     -n %{name}+bus-impl-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+bus-impl-devel

This package contains library source intended for building other packages which
use the "bus-impl" feature of the "%{crate}" crate.

%package     -n %{name}+camino-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+camino-devel

This package contains library source intended for building other packages which
use the "camino" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+option-as-array-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+option-as-array-devel

This package contains library source intended for building other packages which
use the "option-as-array" feature of the "%{crate}" crate.

%package     -n %{name}+p2p-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+p2p-devel

This package contains library source intended for building other packages which
use the "p2p" feature of the "%{crate}" crate.

%package     -n %{name}+serde_bytes-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+serde_bytes-devel

This package contains library source intended for building other packages which
use the "serde_bytes" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-vsock-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+tokio-vsock-devel

This package contains library source intended for building other packages which
use the "tokio-vsock" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+vsock-devel
Summary:        API for D-Bus communication
BuildArch:      noarch
%description -n %{name}+vsock-devel

This package contains library source intended for building other packages which
use the "vsock" feature of the "%{crate}" crate.

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
%files -n rust-zbus-devel -f %{oreon_filedir}/rust-zbus-devel.list

%changelog

%autochangelog
