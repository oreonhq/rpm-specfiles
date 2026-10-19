%global source0_hash 141bf7dfde2fbc246bfd3fe12f2455aa24b0fbd9af535d8c86c7bd1381ff2b1a
%bcond check 0
%global debug_package %{nil}
%global crate quinn-proto
Name:           rust-quinn-proto
Version:        0.10.6
Release:        1%{?dist}
Summary:        State machine for the QUIC transport protocol
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/quinn-proto
Source0:        https://static.crates.io/crates/quinn-proto/quinn-proto-%{version}.crate
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
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+native-certs-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+native-certs-devel

This package contains library source intended for building other packages which
use the "native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+tls-rustls-devel

This package contains library source intended for building other packages which
use the "tls-rustls" feature of the "%{crate}" crate.

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
%files -n rust-quinn-proto-devel -f %{oreon_filedir}/rust-quinn-proto-devel.list

%changelog

%autochangelog
