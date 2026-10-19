%global source0_hash 13f6de320895f42e6e081abb5c7983bedcf0b6d0ff9323de0d33f620c8ac1199
%bcond check 0
%global debug_package %{nil}
%global crate cxx
Name:           rust-cxx
Version:        1.0.202
Release:        1%{?dist}
Summary:        Safe interop between Rust and C++
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cxx
Source0:        https://static.crates.io/crates/cxx/cxx-%{version}.crate
Patch:          cxx-fix-metadata.diff
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
Summary:        Safe interop between Rust and C++
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Safe interop between Rust and C++
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+c++14-devel
Summary:        Safe interop between Rust and C++
BuildArch:      noarch
%description -n %{name}+c++14-devel

This package contains library source intended for building other packages which
use the "c++14" feature of the "%{crate}" crate.

%package     -n %{name}+c++17-devel
Summary:        Safe interop between Rust and C++
BuildArch:      noarch
%description -n %{name}+c++17-devel

This package contains library source intended for building other packages which
use the "c++17" feature of the "%{crate}" crate.

%package     -n %{name}+c++20-devel
Summary:        Safe interop between Rust and C++
BuildArch:      noarch
%description -n %{name}+c++20-devel

This package contains library source intended for building other packages which
use the "c++20" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safe interop between Rust and C++
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-cxx-devel -f %{oreon_filedir}/rust-cxx-devel.list

%changelog

%autochangelog
