%global source0_hash e5d719de8b8f230028cf8192ae4c1b25267cd6b8a99d2747d345a70b8c81aa13
%bcond check 0
%global debug_package %{nil}
%global crate malloc_size_of
Name:           rust-malloc_size_of
Version:        0.1.1
Release:        1%{?dist}
Summary:        A an allocator-agnostic crate for measuring the heap size of a value
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/malloc_size_of
Source0:        https://static.crates.io/crates/malloc_size_of/malloc_size_of-%{version}.crate
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
Summary:        A an allocator-agnostic crate for measuring the heap size of a value
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A an allocator-agnostic crate for measuring the heap size of a value
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+void-devel
Summary:        A an allocator-agnostic crate for measuring the heap size of a value
BuildArch:      noarch
%description -n %{name}+void-devel

This package contains library source intended for building other packages which
use the "void" feature of the "%{crate}" crate.

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
%files -n rust-malloc_size_of-devel -f %{oreon_filedir}/rust-malloc_size_of-devel.list

%changelog

%autochangelog
