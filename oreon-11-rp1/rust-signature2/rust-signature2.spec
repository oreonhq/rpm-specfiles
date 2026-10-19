%global source0_hash 77549399552de45a898a580c1b41d445bf730df867cc44e6c0233bbc4b8329de
%bcond check 0
%global debug_package %{nil}
%global crate signature
Name:           rust-signature2
Version:        2.2.0
Release:        1%{?dist}
Summary:        Traits for cryptographic signature algorithms (e.g. ECDSA, Ed25519)
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/signature
Source0:        https://static.crates.io/crates/signature/signature-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Traits for cryptographic signature algorithms (e.g. ECDSA, Ed25519)
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Traits for cryptographic signature algorithms (e.g. ECDSA, Ed25519)
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        Traits for cryptographic signature algorithms (e.g. ECDSA, Ed25519)
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Traits for cryptographic signature algorithms (e.g. ECDSA, Ed25519)
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Traits for cryptographic signature algorithms (e.g. ECDSA, Ed25519)
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-signature2-devel -f %{oreon_filedir}/rust-signature2-devel.list

%changelog

%autochangelog
