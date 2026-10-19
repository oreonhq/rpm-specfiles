%global source0_hash 031b47cf1a3c6cc8bc2fc76cd437f521619387907d469316e7c0bc278f1f5432
%bcond check 0
%global debug_package %{nil}
%global crate futures-executor
Name:           rust-futures-executor
Version:        0.3.34
Release:        1%{?dist}
Summary:        Executors for asynchronous tasks based on the futures-rs library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-executor
Source0:        https://static.crates.io/crates/futures-executor/futures-executor-%{version}.crate
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
Summary:        Executors for asynchronous tasks based on the futures-rs library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Executors for asynchronous tasks based on the futures-rs library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+thread-pool-devel
Summary:        Executors for asynchronous tasks based on the futures-rs library
BuildArch:      noarch
%description -n %{name}+thread-pool-devel

This package contains library source intended for building other packages which
use the "thread-pool" feature of the "%{crate}" crate.

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
%files -n rust-futures-executor-devel -f %{oreon_filedir}/rust-futures-executor-devel.list

%changelog

%autochangelog
