%global source0_hash 0d41d731c7d2f962d1ccc364cec258de3c0e93b38c2fb3ba97ac74513048d634
%bcond check 0
%global debug_package %{nil}
%global crate rustls
Name:           rust-rustls
Version:        0.23.45
Release:        1%{?dist}
Summary:        Rustls is a modern TLS library written in Rust.
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/rustls
Source0:        https://static.crates.io/crates/rustls/rustls-%{version}.crate
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
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dangerous_configuration-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+dangerous_configuration-devel

This package contains library source intended for building other packages which
use the "dangerous_configuration" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+quic-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+quic-devel

This package contains library source intended for building other packages which
use the "quic" feature of the "%{crate}" crate.

%package     -n %{name}+read_buf-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+read_buf-devel

This package contains library source intended for building other packages which
use the "read_buf" feature of the "%{crate}" crate.

%package     -n %{name}+secret_extraction-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+secret_extraction-devel

This package contains library source intended for building other packages which
use the "secret_extraction" feature of the "%{crate}" crate.

%package     -n %{name}+tls12-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+tls12-devel

This package contains library source intended for building other packages which
use the "tls12" feature of the "%{crate}" crate.

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
%files -n rust-rustls-devel -f %{oreon_filedir}/rust-rustls-devel.list

%changelog

%autochangelog
