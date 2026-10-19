%global source0_hash be176f1a57ce4e3d31c1a166222d9768de5954f811601fb7ca06fc8203905ce1
%bcond check 0
%global debug_package %{nil}
%global crate sha3
Name:           rust-sha30.11
Version:        0.11.0
Release:        1%{?dist}
Summary:        Implementation of the SHA-3 family of cryptographic hash algorithms
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha3
Source0:        https://static.crates.io/crates/sha3/sha3-%{version}.crate
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
Summary:        Implementation of the SHA-3 family of cryptographic hash algorithms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Implementation of the SHA-3 family of cryptographic hash algorithms
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        Implementation of the SHA-3 family of cryptographic hash algorithms
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Implementation of the SHA-3 family of cryptographic hash algorithms
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
%files -n rust-sha30.11-devel -f %{oreon_filedir}/rust-sha30.11-devel.list

%changelog

%autochangelog
