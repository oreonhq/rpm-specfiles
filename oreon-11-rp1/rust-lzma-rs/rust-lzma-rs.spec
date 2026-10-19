%global source0_hash 297e814c836ae64db86b36cf2a557ba54368d03f6afcd7d947c266692f71115e
%bcond check 1
%global debug_package %{nil}
%global crate lzma-rs
Name:           rust-lzma-rs
Version:        0.3.0
Release:        1%{?dist}
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust
License:        MIT
URL:            https://crates.io/crates/lzma-rs
Source0:        https://static.crates.io/crates/lzma-rs/lzma-rs-%{version}.crate
Patch:          lzma-rs-fix-metadata.diff
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
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+enable_logging-devel
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust
BuildArch:      noarch
%description -n %{name}+enable_logging-devel

This package contains library source intended for building other packages which
use the "enable_logging" feature of the "%{crate}" crate.

%package     -n %{name}+env_logger-devel
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust
BuildArch:      noarch
%description -n %{name}+env_logger-devel

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+raw_decoder-devel
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust
BuildArch:      noarch
%description -n %{name}+raw_decoder-devel

This package contains library source intended for building other packages which
use the "raw_decoder" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Codec for LZMA, LZMA2 and XZ written in pure Rust
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

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
%files -n rust-lzma-rs-devel -f %{oreon_filedir}/rust-lzma-rs-devel.list

%changelog

%autochangelog
