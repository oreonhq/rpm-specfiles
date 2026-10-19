%global source0_hash f1648a26dcf2251d444d7c405ed4e227ac08552cdfb31bfc0145266fbec4138c
%bcond check 1
%global debug_package %{nil}
%global crate rustsec
Name:           rust-rustsec
Version:        0.31.0
Release:        1%{?dist}
Summary:        Client library for the RustSec security advisory database
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/rustsec
Source0:        https://static.crates.io/crates/rustsec/rustsec-%{version}.crate
Patch:          rustsec-fix-metadata.diff
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
Summary:        Client library for the RustSec security advisory database
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dependency-tree-devel
Summary:        Client library for the RustSec security advisory database
BuildArch:      noarch
%description -n %{name}+dependency-tree-devel

This package contains library source intended for building other packages which
use the "dependency-tree" feature of the "%{crate}" crate.

%package     -n %{name}+git-devel
Summary:        Client library for the RustSec security advisory database
BuildArch:      noarch
%description -n %{name}+git-devel

This package contains library source intended for building other packages which
use the "git" feature of the "%{crate}" crate.

%package     -n %{name}+gix-curl-devel
Summary:        Client library for the RustSec security advisory database
BuildArch:      noarch
%description -n %{name}+gix-curl-devel

This package contains library source intended for building other packages which
use the "gix-curl" feature of the "%{crate}" crate.

%package     -n %{name}+gix-reqwest-devel
Summary:        Client library for the RustSec security advisory database
BuildArch:      noarch
%description -n %{name}+gix-reqwest-devel

This package contains library source intended for building other packages which
use the "gix-reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+osv-export-devel
Summary:        Client library for the RustSec security advisory database
BuildArch:      noarch
%description -n %{name}+osv-export-devel

This package contains library source intended for building other packages which
use the "osv-export" feature of the "%{crate}" crate.

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

%{cargo_test -- -- --exact %{shrink:
    --skip query_vulnerabilitie
    --skip query_vulnerabilities_with_crate_scope
    --skip enumerate_vulnerabilities
    --skip clone_into_existing_directory
    --skip happy_path
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rustsec-devel -f %{oreon_filedir}/rust-rustsec-devel.list

%changelog

%autochangelog
