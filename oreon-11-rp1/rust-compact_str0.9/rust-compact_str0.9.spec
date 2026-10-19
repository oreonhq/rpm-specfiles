%global source0_hash 9dfdd1c2274d9aa354115b09dc9a901d6c5576818cdf70d14cae2bdb47df00ab
%bcond check 0
%global debug_package %{nil}
%global crate compact_str
Name:           rust-compact_str0.9
Version:        0.9.1
Release:        1%{?dist}
Summary:        A memory efficient string type that transparently stores strings on t...
License:        MIT
URL:            https://crates.io/crates/compact_str
Source0:        https://static.crates.io/crates/compact_str/compact_str-%{version}.crate
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
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+borsh-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+borsh-devel

This package contains library source intended for building other packages which
use the "borsh" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+diesel-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+diesel-devel

This package contains library source intended for building other packages which
use the "diesel" feature of the "%{crate}" crate.

%package     -n %{name}+markup-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+markup-devel

This package contains library source intended for building other packages which
use the "markup" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+sqlx-devel

This package contains library source intended for building other packages which
use the "sqlx" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-mysql-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+sqlx-mysql-devel

This package contains library source intended for building other packages which
use the "sqlx-mysql" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-postgres-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+sqlx-postgres-devel

This package contains library source intended for building other packages which
use the "sqlx-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-sqlite-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+sqlx-sqlite-devel

This package contains library source intended for building other packages which
use the "sqlx-sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A memory efficient string type that transparently stores strings on t...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        A memory efficient string type that transparently stores strings on t...
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
%files -n rust-compact_str0.9-devel -f %{oreon_filedir}/rust-compact_str0.9-devel.list

%changelog

%autochangelog
