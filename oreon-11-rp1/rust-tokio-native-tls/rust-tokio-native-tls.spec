%global source0_hash bbae76ab933c85776efabc971569dd6119c580d8f5d448769dec1764bf796ef2
%bcond check 0
%global debug_package %{nil}
%global crate tokio-native-tls
Name:           rust-tokio-native-tls
Version:        0.3.1
Release:        1%{?dist}
Summary:        An implementation of TLS/SSL streams for Tokio using native-tls givin...
License:        MIT
URL:            https://crates.io/crates/tokio-native-tls
Source0:        https://static.crates.io/crates/tokio-native-tls/tokio-native-tls-%{version}.crate
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

%package     -n %{name}+vendored-devel
Summary:        An implementation of TLS/SSL streams for Tokio using native-tls givin...
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

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
%files -n rust-tokio-native-tls-devel -f %{oreon_filedir}/rust-tokio-native-tls-devel.list

%changelog

%autochangelog
