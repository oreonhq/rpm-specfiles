%global source0_hash e6505efef05804732ed8a3f2d4f279429eb485bd69d5b0cc6b19cc02005cda16
%bcond check 0
%global debug_package %{nil}
%global crate similar
Name:           rust-similar
Version:        3.1.1
Release:        1%{?dist}
Summary:        A diff library for Rust
License:        Apache-2.0
URL:            https://crates.io/crates/similar
Source0:        https://static.crates.io/crates/similar/similar-%{version}.crate
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
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+inline-devel
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+inline-devel

This package contains library source intended for building other packages which
use the "inline" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+text-devel
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+text-devel

This package contains library source intended for building other packages which
use the "text" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%package     -n %{name}+wasm32_web_time-devel
Summary:        A diff library for Rust
BuildArch:      noarch
%description -n %{name}+wasm32_web_time-devel

This package contains library source intended for building other packages which
use the "wasm32_web_time" feature of the "%{crate}" crate.

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
%files -n rust-similar-devel -f %{oreon_filedir}/rust-similar-devel.list

%changelog

%autochangelog
