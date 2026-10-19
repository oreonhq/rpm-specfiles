%global source0_hash 3a32acac15fe1967bc3986b2a6347dffc965602354ea6f450ad07e8bfd253583
%bcond check 0
%global debug_package %{nil}
%global crate brotli-decompressor
Name:           rust-brotli-decompressor
Version:        5.0.3
Release:        1%{?dist}
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
License:        BSD-3-Clause OR MIT
URL:            https://crates.io/crates/brotli-decompressor
Source0:        https://static.crates.io/crates/brotli-decompressor/brotli-decompressor-%{version}.crate
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
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-stdlib-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+alloc-stdlib-devel

This package contains library source intended for building other packages which
use the "alloc-stdlib" feature of the "%{crate}" crate.

%package     -n %{name}+benchmark-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+benchmark-devel

This package contains library source intended for building other packages which
use the "benchmark" feature of the "%{crate}" crate.

%package     -n %{name}+disable-timer-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+disable-timer-devel

This package contains library source intended for building other packages which
use the "disable-timer" feature of the "%{crate}" crate.

%package     -n %{name}+ffi-api-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+ffi-api-devel

This package contains library source intended for building other packages which
use the "ffi-api" feature of the "%{crate}" crate.

%package     -n %{name}+pass-through-ffi-panics-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+pass-through-ffi-panics-devel

This package contains library source intended for building other packages which
use the "pass-through-ffi-panics" feature of the "%{crate}" crate.

%package     -n %{name}+seccomp-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+seccomp-devel

This package contains library source intended for building other packages which
use the "seccomp" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-devel
Summary:        A brotli decompressor that with an interface avoiding the rust stdlib...
BuildArch:      noarch
%description -n %{name}+unsafe-devel

This package contains library source intended for building other packages which
use the "unsafe" feature of the "%{crate}" crate.

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
%files -n rust-brotli-decompressor-devel -f %{oreon_filedir}/rust-brotli-decompressor-devel.list

%changelog

%autochangelog
