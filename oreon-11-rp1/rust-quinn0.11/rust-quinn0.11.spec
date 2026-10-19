%global source0_hash 4051e23e9185c255a7e33ef59cdbca87a22d359052eecd22fc6b901fb37d9d11
%bcond check 1
%global debug_package %{nil}
%global crate quinn
Name:           rust-quinn0.11
Version:        0.11.12
Release:        1%{?dist}
Summary:        Versatile QUIC transport protocol implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/quinn
Source0:        https://static.crates.io/crates/quinn/quinn-%{version}.crate
Patch:          quinn-fix-metadata-auto.diff
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
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-post-quantum-test-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+__rustls-post-quantum-test-devel

This package contains library source intended for building other packages which
use the "__rustls-post-quantum-test" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-fips-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-fips-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs-fips" feature of the "%{crate}" crate.

%package     -n %{name}+bloom-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+bloom-devel

This package contains library source intended for building other packages which
use the "bloom" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+lock_tracking-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+lock_tracking-devel

This package contains library source intended for building other packages which
use the "lock_tracking" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+platform-verifier-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+platform-verifier-devel

This package contains library source intended for building other packages which
use the "platform-verifier" feature of the "%{crate}" crate.

%package     -n %{name}+qlog-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+qlog-devel

This package contains library source intended for building other packages which
use the "qlog" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-async-std-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+runtime-async-std-devel

This package contains library source intended for building other packages which
use the "runtime-async-std" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-smol-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+runtime-smol-devel

This package contains library source intended for building other packages which
use the "runtime-smol" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-tokio-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+runtime-tokio-devel

This package contains library source intended for building other packages which
use the "runtime-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-aws-lc-rs-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+rustls-aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "rustls-aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-aws-lc-rs-fips-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+rustls-aws-lc-rs-fips-devel

This package contains library source intended for building other packages which
use the "rustls-aws-lc-rs-fips" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-log-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+rustls-log-devel

This package contains library source intended for building other packages which
use the "rustls-log" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-ring-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+rustls-ring-devel

This package contains library source intended for building other packages which
use the "rustls-ring" feature of the "%{crate}" crate.

%package     -n %{name}+smol-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+smol-devel

This package contains library source intended for building other packages which
use the "smol" feature of the "%{crate}" crate.

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
%files -n rust-quinn0.11-devel -f %{oreon_filedir}/rust-quinn0.11-devel.list

%changelog

%autochangelog
