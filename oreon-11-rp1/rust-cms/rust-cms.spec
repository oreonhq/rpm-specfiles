%global source11_hash ae9baa7beea910273c2f384c2a6b721fb7bd02bda3436074a1072e4ee689f985
%global source10_hash a9040321c3712d8fd0b09cf52b17445de04a23a10165049ae187cd39e5c86be5
%global source0_hash 7b77c319abfd5219629c45c34c89ba945ed3c5e49fcde9d16b6c3885f118a730
%bcond check 1
%global debug_package %{nil}
%global crate cms
Name:           rust-cms
Version:        0.2.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/cms
Source0:        https://static.crates.io/crates/cms/cms-%{version}.crate
Source10:       https://raw.githubusercontent.com/RustCrypto/formats/refs/heads/master/cms/LICENSE-APACHE
Source11:       https://raw.githubusercontent.com/RustCrypto/formats/refs/heads/master/cms/LICENSE-MIT
Patch:          cms-fix-metadata.diff
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
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aes-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+aes-devel

This package contains library source intended for building other packages which
use the "aes" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+builder-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+builder-devel

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

%package     -n %{name}+cbc-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+cbc-devel

This package contains library source intended for building other packages which
use the "cbc" feature of the "%{crate}" crate.

%package     -n %{name}+cipher-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+cipher-devel

This package contains library source intended for building other packages which
use the "cipher" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+rsa-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+rsa-devel

This package contains library source intended for building other packages which
use the "rsa" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+sha3-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+sha3-devel

This package contains library source intended for building other packages which
use the "sha3" feature of the "%{crate}" crate.

%package     -n %{name}+signature-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+signature-devel

This package contains library source intended for building other packages which
use the "signature" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of the Cryptographic Message Syntax
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' .
cp -p '%{SOURCE11}' .
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
%files -n rust-cms-devel -f %{oreon_filedir}/rust-cms-devel.list

%changelog

%autochangelog
