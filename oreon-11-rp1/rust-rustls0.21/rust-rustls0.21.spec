%global source0_hash 3f56a14d1f48b391359b22f731fd4bd7e43c97f3c50eee276f3aa09c94784d3e
%bcond check 0
%global debug_package %{nil}
%global crate rustls
Name:           rust-rustls0.21
Version:        0.21.12
Release:        1%{?dist}
Summary:        Modern TLS library written in Rust
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
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dangerous_configuration-devel
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+dangerous_configuration-devel

This package contains library source intended for building other packages which
use the "dangerous_configuration" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+quic-devel
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+quic-devel

This package contains library source intended for building other packages which
use the "quic" feature of the "%{crate}" crate.

%package     -n %{name}+read_buf-devel
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+read_buf-devel

This package contains library source intended for building other packages which
use the "read_buf" feature of the "%{crate}" crate.

%package     -n %{name}+rustversion-devel
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+rustversion-devel

This package contains library source intended for building other packages which
use the "rustversion" feature of the "%{crate}" crate.

%package     -n %{name}+secret_extraction-devel
Summary:        Modern TLS library written in Rust
BuildArch:      noarch
%description -n %{name}+secret_extraction-devel

This package contains library source intended for building other packages which
use the "secret_extraction" feature of the "%{crate}" crate.

%package     -n %{name}+tls12-devel
Summary:        Modern TLS library written in Rust
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

%cargo_test -- --lib -- --exact --skip msgs::message_test::test_read_fuzz_corpus
%cargo_test -- --doc -- --exact --skip msgs::message_test::test_read_fuzz_corpus
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rustls0.21-devel -f %{oreon_filedir}/rust-rustls0.21-devel.list

%changelog

%autochangelog
