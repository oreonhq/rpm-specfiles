%global source0_hash b8b88ea9df13354b55bc7234ebcce36e6ef896aca2e42a15de9e10edce01b427
%bcond check 0
%global debug_package %{nil}
%global crate color-spantrace
Name:           rust-color-spantrace
Version:        0.3.0
Release:        1%{?dist}
Summary:        Pretty printer for tracing_error::SpanTrace based on color-backtrace
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/color-spantrace
Source0:        https://static.crates.io/crates/color-spantrace/color-spantrace-%{version}.crate
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
Summary:        Pretty printer for tracing_error::SpanTrace based on color-backtrace
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
%files -n rust-color-spantrace-devel -f %{oreon_filedir}/rust-color-spantrace-devel.list

%changelog

%autochangelog
