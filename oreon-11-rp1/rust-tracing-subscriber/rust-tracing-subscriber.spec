%global source0_hash cb7f578e5945fb242538965c2d0b04418d38ec25c79d160cd279bf0731c8d319
%bcond check 0
%global debug_package %{nil}
%global crate tracing-subscriber
Name:           rust-tracing-subscriber
Version:        0.3.23
Release:        1%{?dist}
Summary:        Utilities for implementing and composing `tracing` subscribers.
License:        MIT
URL:            https://crates.io/crates/tracing-subscriber
Source0:        https://static.crates.io/crates/tracing-subscriber/tracing-subscriber-%{version}.crate
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
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+ansi-devel

This package contains library source intended for building other packages which
use the "ansi" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+env-filter-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+env-filter-devel

This package contains library source intended for building other packages which
use the "env-filter" feature of the "%{crate}" crate.

%package     -n %{name}+fmt-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+fmt-devel

This package contains library source intended for building other packages which
use the "fmt" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+local-time-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+local-time-devel

This package contains library source intended for building other packages which
use the "local-time" feature of the "%{crate}" crate.

%package     -n %{name}+matchers-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+matchers-devel

This package contains library source intended for building other packages which
use the "matchers" feature of the "%{crate}" crate.

%package     -n %{name}+nu-ansi-term-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+nu-ansi-term-devel

This package contains library source intended for building other packages which
use the "nu-ansi-term" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+registry-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+registry-devel

This package contains library source intended for building other packages which
use the "registry" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sharded-slab-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+sharded-slab-devel

This package contains library source intended for building other packages which
use the "sharded-slab" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+thread_local-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+thread_local-devel

This package contains library source intended for building other packages which
use the "thread_local" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-log-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+tracing-log-devel

This package contains library source intended for building other packages which
use the "tracing-log" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-serde-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+tracing-serde-devel

This package contains library source intended for building other packages which
use the "tracing-serde" feature of the "%{crate}" crate.

%package     -n %{name}+valuable-devel
Summary:        Utilities for implementing and composing `tracing` subscribers.
BuildArch:      noarch
%description -n %{name}+valuable-devel

This package contains library source intended for building other packages which
use the "valuable" feature of the "%{crate}" crate.

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
%files -n rust-tracing-subscriber-devel -f %{oreon_filedir}/rust-tracing-subscriber-devel.list

%changelog

%autochangelog
