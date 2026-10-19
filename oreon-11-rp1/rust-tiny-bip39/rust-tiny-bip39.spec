%global source0_hash a30fd743a02bf35236f6faf99adb03089bb77e91c998dac2c2ad76bb424f668c
%bcond check 0
%global debug_package %{nil}
%global crate tiny-bip39
Name:           rust-tiny-bip39
Version:        2.0.0
Release:        1%{?dist}
Summary:        Rust implementation of BIP-0039
License:        MIT AND (MIT OR Apache-2.0)
URL:            https://crates.io/crates/tiny-bip39
Source0:        https://static.crates.io/crates/tiny-bip39/tiny-bip39-%{version}.crate
Patch:          tiny-bip39-fix-metadata-auto.diff
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
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chinese-simplified-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+chinese-simplified-devel

This package contains library source intended for building other packages which
use the "chinese-simplified" feature of the "%{crate}" crate.

%package     -n %{name}+chinese-traditional-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+chinese-traditional-devel

This package contains library source intended for building other packages which
use the "chinese-traditional" feature of the "%{crate}" crate.

%package     -n %{name}+default-langs-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+default-langs-devel

This package contains library source intended for building other packages which
use the "default-langs" feature of the "%{crate}" crate.

%package     -n %{name}+french-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+french-devel

This package contains library source intended for building other packages which
use the "french" feature of the "%{crate}" crate.

%package     -n %{name}+italian-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+italian-devel

This package contains library source intended for building other packages which
use the "italian" feature of the "%{crate}" crate.

%package     -n %{name}+japanese-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+japanese-devel

This package contains library source intended for building other packages which
use the "japanese" feature of the "%{crate}" crate.

%package     -n %{name}+korean-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+korean-devel

This package contains library source intended for building other packages which
use the "korean" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+spanish-devel
Summary:        Rust implementation of BIP-0039
BuildArch:      noarch
%description -n %{name}+spanish-devel

This package contains library source intended for building other packages which
use the "spanish" feature of the "%{crate}" crate.

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
%files -n rust-tiny-bip39-devel -f %{oreon_filedir}/rust-tiny-bip39-devel.list

%changelog

%autochangelog
