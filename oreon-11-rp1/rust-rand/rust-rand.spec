%global source0_hash 65c9fb96cbc91e3478eaae79a69fcd3f1ae4ad052e471fe6732fff548984b4af
%bcond check 0
%global debug_package %{nil}
%global crate rand
Name:           rust-rand
Version:        0.10.3
Release:        1%{?dist}
Summary:        Random number generators and other randomness functionality
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand
Source0:        https://static.crates.io/crates/rand/rand-%{version}.crate
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
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+chacha-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+chacha-devel

This package contains library source intended for building other packages which
use the "chacha" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+simd_support-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+simd_support-devel

This package contains library source intended for building other packages which
use the "simd_support" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+std_rng-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+std_rng-devel

This package contains library source intended for building other packages which
use the "std_rng" feature of the "%{crate}" crate.

%package     -n %{name}+sys_rng-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+sys_rng-devel

This package contains library source intended for building other packages which
use the "sys_rng" feature of the "%{crate}" crate.

%package     -n %{name}+thread_rng-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+thread_rng-devel

This package contains library source intended for building other packages which
use the "thread_rng" feature of the "%{crate}" crate.

%package     -n %{name}+unbiased-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+unbiased-devel

This package contains library source intended for building other packages which
use the "unbiased" feature of the "%{crate}" crate.

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
%files -n rust-rand-devel -f %{oreon_filedir}/rust-rand-devel.list

%changelog

%autochangelog
