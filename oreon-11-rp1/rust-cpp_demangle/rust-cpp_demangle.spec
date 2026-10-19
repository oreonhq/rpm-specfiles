%global source0_hash 0667304c32ea56cb4cd6d2d7c0cfe9a2f8041229db8c033af7f8d69492429def
%bcond check 0
%global debug_package %{nil}
%global crate cpp_demangle
Name:           rust-cpp_demangle
Version:        0.5.1
Release:        1%{?dist}
Summary:        A crate for demangling C++ symbols
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cpp_demangle
Source0:        https://static.crates.io/crates/cpp_demangle/cpp_demangle-%{version}.crate
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
Summary:        A crate for demangling C++ symbols
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+afl-devel
Summary:        A crate for demangling C++ symbols
BuildArch:      noarch
%description -n %{name}+afl-devel

This package contains library source intended for building other packages which
use the "afl" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A crate for demangling C++ symbols
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+fuzz-devel
Summary:        A crate for demangling C++ symbols
BuildArch:      noarch
%description -n %{name}+fuzz-devel

This package contains library source intended for building other packages which
use the "fuzz" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        A crate for demangling C++ symbols
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+run_libiberty_tests-devel
Summary:        A crate for demangling C++ symbols
BuildArch:      noarch
%description -n %{name}+run_libiberty_tests-devel

This package contains library source intended for building other packages which
use the "run_libiberty_tests" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A crate for demangling C++ symbols
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
%files -n rust-cpp_demangle-devel -f %{oreon_filedir}/rust-cpp_demangle-devel.list

%changelog

%autochangelog
