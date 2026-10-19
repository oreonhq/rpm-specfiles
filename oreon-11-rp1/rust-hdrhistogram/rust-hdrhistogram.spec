%global source0_hash f49d1053f4708f0af3cf9fc5bffc7e68a914a3c45becb231c80068c9c3f78bea
%bcond check 0
%global debug_package %{nil}
%global crate hdrhistogram
Name:           rust-hdrhistogram
Version:        7.6.0
Release:        1%{?dist}
Summary:        A port of HdrHistogram to Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hdrhistogram
Source0:        https://static.crates.io/crates/hdrhistogram/hdrhistogram-%{version}.crate
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
Summary:        A port of HdrHistogram to Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bench_private-devel
Summary:        A port of HdrHistogram to Rust
BuildArch:      noarch
%description -n %{name}+bench_private-devel

This package contains library source intended for building other packages which
use the "bench_private" feature of the "%{crate}" crate.

%package     -n %{name}+serialization-devel
Summary:        A port of HdrHistogram to Rust
BuildArch:      noarch
%description -n %{name}+serialization-devel

This package contains library source intended for building other packages which
use the "serialization" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        A port of HdrHistogram to Rust
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

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
%files -n rust-hdrhistogram-devel -f %{oreon_filedir}/rust-hdrhistogram-devel.list

%changelog

%autochangelog
