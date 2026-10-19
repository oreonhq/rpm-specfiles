%global source2_hash c986bcdb83103d4ddf58aeb7b5302359782e54dc4eea14a0cc27c62dcbd50729
%global source1_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash 59d2aba832b60be25c1b169146b27c64115470981b128ed84c8db18c1b03c6ff
%bcond check 0
%global debug_package %{nil}
%global crate hash32-derive
Name:           rust-hash32-derive
Version:        0.1.1
Release:        1%{?dist}
Summary:        Macros 1.1 implementation of #[derive(Hash32)]
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hash32-derive
Source0:        https://static.crates.io/crates/hash32-derive/hash32-derive-%{version}.crate
Source1:        https://raw.githubusercontent.com/japaric/hash32/main/LICENSE-APACHE
Source2:        https://raw.githubusercontent.com/japaric/hash32/main/LICENSE-MIT
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
Summary:        Macros 1.1 implementation of #[derive(Hash32)]
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
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
%files -n rust-hash32-derive-devel -f %{oreon_filedir}/rust-hash32-derive-devel.list

%changelog

%autochangelog
