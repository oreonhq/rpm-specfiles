%global source0_hash 72069c3113ab32ab29e5584db3c6ec55d416895e60715417b5b883a357c3e471
%bcond check 0
%global debug_package %{nil}
%global crate widestring
Name:           rust-widestring
Version:        1.2.1
Release:        1%{?dist}
Summary:        A wide string Rust library for converting to and from wide strings, s...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/widestring
Source0:        https://static.crates.io/crates/widestring/widestring-%{version}.crate
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
Summary:        A wide string Rust library for converting to and from wide strings, s...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A wide string Rust library for converting to and from wide strings, s...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+debugger_visualizer-devel
Summary:        A wide string Rust library for converting to and from wide strings, s...
BuildArch:      noarch
%description -n %{name}+debugger_visualizer-devel

This package contains library source intended for building other packages which
use the "debugger_visualizer" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A wide string Rust library for converting to and from wide strings, s...
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
%files -n rust-widestring-devel -f %{oreon_filedir}/rust-widestring-devel.list

%changelog

%autochangelog
