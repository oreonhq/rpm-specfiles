%global source0_hash 46409491c9375a693ce7032101970a54f8a2010efb77e13f70788f0d84489e39
%bcond check 0
%global debug_package %{nil}
%global crate tokio
Name:           rust-tokio0.3
Version:        0.3.7
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

%package     -n %{name}+bytes-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

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

%package     -n %{name}+once_cell-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

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

%package     -n %{name}+rt-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+rt-devel

This package contains library source intended for building other packages which
use the "rt" feature of the "%{crate}" crate.

%package     -n %{name}+rt-multi-thread-devel
Summary:        An event-driven, non-blocking I/O platform for writing asynchronous I/O
BuildArch:      noarch
%description -n %{name}+rt-multi-thread-devel

This package contains library source intended for building other packages which
use the "rt-multi-thread" feature of the "%{crate}" crate.

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
%files -n rust-tokio0.3-devel -f %{oreon_filedir}/rust-tokio0.3-devel.list

%changelog

%autochangelog
