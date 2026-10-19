%global source0_hash 30d5b2194ed13191c1999ae0704b7839fb18384fa22e49b57eeaa97d79ce40da
%bcond check 1
%global debug_package %{nil}
%global crate page_size
Name:           rust-page_size
Version:        0.6.0
Release:        1%{?dist}
Summary:        Provides an easy, fast, cross-platform way to retrieve the memory
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/page_size
Source0:        https://static.crates.io/crates/page_size/page_size-%{version}.crate
Patch:          page_size-fix-metadata-auto.diff
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
Summary:        Provides an easy, fast, cross-platform way to retrieve the memory
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Provides an easy, fast, cross-platform way to retrieve the memory
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

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
%files -n rust-page_size-devel -f %{oreon_filedir}/rust-page_size-devel.list

%changelog

%autochangelog
