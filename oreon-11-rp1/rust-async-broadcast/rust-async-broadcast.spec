%global source0_hash 435a87a52755b8f27fcf321ac4f04b2802e337c8c4872923137471ec39c37532
%bcond check 0
%global debug_package %{nil}
%global crate async-broadcast
Name:           rust-async-broadcast
Version:        0.7.2
Release:        1%{?dist}
Summary:        Async broadcast channels
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/async-broadcast
Source0:        https://static.crates.io/crates/async-broadcast/async-broadcast-%{version}.crate
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
Summary:        Async broadcast channels
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
%files -n rust-async-broadcast-devel -f %{oreon_filedir}/rust-async-broadcast-devel.list

%changelog

%autochangelog
