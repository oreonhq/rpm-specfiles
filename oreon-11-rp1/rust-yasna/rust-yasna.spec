%global source2_hash 2a7df90e60fd5512b8bca35d3ce90e068f21c52d962855053fd1d9e2e7ca0f16
%global source1_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash e17bb3549cc1321ae1296b9cdc2698e2b6cb1992adfa19a8c72e5b7a738f44cd
%bcond check 0
%global debug_package %{nil}
%global crate yasna
Name:           rust-yasna
Version:        0.5.2
Release:        1%{?dist}
Summary:        ASN.1 library for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/yasna
Source0:        https://static.crates.io/crates/yasna/yasna-%{version}.crate
Source1:        https://github.com/qnighy/yasna.rs/raw/yasna-0.5.0/LICENSE-APACHE
Source2:        https://github.com/qnighy/yasna.rs/raw/yasna-0.5.0/LICENSE-MIT
Patch:          yasna-fix-metadata.diff
Patch2:         https://github.com/qnighy/yasna.rs/pull/73.patch
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
Summary:        ASN.1 library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-devel
Summary:        ASN.1 library for Rust
BuildArch:      noarch
%description -n %{name}+bit-vec-devel

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        ASN.1 library for Rust
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        ASN.1 library for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        ASN.1 library for Rust
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-yasna-devel -f %{oreon_filedir}/rust-yasna-devel.list

%changelog

%autochangelog
