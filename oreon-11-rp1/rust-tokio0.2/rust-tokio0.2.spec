%global source0_hash 6703a273949a90131b290be1fe7b039d0fc884aa1935860dfcbe056f28cd8092
%bcond check 0
%global debug_package %{nil}
%global crate tokio
Name:           rust-tokio0.2
Version:        0.2.25
Release:        1%{?dist}
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
License:        MIT
URL:            https://crates.io/crates/tokio
Source0:        https://static.crates.io/crates/tokio/tokio-%{version}.crate
Patch:          tokio-fix-metadata-auto.diff
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

%package     -n %{name}+blocking-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+dns-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+dns-devel

This package contains library source intended for building other packages which
use the "dns" feature of the "%{crate}" crate.

%package     -n %{name}+fnv-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+fnv-devel

This package contains library source intended for building other packages which
use the "fnv" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+io-driver-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+io-driver-devel

This package contains library source intended for building other packages which
use the "io-driver" feature of the "%{crate}" crate.

%package     -n %{name}+io-std-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+io-std-devel

This package contains library source intended for building other packages which
use the "io-std" feature of the "%{crate}" crate.

%package     -n %{name}+io-util-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+io-util-devel

This package contains library source intended for building other packages which
use the "io-util" feature of the "%{crate}" crate.

%package     -n %{name}+iovec-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+iovec-devel

This package contains library source intended for building other packages which
use the "iovec" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+lazy_static-devel

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+mio-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+mio-devel

This package contains library source intended for building other packages which
use the "mio" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+num_cpus-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+num_cpus-devel

This package contains library source intended for building other packages which
use the "num_cpus" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+process-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+process-devel

This package contains library source intended for building other packages which
use the "process" feature of the "%{crate}" crate.

%package     -n %{name}+rt-core-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+rt-core-devel

This package contains library source intended for building other packages which
use the "rt-core" feature of the "%{crate}" crate.

%package     -n %{name}+rt-threaded-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+rt-threaded-devel

This package contains library source intended for building other packages which
use the "rt-threaded" feature of the "%{crate}" crate.

%package     -n %{name}+rt-util-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+rt-util-devel

This package contains library source intended for building other packages which
use the "rt-util" feature of the "%{crate}" crate.

%package     -n %{name}+signal-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+signal-devel

This package contains library source intended for building other packages which
use the "signal" feature of the "%{crate}" crate.

%package     -n %{name}+slab-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+slab-devel

This package contains library source intended for building other packages which
use the "slab" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

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

%package     -n %{name}+test-util-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+test-util-devel

This package contains library source intended for building other packages which
use the "test-util" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-macros-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tokio-macros-devel

This package contains library source intended for building other packages which
use the "tokio-macros" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-tokio0.2-devel -f %{oreon_filedir}/rust-tokio0.2-devel.list

%changelog

%autochangelog
