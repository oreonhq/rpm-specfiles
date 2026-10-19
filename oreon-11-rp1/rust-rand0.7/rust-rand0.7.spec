%global source0_hash 6a6b1679d49b24bbfe0c803429aa1874472f50d9b363131f0e89fc356b544d03
%bcond_with check
%global debug_package %{nil}
%global crate rand
Name:           rust-rand0.7
Version:        0.7.3
Release:        1%{?dist}
Summary:        Random number generators and other randomness functionality
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand
Source0:        https://static.crates.io/crates/rand/rand-%{version}.crate
Patch:          rand-fix-metadata-auto.diff
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

%package     -n %{name}+getrandom-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom_package-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+getrandom_package-devel

This package contains library source intended for building other packages which
use the "getrandom_package" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+rand_pcg-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+rand_pcg-devel

This package contains library source intended for building other packages which
use the "rand_pcg" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

%package     -n %{name}+small_rng-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+small_rng-devel

This package contains library source intended for building other packages which
use the "small_rng" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
%files -n rust-rand0.7-devel -f %{oreon_filedir}/rust-rand0.7-devel.list

%changelog

%autochangelog
