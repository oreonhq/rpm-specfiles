%global source0_hash 8cc2c5017e4b43d5995dcea317bc46c1e09404c0a9664d2908f7f02dfe943d75
%bcond check 0
%global debug_package %{nil}
%global crate quinn
Name:           rust-quinn
Version:        0.10.2
Release:        1%{?dist}
Summary:        Versatile QUIC transport protocol implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/quinn
Source0:        https://static.crates.io/crates/quinn/quinn-%{version}.crate
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

%package     -n %{name}+native-certs-devel
Summary:        Versatile QUIC transport protocol implementation
BuildArch:      noarch
%description -n %{name}+native-certs-devel

This package contains library source intended for building other packages which
use the "native-certs" feature of the "%{crate}" crate.

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

%package     -n %{name}+tls-rustls-devel
Summary:        Versatile QUIC transport protocol implementation
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
%files -n rust-quinn-devel -f %{oreon_filedir}/rust-quinn-devel.list

%changelog

%autochangelog
