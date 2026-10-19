%global source0_hash 710e8eae58854cdc1790fcb56cca04d712a17be849eeb81da2a724bf4bae2bc4
%bcond check 0
%global debug_package %{nil}
%global crate annotate-snippets
Name:           rust-annotate-snippets0.11
Version:        0.11.5
Release:        1%{?dist}
Summary:        Library for building code annotations
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/annotate-snippets
Source0:        https://static.crates.io/crates/annotate-snippets/annotate-snippets-%{version}.crate
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
Summary:        Library for building code annotations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        Library for building code annotations
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Library for building code annotations
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+testing-colors-devel
Summary:        Library for building code annotations
BuildArch:      noarch
%description -n %{name}+testing-colors-devel

This package contains library source intended for building other packages which
use the "testing-colors" feature of the "%{crate}" crate.

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
%files -n rust-annotate-snippets0.11-devel -f %{oreon_filedir}/rust-annotate-snippets0.11-devel.list

%changelog

%autochangelog
