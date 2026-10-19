%global source0_hash 65c35e4b699c7e15ccbe7ee35c005e4fc0a278d22238a2857e6ce2dadeda1b06
%bcond check 0
%global debug_package %{nil}
%global crate chacha20
Name:           rust-chacha20
Version:        0.10.2
Release:        1%{?dist}
Summary:        The ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chacha20
Source0:        https://static.crates.io/crates/chacha20/chacha20-%{version}.crate
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
Summary:        The ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-devel
Summary:        The ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using
BuildArch:      noarch
%description -n %{name}+legacy-devel

This package contains library source intended for building other packages which
use the "legacy" feature of the "%{crate}" crate.

%package     -n %{name}+rng-devel
Summary:        The ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using
BuildArch:      noarch
%description -n %{name}+rng-devel

This package contains library source intended for building other packages which
use the "rng" feature of the "%{crate}" crate.

%package     -n %{name}+xchacha-devel
Summary:        The ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using
BuildArch:      noarch
%description -n %{name}+xchacha-devel

This package contains library source intended for building other packages which
use the "xchacha" feature of the "%{crate}" crate.

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
%files -n rust-chacha20-devel -f %{oreon_filedir}/rust-chacha20-devel.list

%changelog

%autochangelog
