%global source0_hash 465500e14ea162429d264d44189adc38b199b62b1c21eea9f69e4b73cb03bbf2
%bcond check 0
%global debug_package %{nil}
%global crate native-tls
Name:           rust-native-tls
Version:        0.2.18
Release:        1%{?dist}
Summary:        A wrapper over a platform's native TLS implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/native-tls
Source0:        https://static.crates.io/crates/native-tls/native-tls-%{version}.crate
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
Summary:        A wrapper over a platform's native TLS implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alpn-devel
Summary:        A wrapper over a platform's native TLS implementation
BuildArch:      noarch
%description -n %{name}+alpn-devel

This package contains library source intended for building other packages which
use the "alpn" feature of the "%{crate}" crate.

%package     -n %{name}+alpn-accept-devel
Summary:        A wrapper over a platform's native TLS implementation
BuildArch:      noarch
%description -n %{name}+alpn-accept-devel

This package contains library source intended for building other packages which
use the "alpn-accept" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        A wrapper over a platform's native TLS implementation
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
%files -n rust-native-tls-devel -f %{oreon_filedir}/rust-native-tls-devel.list

%changelog

%autochangelog
