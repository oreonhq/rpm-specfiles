%global source0_hash 4e8257fbc510f0a46eb602c10215901938b5c2a7d5e70fc11483b1d3c9b5b18c
%ifarch x86_64 %{ix86}
%bcond check 0
%else
%bcond check 1
%endif
%global debug_package %{nil}
%global crate v_htmlescape
Name:           rust-v_htmlescape
Version:        0.15.8
Release:        1%{?dist}
Summary:        Simd optimized HTML escaping code
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/v_htmlescape
Source0:        https://static.crates.io/crates/v_htmlescape/v_htmlescape-%{version}.crate
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
Summary:        Simd optimized HTML escaping code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+buf-min-devel
Summary:        Simd optimized HTML escaping code
BuildArch:      noarch
%description -n %{name}+buf-min-devel

This package contains library source intended for building other packages which
use the "buf-min" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-buf-devel
Summary:        Simd optimized HTML escaping code
BuildArch:      noarch
%description -n %{name}+bytes-buf-devel

This package contains library source intended for building other packages which
use the "bytes-buf" feature of the "%{crate}" crate.

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
%files -n rust-v_htmlescape-devel -f %{oreon_filedir}/rust-v_htmlescape-devel.list

%changelog

%autochangelog
