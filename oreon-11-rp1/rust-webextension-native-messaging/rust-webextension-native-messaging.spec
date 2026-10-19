%global source0_hash d2b651c70d995e28eef3263174a9016b2250ba9b2e226a9e7fbc7f90402c7093
%bcond check 1
%global debug_package %{nil}
%global crate webextension-native-messaging
Name:           rust-webextension-native-messaging
Version:        1.0.1
Release:        1%{?dist}
Summary:        WebExtension native messaging library for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/webextension-native-messaging
Source0:        https://static.crates.io/crates/webextension-native-messaging/webextension-native-messaging-%{version}.crate
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
Summary:        WebExtension native messaging library for Rust
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
%files -n rust-webextension-native-messaging-devel -f %{oreon_filedir}/rust-webextension-native-messaging-devel.list

%changelog

%autochangelog
