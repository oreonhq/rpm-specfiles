%global source1_hash 92d82b247046525130b278df9c1d3d985f78cce81eb93722bd3d9dd9094185c2
%global source0_hash 7b047adab56acc4948d4b9b58693c1f33fd13efef2d6bb5f0f66a47436ceada8
%bcond check 1
%global debug_package %{nil}
%global crate qapi
Name:           rust-qapi
Version:        0.15.0
Release:        1%{?dist}
Summary:        QEMU QMP and Guest Agent API
License:        MIT
URL:            https://crates.io/crates/qapi
Source0:        https://static.crates.io/crates/qapi/qapi-%{version}.crate
Source1:        https://raw.githubusercontent.com/arcnmx/qapi-rs/refs/heads/main/COPYING
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
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+async-tokio-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+async-tokio-devel

This package contains library source intended for building other packages which
use the "async-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+async-tokio-all-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+async-tokio-all-devel

This package contains library source intended for building other packages which
use the "async-tokio-all" feature of the "%{crate}" crate.

%package     -n %{name}+async-tokio-net-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+async-tokio-net-devel

This package contains library source intended for building other packages which
use the "async-tokio-net" feature of the "%{crate}" crate.

%package     -n %{name}+async-tokio-spawn-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+async-tokio-spawn-devel

This package contains library source intended for building other packages which
use the "async-tokio-spawn" feature of the "%{crate}" crate.

%package     -n %{name}+async-tower-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+async-tower-devel

This package contains library source intended for building other packages which
use the "async-tower" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+qapi-qga-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+qapi-qga-devel

This package contains library source intended for building other packages which
use the "qapi-qga" feature of the "%{crate}" crate.

%package     -n %{name}+qapi-qmp-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+qapi-qmp-devel

This package contains library source intended for building other packages which
use the "qapi-qmp" feature of the "%{crate}" crate.

%package     -n %{name}+qga-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+qga-devel

This package contains library source intended for building other packages which
use the "qga" feature of the "%{crate}" crate.

%package     -n %{name}+qmp-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+qmp-devel

This package contains library source intended for building other packages which
use the "qmp" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%package     -n %{name}+tower-service-devel
Summary:        QEMU QMP and Guest Agent API
BuildArch:      noarch
%description -n %{name}+tower-service-devel

This package contains library source intended for building other packages which
use the "tower-service" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-qapi-devel -f %{oreon_filedir}/rust-qapi-devel.list

%changelog

%autochangelog
