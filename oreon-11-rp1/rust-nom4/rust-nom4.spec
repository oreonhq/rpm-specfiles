%global source0_hash 2ad2a91a8e869eeb30b9cb3119ae87773a8f4ae617f41b1eb9c154b2905f7bd6
%bcond check 0
%global debug_package %{nil}
%global crate nom
Name:           rust-nom4
Version:        4.2.3
Release:        1%{?dist}
Summary:        A byte-oriented, zero-copy, parser combinators library
License:        MIT
URL:            https://crates.io/crates/nom
Source0:        https://static.crates.io/crates/nom/nom-%{version}.crate
Patch:          nom-fix-metadata.diff
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
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+lazy_static-devel

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+regexp-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+regexp-devel

This package contains library source intended for building other packages which
use the "regexp" feature of the "%{crate}" crate.

%package     -n %{name}+regexp_macros-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+regexp_macros-devel

This package contains library source intended for building other packages which
use the "regexp_macros" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+verbose-errors-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+verbose-errors-devel

This package contains library source intended for building other packages which
use the "verbose-errors" feature of the "%{crate}" crate.

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
%files -n rust-nom4-devel -f %{oreon_filedir}/rust-nom4-devel.list

%changelog

%autochangelog
