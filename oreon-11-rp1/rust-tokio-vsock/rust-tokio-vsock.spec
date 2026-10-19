%global source0_hash 8b319ef9394889dab2e1b4f0085b45ba11d0c79dc9d1a9d1afc057d009d0f1c7
%bcond check 0
%global debug_package %{nil}
%global crate tokio-vsock
Name:           rust-tokio-vsock
Version:        0.7.2
Release:        1%{?dist}
Summary:        Asynchronous Virtio socket support for Rust
License:        Apache-2.0
URL:            https://crates.io/crates/tokio-vsock
Source0:        https://static.crates.io/crates/tokio-vsock/tokio-vsock-%{version}.crate
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

%package     -n %{name}+axum08-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+axum08-devel

This package contains library source intended for building other packages which
use the "axum08" feature of the "%{crate}" crate.

%package     -n %{name}+tonic010-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic010-devel

This package contains library source intended for building other packages which
use the "tonic010" feature of the "%{crate}" crate.

%package     -n %{name}+tonic011-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic011-devel

This package contains library source intended for building other packages which
use the "tonic011" feature of the "%{crate}" crate.

%package     -n %{name}+tonic012-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic012-devel

This package contains library source intended for building other packages which
use the "tonic012" feature of the "%{crate}" crate.

%package     -n %{name}+tonic013-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic013-devel

This package contains library source intended for building other packages which
use the "tonic013" feature of the "%{crate}" crate.

%package     -n %{name}+tonic014-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic014-devel

This package contains library source intended for building other packages which
use the "tonic014" feature of the "%{crate}" crate.

%package     -n %{name}+tonic05-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic05-devel

This package contains library source intended for building other packages which
use the "tonic05" feature of the "%{crate}" crate.

%package     -n %{name}+tonic06-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic06-devel

This package contains library source intended for building other packages which
use the "tonic06" feature of the "%{crate}" crate.

%package     -n %{name}+tonic07-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic07-devel

This package contains library source intended for building other packages which
use the "tonic07" feature of the "%{crate}" crate.

%package     -n %{name}+tonic08-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic08-devel

This package contains library source intended for building other packages which
use the "tonic08" feature of the "%{crate}" crate.

%package     -n %{name}+tonic09-devel
Summary:        Asynchronous Virtio socket support for Rust
BuildArch:      noarch
%description -n %{name}+tonic09-devel

This package contains library source intended for building other packages which
use the "tonic09" feature of the "%{crate}" crate.

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
%files -n rust-tokio-vsock-devel -f %{oreon_filedir}/rust-tokio-vsock-devel.list

%changelog

%autochangelog
