%global source0_hash eef8a023d2b19f44e430da334f7dfb5e5db219bb83e2b4f56a09c1cb12abe915
%bcond check 0
%global debug_package %{nil}
%global crate tracy-client-sys
Name:           rust-tracy-client-sys
Version:        0.30.0
Release:        1%{?dist}
Summary:        Low level bindings to the client libraries for the Tracy profiler
License:        (MIT OR Apache-2.0) AND BSD-3-Clause
URL:            https://crates.io/crates/tracy-client-sys
Source0:        https://static.crates.io/crates/tracy-client-sys/tracy-client-sys-%{version}.crate
Patch:          tracy-client-sys-fix-metadata-auto.diff
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
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+broadcast-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+broadcast-devel

This package contains library source intended for building other packages which
use the "broadcast" feature of the "%{crate}" crate.

%package     -n %{name}+callstack-inlines-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+callstack-inlines-devel

This package contains library source intended for building other packages which
use the "callstack-inlines" feature of the "%{crate}" crate.

%package     -n %{name}+code-transfer-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+code-transfer-devel

This package contains library source intended for building other packages which
use the "code-transfer" feature of the "%{crate}" crate.

%package     -n %{name}+context-switch-tracing-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+context-switch-tracing-devel

This package contains library source intended for building other packages which
use the "context-switch-tracing" feature of the "%{crate}" crate.

%package     -n %{name}+crash-handler-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+crash-handler-devel

This package contains library source intended for building other packages which
use the "crash-handler" feature of the "%{crate}" crate.

%package     -n %{name}+debuginfod-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+debuginfod-devel

This package contains library source intended for building other packages which
use the "debuginfod" feature of the "%{crate}" crate.

%package     -n %{name}+delayed-init-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+delayed-init-devel

This package contains library source intended for building other packages which
use the "delayed-init" feature of the "%{crate}" crate.

%package     -n %{name}+demangle-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+demangle-devel

This package contains library source intended for building other packages which
use the "demangle" feature of the "%{crate}" crate.

%package     -n %{name}+enable-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+enable-devel

This package contains library source intended for building other packages which
use the "enable" feature of the "%{crate}" crate.

%package     -n %{name}+fibers-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+fibers-devel

This package contains library source intended for building other packages which
use the "fibers" feature of the "%{crate}" crate.

%package     -n %{name}+flush-on-exit-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+flush-on-exit-devel

This package contains library source intended for building other packages which
use the "flush-on-exit" feature of the "%{crate}" crate.

%package     -n %{name}+manual-lifetime-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+manual-lifetime-devel

This package contains library source intended for building other packages which
use the "manual-lifetime" feature of the "%{crate}" crate.

%package     -n %{name}+ondemand-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+ondemand-devel

This package contains library source intended for building other packages which
use the "ondemand" feature of the "%{crate}" crate.

%package     -n %{name}+only-ipv4-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+only-ipv4-devel

This package contains library source intended for building other packages which
use the "only-ipv4" feature of the "%{crate}" crate.

%package     -n %{name}+only-localhost-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+only-localhost-devel

This package contains library source intended for building other packages which
use the "only-localhost" feature of the "%{crate}" crate.

%package     -n %{name}+sampling-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+sampling-devel

This package contains library source intended for building other packages which
use the "sampling" feature of the "%{crate}" crate.

%package     -n %{name}+system-tracing-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+system-tracing-devel

This package contains library source intended for building other packages which
use the "system-tracing" feature of the "%{crate}" crate.

%package     -n %{name}+timer-fallback-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+timer-fallback-devel

This package contains library source intended for building other packages which
use the "timer-fallback" feature of the "%{crate}" crate.

%package     -n %{name}+verify-devel
Summary:        Low level bindings to the client libraries for the Tracy profiler
BuildArch:      noarch
%description -n %{name}+verify-devel

This package contains library source intended for building other packages which
use the "verify" feature of the "%{crate}" crate.

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
%files -n rust-tracy-client-sys-devel -f %{oreon_filedir}/rust-tracy-client-sys-devel.list

%changelog

%autochangelog
