%global source0_hash 97d095ae15e245a057c8e8451bab9b3ee1e1f68e9ba2b4fbc18d0ac5237835f2
%bcond check 0
%global debug_package %{nil}
%global crate tracing-futures
Name:           rust-tracing-futures
Version:        0.2.5
Release:        1%{?dist}
Summary:        Utilities for instrumenting `futures` with `tracing`.
License:        MIT
URL:            https://crates.io/crates/tracing-futures
Source0:        https://static.crates.io/crates/tracing-futures/tracing-futures-%{version}.crate
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
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-01-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+futures-01-devel

This package contains library source intended for building other packages which
use the "futures-01" feature of the "%{crate}" crate.

%package     -n %{name}+futures-03-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+futures-03-devel

This package contains library source intended for building other packages which
use the "futures-03" feature of the "%{crate}" crate.

%package     -n %{name}+futures-task-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+futures-task-devel

This package contains library source intended for building other packages which
use the "futures-task" feature of the "%{crate}" crate.

%package     -n %{name}+futures_01-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+futures_01-devel

This package contains library source intended for building other packages which
use the "futures_01" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+pin-project-devel

This package contains library source intended for building other packages which
use the "pin-project" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+std-future-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+std-future-devel

This package contains library source intended for building other packages which
use the "std-future" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-executor-devel
Summary:        Utilities for instrumenting `futures` with `tracing`.
BuildArch:      noarch
%description -n %{name}+tokio-executor-devel

This package contains library source intended for building other packages which
use the "tokio-executor" feature of the "%{crate}" crate.

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
%files -n rust-tracing-futures-devel -f %{oreon_filedir}/rust-tracing-futures-devel.list

%changelog

%autochangelog
