%global source0_hash c6f140db74548f7c9d7cce60912c9ac414e74df5e718dc947d514b051b42f3f4
%bcond check 0
%global debug_package %{nil}
%global crate rustfft
Name:           rust-rustfft
Version:        6.4.0
Release:        1%{?dist}
Summary:        High-performance FFT library written in pure Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustfft
Source0:        https://static.crates.io/crates/rustfft/rustfft-%{version}.crate
Patch:          rustfft-fix-metadata.diff
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
Summary:        High-performance FFT library written in pure Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+avx-devel
Summary:        High-performance FFT library written in pure Rust
BuildArch:      noarch
%description -n %{name}+avx-devel

This package contains library source intended for building other packages which
use the "avx" feature of the "%{crate}" crate.

%package     -n %{name}+neon-devel
Summary:        High-performance FFT library written in pure Rust
BuildArch:      noarch
%description -n %{name}+neon-devel

This package contains library source intended for building other packages which
use the "neon" feature of the "%{crate}" crate.

%package     -n %{name}+sse-devel
Summary:        High-performance FFT library written in pure Rust
BuildArch:      noarch
%description -n %{name}+sse-devel

This package contains library source intended for building other packages which
use the "sse" feature of the "%{crate}" crate.

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
%files -n rust-rustfft-devel -f %{oreon_filedir}/rust-rustfft-devel.list

%changelog

%autochangelog
