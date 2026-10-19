%global source0_hash 0d4770b8024672c1101b3f6733eab95b18007dbe0847a8afe341fcf79e06043f
%bcond check 0
%global debug_package %{nil}
%global crate tokio-socks
Name:           rust-tokio-socks
Version:        0.5.2
Release:        1%{?dist}
Summary:        Asynchronous SOCKS proxy support for Rust
License:        MIT
URL:            https://crates.io/crates/tokio-socks
Source0:        https://static.crates.io/crates/tokio-socks/tokio-socks-%{version}.crate
Patch:          tokio-socks-fix-metadata.diff
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
Summary:        Asynchronous SOCKS proxy support for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Asynchronous SOCKS proxy support for Rust
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Asynchronous SOCKS proxy support for Rust
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tor-devel
Summary:        Asynchronous SOCKS proxy support for Rust
BuildArch:      noarch
%description -n %{name}+tor-devel

This package contains library source intended for building other packages which
use the "tor" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tokio-socks-devel -f %{oreon_filedir}/rust-tokio-socks-devel.list

%changelog

%autochangelog
