%global source0_hash 5669c09dbcb4a0b5f6de8364154495574238e18d6736bbdaa7726307f3268471
%bcond check 0
%global debug_package %{nil}
%global crate logging_timer
Name:           rust-logging_timer
Version:        1.1.1
Release:        1%{?dist}
Summary:        Simple timers that log the elapsed time when dropped
License:        MIT
URL:            https://crates.io/crates/logging_timer
Source0:        https://static.crates.io/crates/logging_timer/logging_timer-%{version}.crate
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
Summary:        Simple timers that log the elapsed time when dropped
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-logging_timer-devel -f %{oreon_filedir}/rust-logging_timer-devel.list

%changelog

%autochangelog
