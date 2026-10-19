%global source0_hash ce2dc9ee5f88d11e0beb842c88b33c8a5cf0d1329c4b19494af42b07dbfe8896
%bcond check 0
%global debug_package %{nil}
%global crate cbc
Name:           rust-cbc
Version:        0.2.1
Release:        1%{?dist}
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cbc
Source0:        https://static.crates.io/crates/cbc/cbc-%{version}.crate
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
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+block-padding-devel
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
BuildArch:      noarch
%description -n %{name}+block-padding-devel

This package contains library source intended for building other packages which
use the "block-padding" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation
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
%files -n rust-cbc-devel -f %{oreon_filedir}/rust-cbc-devel.list

%changelog

%autochangelog
