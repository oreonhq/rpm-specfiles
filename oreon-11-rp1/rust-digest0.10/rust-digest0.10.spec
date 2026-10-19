%global source0_hash 9ed9a281f7bc9b7576e61468ba615a66a5c8cfdff42420a70aa82701a3b1e292
%bcond check 1
%global debug_package %{nil}
%global crate digest
Name:           rust-digest0.10
Version:        0.10.7
Release:        1%{?dist}
Summary:        Traits for cryptographic hash functions and message authentication codes
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/digest
Source0:        https://static.crates.io/crates/digest/digest-%{version}.crate
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
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+blobby-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+blobby-devel

This package contains library source intended for building other packages which
use the "blobby" feature of the "%{crate}" crate.

%package     -n %{name}+block-buffer-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+block-buffer-devel

This package contains library source intended for building other packages which
use the "block-buffer" feature of the "%{crate}" crate.

%package     -n %{name}+const-oid-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+const-oid-devel

This package contains library source intended for building other packages which
use the "const-oid" feature of the "%{crate}" crate.

%package     -n %{name}+core-api-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+core-api-devel

This package contains library source intended for building other packages which
use the "core-api" feature of the "%{crate}" crate.

%package     -n %{name}+dev-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+dev-devel

This package contains library source intended for building other packages which
use the "dev" feature of the "%{crate}" crate.

%package     -n %{name}+mac-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+mac-devel

This package contains library source intended for building other packages which
use the "mac" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+subtle-devel
Summary:        Traits for cryptographic hash functions and message authentication codes
BuildArch:      noarch
%description -n %{name}+subtle-devel

This package contains library source intended for building other packages which
use the "subtle" feature of the "%{crate}" crate.

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
%files -n rust-digest0.10-devel -f %{oreon_filedir}/rust-digest0.10-devel.list

%changelog

%autochangelog
