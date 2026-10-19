%global source0_hash 7e08d0cdb774acd1e4dac11478b1a0c0d203134b2aab0ba25eb430de9b18f8b9
%bcond check 0
%global debug_package %{nil}
%global crate aes-siv
Name:           rust-aes-siv
Version:        0.7.0
Release:        1%{?dist}
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/aes-siv
Source0:        https://static.crates.io/crates/aes-siv/aes-siv-%{version}.crate
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
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+pmac-devel
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
BuildArch:      noarch
%description -n %{name}+pmac-devel

This package contains library source intended for building other packages which
use the "pmac" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        AES-SIV Misuse-Resistant Authenticated Encryption Cipher
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

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
%files -n rust-aes-siv-devel -f %{oreon_filedir}/rust-aes-siv-devel.list

%changelog

%autochangelog
