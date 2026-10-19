%global source0_hash ecbdfe44b1bd960b68170b417450a628c43f7cf56bb3c5317e61cb230ee7f226
%bcond check 0
%global debug_package %{nil}
%global crate lz4_flex
Name:           rust-lz4_flex
Version:        0.14.0
Release:        1%{?dist}
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
License:        MIT
URL:            https://crates.io/crates/lz4_flex
Source0:        https://static.crates.io/crates/lz4_flex/lz4_flex-%{version}.crate
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
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+checked-decode-devel
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+checked-decode-devel

This package contains library source intended for building other packages which
use the "checked-decode" feature of the "%{crate}" crate.

%package     -n %{name}+frame-devel
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+frame-devel

This package contains library source intended for building other packages which
use the "frame" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+safe-decode-devel
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+safe-decode-devel

This package contains library source intended for building other packages which
use the "safe-decode" feature of the "%{crate}" crate.

%package     -n %{name}+safe-encode-devel
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+safe-encode-devel

This package contains library source intended for building other packages which
use the "safe-encode" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+twox-hash-devel
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default.
BuildArch:      noarch
%description -n %{name}+twox-hash-devel

This package contains library source intended for building other packages which
use the "twox-hash" feature of the "%{crate}" crate.

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
%files -n rust-lz4_flex-devel -f %{oreon_filedir}/rust-lz4_flex-devel.list

%changelog

%autochangelog
