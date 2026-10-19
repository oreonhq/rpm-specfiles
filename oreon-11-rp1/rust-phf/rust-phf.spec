%global source0_hash 010378780309880b08997fae13be7834dba947d36393bd372f2b1556deb2a2f6
%bcond check 0
%global debug_package %{nil}
%global crate phf
Name:           rust-phf
Version:        0.14.0
Release:        1%{?dist}
Summary:        Runtime support for perfect hash function data structures
License:        MIT
URL:            https://crates.io/crates/phf
Source0:        https://static.crates.io/crates/phf/phf-%{version}.crate
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
Summary:        Runtime support for perfect hash function data structures
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Runtime support for perfect hash function data structures
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+phf_macros-devel
Summary:        Runtime support for perfect hash function data structures
BuildArch:      noarch
%description -n %{name}+phf_macros-devel

This package contains library source intended for building other packages which
use the "phf_macros" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Runtime support for perfect hash function data structures
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Runtime support for perfect hash function data structures
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+uncased-devel
Summary:        Runtime support for perfect hash function data structures
BuildArch:      noarch
%description -n %{name}+uncased-devel

This package contains library source intended for building other packages which
use the "uncased" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        Runtime support for perfect hash function data structures
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

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
%files -n rust-phf-devel -f %{oreon_filedir}/rust-phf-devel.list

%changelog

%autochangelog
