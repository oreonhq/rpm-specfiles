%global source0_hash 5a09c0b5bb588872ab2f09afa13ee6e9dac11e10a0ec9e8e3ba39a5a5d530af6
%bcond check 0
%global debug_package %{nil}
%global crate tokio
Name:           rust-tokio0.1
Version:        0.1.22
Release:        1%{?dist}
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
License:        MIT
URL:            https://crates.io/crates/tokio
Source0:        https://static.crates.io/crates/tokio/tokio-%{version}.crate
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
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+codec-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+codec-devel

This package contains library source intended for building other packages which
use the "codec" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-tracing-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+experimental-tracing-devel

This package contains library source intended for building other packages which
use the "experimental-tracing" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+io-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+io-devel

This package contains library source intended for building other packages which
use the "io" feature of the "%{crate}" crate.

%package     -n %{name}+mio-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+mio-devel

This package contains library source intended for building other packages which
use the "mio" feature of the "%{crate}" crate.

%package     -n %{name}+num_cpus-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+num_cpus-devel

This package contains library source intended for building other packages which
use the "num_cpus" feature of the "%{crate}" crate.

%package     -n %{name}+reactor-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+reactor-devel

This package contains library source intended for building other packages which
use the "reactor" feature of the "%{crate}" crate.

%package     -n %{name}+rt-full-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+rt-full-devel

This package contains library source intended for building other packages which
use the "rt-full" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%package     -n %{name}+tcp-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tcp-devel

This package contains library source intended for building other packages which
use the "tcp" feature of the "%{crate}" crate.

%package     -n %{name}+timer-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+timer-devel

This package contains library source intended for building other packages which
use the "timer" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-codec-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-codec-devel

This package contains library source intended for building other packages which
use the "tokio-codec" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-current-thread-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-current-thread-devel

This package contains library source intended for building other packages which
use the "tokio-current-thread" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-executor-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-executor-devel

This package contains library source intended for building other packages which
use the "tokio-executor" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-fs-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-fs-devel

This package contains library source intended for building other packages which
use the "tokio-fs" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-io-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-io-devel

This package contains library source intended for building other packages which
use the "tokio-io" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-reactor-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-reactor-devel

This package contains library source intended for building other packages which
use the "tokio-reactor" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-sync-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-sync-devel

This package contains library source intended for building other packages which
use the "tokio-sync" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-tcp-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-tcp-devel

This package contains library source intended for building other packages which
use the "tokio-tcp" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-threadpool-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-threadpool-devel

This package contains library source intended for building other packages which
use the "tokio-threadpool" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-timer-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-timer-devel

This package contains library source intended for building other packages which
use the "tokio-timer" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-udp-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-udp-devel

This package contains library source intended for building other packages which
use the "tokio-udp" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-core-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tracing-core-devel

This package contains library source intended for building other packages which
use the "tracing-core" feature of the "%{crate}" crate.

%package     -n %{name}+udp-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+udp-devel

This package contains library source intended for building other packages which
use the "udp" feature of the "%{crate}" crate.

%package     -n %{name}+uds-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+uds-devel

This package contains library source intended for building other packages which
use the "uds" feature of the "%{crate}" crate.

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
%files -n rust-tokio0.1-devel -f %{oreon_filedir}/rust-tokio0.1-devel.list

%changelog

%autochangelog
