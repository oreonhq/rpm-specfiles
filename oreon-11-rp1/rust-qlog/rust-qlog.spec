%global source2_hash 2ef4b5abfce387a83933bda738e72467a79d15c1c17679143ec55011dae66b84
%global source0_hash 0f15b83c59e6b945f2261c95a1dd9faf239187f32ff0a96af1d1d28c4557f919
%bcond check 1
%global debug_package %{nil}
%global crate qlog
Name:           rust-qlog
Version:        0.15.2
Release:        1%{?dist}
Summary:        Qlog data model for QUIC and HTTP/3
License:        BSD-2-Clause
URL:            https://crates.io/crates/qlog
Source0:        https://static.crates.io/crates/qlog/qlog-%{version}.crate
Source2:        https://github.com/cloudflare/quiche/raw/refs/tags/qlog-0.15.2/COPYING
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
Summary:        Qlog data model for QUIC and HTTP/3
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pL %{SOURCE2} .
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
%files -n rust-qlog-devel -f %{oreon_filedir}/rust-qlog-devel.list

%changelog

%autochangelog
