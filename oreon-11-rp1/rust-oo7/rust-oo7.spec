%global source0_hash 6cb23d3ec3527d65a83be1c1795cb883c52cfa57147d42acc797127df56fc489
%bcond check 1
%global debug_package %{nil}
%global crate oo7
Name:           rust-oo7
Version:        0.4.3
Release:        1%{?dist}
Summary:        Library to access freedesktop.org D-Bus Secret Service
License:        MIT
URL:            https://crates.io/crates/oo7
Source0:        https://static.crates.io/crates/oo7/oo7-%{version}.crate
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
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+local_tests-devel
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+local_tests-devel

This package contains library source intended for building other packages which
use the "local_tests" feature of the "%{crate}" crate.

%package     -n %{name}+native_crypto-devel
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+native_crypto-devel

This package contains library source intended for building other packages which
use the "native_crypto" feature of the "%{crate}" crate.

%package     -n %{name}+openssl_crypto-devel
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+openssl_crypto-devel

This package contains library source intended for building other packages which
use the "openssl_crypto" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Library to access freedesktop.org D-Bus Secret Service
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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

%cargo_test -- -- --test-threads 1 --skip 'dbus::'
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-oo7-devel -f %{oreon_filedir}/rust-oo7-devel.list

%changelog

%autochangelog
