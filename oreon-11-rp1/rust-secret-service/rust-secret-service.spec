%global source0_hash 5107b24b91445dd2aa449a258a1807b63240942157292354dc5bfdbeb8bc6db8
%bcond check 0
%global debug_package %{nil}
%global crate secret-service
Name:           rust-secret-service
Version:        5.2.0
Release:        1%{?dist}
Summary:        Library to interface with Secret Service API
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/secret-service
Source0:        https://static.crates.io/crates/secret-service/secret-service-%{version}.crate
Patch:          secret-service-fix-metadata.diff
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
Summary:        Library to interface with Secret Service API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-openssl-devel
Summary:        Library to interface with Secret Service API
BuildArch:      noarch
%description -n %{name}+crypto-openssl-devel

This package contains library source intended for building other packages which
use the "crypto-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-rust-devel
Summary:        Library to interface with Secret Service API
BuildArch:      noarch
%description -n %{name}+crypto-rust-devel

This package contains library source intended for building other packages which
use the "crypto-rust" feature of the "%{crate}" crate.

%package     -n %{name}+rt-async-io-crypto-openssl-devel
Summary:        Library to interface with Secret Service API
BuildArch:      noarch
%description -n %{name}+rt-async-io-crypto-openssl-devel

This package contains library source intended for building other packages which
use the "rt-async-io-crypto-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+rt-async-io-crypto-rust-devel
Summary:        Library to interface with Secret Service API
BuildArch:      noarch
%description -n %{name}+rt-async-io-crypto-rust-devel

This package contains library source intended for building other packages which
use the "rt-async-io-crypto-rust" feature of the "%{crate}" crate.

%package     -n %{name}+rt-tokio-crypto-openssl-devel
Summary:        Library to interface with Secret Service API
BuildArch:      noarch
%description -n %{name}+rt-tokio-crypto-openssl-devel

This package contains library source intended for building other packages which
use the "rt-tokio-crypto-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+rt-tokio-crypto-rust-devel
Summary:        Library to interface with Secret Service API
BuildArch:      noarch
%description -n %{name}+rt-tokio-crypto-rust-devel

This package contains library source intended for building other packages which
use the "rt-tokio-crypto-rust" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -r -i 's@^([[:blank:]]*)(#\[test_with::)@\1//\2@' \
src/blocking/mod.rs src/lib.rs
%oreon_vendor_cargo
%build

%cargo_build -f rt-tokio-crypto-rust
%install
%cargo_install -f rt-tokio-crypto-rust
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f rt-tokio-crypto-rust
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-secret-service-devel -f %{oreon_filedir}/rust-secret-service-devel.list

%changelog

%autochangelog
