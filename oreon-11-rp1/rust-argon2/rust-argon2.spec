%global source0_hash 3c3610892ee6e0cbce8ae2700349fcf8f98adb0dbfbee85aec3c9179d29cc072
%bcond check 0
%global debug_package %{nil}
%global crate argon2
Name:           rust-argon2
Version:        0.5.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/argon2
Source0:        https://static.crates.io/crates/argon2/argon2-%{version}.crate
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
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+password-hash-devel
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
BuildArch:      noarch
%description -n %{name}+password-hash-devel

This package contains library source intended for building other packages which
use the "password-hash" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+simple-devel
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
BuildArch:      noarch
%description -n %{name}+simple-devel

This package contains library source intended for building other packages which
use the "simple" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of the Argon2 password hashing function with...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-argon2-devel -f %{oreon_filedir}/rust-argon2-devel.list

%changelog

%autochangelog
