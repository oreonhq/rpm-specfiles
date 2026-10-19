%global source0_hash b9d6cf87adf719ddf43a805e92c6870a531aedda35ff640442cbaf8674e141e1
%bcond check 1
%global debug_package %{nil}
%global crate crypto_secretbox
Name:           rust-crypto_secretbox
Version:        0.1.1
Release:        1%{?dist}
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/crypto_secretbox
Source0:        https://static.crates.io/crates/crypto_secretbox/crypto_secretbox-%{version}.crate
Patch:          crypto_secretbox-fix-metadata.diff
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
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+chacha20-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+chacha20-devel

This package contains library source intended for building other packages which
use the "chacha20" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+salsa20-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+salsa20-devel

This package contains library source intended for building other packages which
use the "salsa20" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Implementation of the XSalsa20Poly1305 and XChaCha20Poly1305 ciphers
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-crypto_secretbox-devel -f %{oreon_filedir}/rust-crypto_secretbox-devel.list

%changelog

%autochangelog
