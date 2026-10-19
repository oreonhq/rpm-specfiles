%global source0_hash d0879bd39df99c4c5e2c6615ccc026391a423dde10532c573e6086eb94a802cc
%bcond check 0
%global debug_package %{nil}
%global crate jiff-static
Name:           rust-jiff-static
Version:        0.2.32
Release:        1%{?dist}
Summary:        Create static TimeZone values for Jiff (useful in core-only environme...
License:        Unlicense OR MIT
URL:            https://crates.io/crates/jiff-static
Source0:        https://static.crates.io/crates/jiff-static/jiff-static-%{version}.crate
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
Summary:        Create static TimeZone values for Jiff (useful in core-only environme...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+perf-inline-devel
Summary:        Create static TimeZone values for Jiff (useful in core-only environme...
BuildArch:      noarch
%description -n %{name}+perf-inline-devel

This package contains library source intended for building other packages which
use the "perf-inline" feature of the "%{crate}" crate.

%package     -n %{name}+tz-fat-devel
Summary:        Create static TimeZone values for Jiff (useful in core-only environme...
BuildArch:      noarch
%description -n %{name}+tz-fat-devel

This package contains library source intended for building other packages which
use the "tz-fat" feature of the "%{crate}" crate.

%package     -n %{name}+tzdb-devel
Summary:        Create static TimeZone values for Jiff (useful in core-only environme...
BuildArch:      noarch
%description -n %{name}+tzdb-devel

This package contains library source intended for building other packages which
use the "tzdb" feature of the "%{crate}" crate.

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
%files -n rust-jiff-static-devel -f %{oreon_filedir}/rust-jiff-static-devel.list

%changelog

%autochangelog
