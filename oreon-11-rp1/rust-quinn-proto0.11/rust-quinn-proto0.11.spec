%global source0_hash 0e750cca55fe4f0439a15d0bb529da9651e79993e8e72c61a899a36d462befbe
%bcond check 0
%global debug_package %{nil}
%global crate quinn-proto
Name:           rust-quinn-proto0.11
Version:        0.11.19
Release:        1%{?dist}
Summary:        State machine for the QUIC transport protocol
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/quinn-proto
Source0:        https://static.crates.io/crates/quinn-proto/quinn-proto-%{version}.crate
Patch:          quinn-proto-fix-metadata-auto.diff
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

%package     -n %{name}+__rustls-post-quantum-test-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+__rustls-post-quantum-test-devel

This package contains library source intended for building other packages which
use the "__rustls-post-quantum-test" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-fips-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-fips-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs-fips" feature of the "%{crate}" crate.

%package     -n %{name}+bloom-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+bloom-devel

This package contains library source intended for building other packages which
use the "bloom" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+platform-verifier-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+platform-verifier-devel

This package contains library source intended for building other packages which
use the "platform-verifier" feature of the "%{crate}" crate.

%package     -n %{name}+qlog-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+qlog-devel

This package contains library source intended for building other packages which
use the "qlog" feature of the "%{crate}" crate.

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

%package     -n %{name}+rustls-aws-lc-rs-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+rustls-aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "rustls-aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-aws-lc-rs-fips-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+rustls-aws-lc-rs-fips-devel

This package contains library source intended for building other packages which
use the "rustls-aws-lc-rs-fips" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-log-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+rustls-log-devel

This package contains library source intended for building other packages which
use the "rustls-log" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-ring-devel
Summary:        State machine for the QUIC transport protocol
BuildArch:      noarch
%description -n %{name}+rustls-ring-devel

This package contains library source intended for building other packages which
use the "rustls-ring" feature of the "%{crate}" crate.

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
%files -n rust-quinn-proto0.11-devel -f %{oreon_filedir}/rust-quinn-proto0.11-devel.list

%changelog

%autochangelog
