%global source0_hash 957228ad12042ee839f93c8f257b62b4c0ab5eaae1d4fa60de53b27c9d7c5046
%bcond check 1
%global debug_package %{nil}
%global crate moka
Name:           rust-moka
Version:        0.12.15
Release:        1%{?dist}
Summary:        Fast and concurrent cache library inspired by Java Caffeine
License:        (MIT OR Apache-2.0) AND Apache-2.0
URL:            https://crates.io/crates/moka
Source0:        https://static.crates.io/crates/moka/moka-%{version}.crate
Patch:          moka-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%if 0%{?__isa_bits} == 32
# Avoid memory (address-space) exhaustion on 32-bit architectures when
# compiling the moka crate for the tests.
# https://doc.rust-lang.org/rustc/codegen-options/index.html#debuginfo
%global rustflags_debuginfo 1
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Fast and concurrent cache library inspired by Java Caffeine
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+future-devel
Summary:        Fast and concurrent cache library inspired by Java Caffeine
BuildArch:      noarch
%description -n %{name}+future-devel

This package contains library source intended for building other packages which
use the "future" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Fast and concurrent cache library inspired by Java Caffeine
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+quanta-devel
Summary:        Fast and concurrent cache library inspired by Java Caffeine
BuildArch:      noarch
%description -n %{name}+quanta-devel

This package contains library source intended for building other packages which
use the "quanta" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        Fast and concurrent cache library inspired by Java Caffeine
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f future,sync
%install
%cargo_install -f future,sync
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f future,sync
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-moka-devel -f %{oreon_filedir}/rust-moka-devel.list

%changelog

%autochangelog
