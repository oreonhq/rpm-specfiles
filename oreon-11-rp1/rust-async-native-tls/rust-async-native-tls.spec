%global source0_hash 9e9e7a929bd34c68a82d58a4de7f86fffdaf97fb2af850162a7bb19dd7269b33
%bcond check 0
%global debug_package %{nil}
%global crate async-native-tls
Name:           rust-async-native-tls
Version:        0.3.3
Release:        1%{?dist}
Summary:        Native TLS using futures
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/async-native-tls
Source0:        https://static.crates.io/crates/async-native-tls/async-native-tls-%{version}.crate
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
Summary:        Native TLS using futures
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Native TLS using futures
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-async-std-devel
Summary:        Native TLS using futures
BuildArch:      noarch
%description -n %{name}+runtime-async-std-devel

This package contains library source intended for building other packages which
use the "runtime-async-std" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-tokio-devel
Summary:        Native TLS using futures
BuildArch:      noarch
%description -n %{name}+runtime-tokio-devel

This package contains library source intended for building other packages which
use the "runtime-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Native TLS using futures
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        Native TLS using futures
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
%files -n rust-async-native-tls-devel -f %{oreon_filedir}/rust-async-native-tls-devel.list

%changelog

%autochangelog
