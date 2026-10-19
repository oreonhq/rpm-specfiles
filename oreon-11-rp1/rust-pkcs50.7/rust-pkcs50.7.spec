%global source0_hash e847e2c91a18bfa887dd028ec33f2fe6f25db77db3619024764914affe8b69a6
%bcond check 0
%global debug_package %{nil}
%global crate pkcs5
Name:           rust-pkcs50.7
Version:        0.7.1
Release:        1%{?dist}
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pkcs5
Source0:        https://static.crates.io/crates/pkcs5/pkcs5-%{version}.crate
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

%package     -n %{name}+3des-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+3des-devel

This package contains library source intended for building other packages which
use the "3des" feature of the "%{crate}" crate.

%package     -n %{name}+aes-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+aes-devel

This package contains library source intended for building other packages which
use the "aes" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+cbc-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+cbc-devel

This package contains library source intended for building other packages which
use the "cbc" feature of the "%{crate}" crate.

%package     -n %{name}+des-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+des-devel

This package contains library source intended for building other packages which
use the "des" feature of the "%{crate}" crate.

%package     -n %{name}+des-insecure-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+des-insecure-devel

This package contains library source intended for building other packages which
use the "des-insecure" feature of the "%{crate}" crate.

%package     -n %{name}+pbes2-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+pbes2-devel

This package contains library source intended for building other packages which
use the "pbes2" feature of the "%{crate}" crate.

%package     -n %{name}+pbkdf2-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+pbkdf2-devel

This package contains library source intended for building other packages which
use the "pbkdf2" feature of the "%{crate}" crate.

%package     -n %{name}+scrypt-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+scrypt-devel

This package contains library source intended for building other packages which
use the "scrypt" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-insecure-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+sha1-insecure-devel

This package contains library source intended for building other packages which
use the "sha1-insecure" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5:
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

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
%files -n rust-pkcs50.7-devel -f %{oreon_filedir}/rust-pkcs50.7-devel.list

%changelog

%autochangelog
