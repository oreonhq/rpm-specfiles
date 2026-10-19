%global source0_hash 5d1126dcf58e93cee7d098dbda643b5f92ed724f1f6a63007c1116eed6700c81
%bcond check 0
%global debug_package %{nil}
%global crate rustls
Name:           rust-rustls0.18
Version:        0.18.1
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
%files -n rust-rustls0.18-devel -f %{oreon_filedir}/rust-rustls0.18-devel.list

%changelog

%autochangelog
