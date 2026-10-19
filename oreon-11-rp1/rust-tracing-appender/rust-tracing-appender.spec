%global source0_hash 786d480bce6247ab75f005b14ae1624ad978d3029d9113f0a22fa1ac773faeaf
%bcond check 1
%global debug_package %{nil}
%global crate tracing-appender
Name:           rust-tracing-appender
Version:        0.2.4
Release:        1%{?dist}
Summary:        Utilities for file appenders and making non-blocking writers
License:        MIT
URL:            https://crates.io/crates/tracing-appender
Source0:        https://static.crates.io/crates/tracing-appender/tracing-appender-%{version}.crate
Patch:          tracing-appender-fix-metadata.diff
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
Summary:        Utilities for file appenders and making non-blocking writers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Utilities for file appenders and making non-blocking writers
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

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
%files -n rust-tracing-appender-devel -f %{oreon_filedir}/rust-tracing-appender-devel.list

%changelog

%autochangelog
