%global source0_hash 5a07b7c1885bd8ed3831c289b7870b13ef46fe0e856d288c30d9cc17d75a2092
%bcond check 0
%global debug_package %{nil}
%global crate rustls-native-certs
Name:           rust-rustls-native-certs0.5
Version:        0.5.0
Release:        1%{?dist}
Summary:        rustls-native-certs allows rustls to use the platform native certific...
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/rustls-native-certs
Source0:        https://static.crates.io/crates/rustls-native-certs/rustls-native-certs-%{version}.crate
Patch:          rustls-native-certs-fix-metadata-auto.diff
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
Summary:        rustls-native-certs allows rustls to use the platform native certific...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        rustls-native-certs allows rustls to use the platform native certific...
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

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
%files -n rust-rustls-native-certs0.5-devel -f %{oreon_filedir}/rust-rustls-native-certs0.5-devel.list

%changelog

%autochangelog
