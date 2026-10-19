%global source0_hash 4638549219af538d12f0c9855c55c2adc45d378428fe76635daeccfded9908cc
%bcond check 1
%global debug_package %{nil}
%global crate warp-sessions
Name:           rust-warp-sessions
Version:        1.0.21
Release:        1%{?dist}
Summary:        Generic session middleware for the warp HTTP framework
License:        MIT
URL:            https://crates.io/crates/warp-sessions
Source0:        https://static.crates.io/crates/warp-sessions/warp-sessions-%{version}.crate
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
Summary:        Generic session middleware for the warp HTTP framework
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
%files -n rust-warp-sessions-devel -f %{oreon_filedir}/rust-warp-sessions-devel.list

%changelog

%autochangelog
