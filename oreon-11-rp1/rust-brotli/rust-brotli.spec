%global source0_hash 5cc91aac060a7a1e25823bdccbfb6af1875b88f17c6daac97894eed8207166b3
%bcond check 0
%global debug_package %{nil}
%global crate brotli
Name:           rust-brotli
Version:        8.0.4
Release:        1%{?dist}
Summary:        A brotli compressor and decompressor that with an interface avoiding...
License:        BSD-3-Clause AND MIT
URL:            https://crates.io/crates/brotli
Source0:        https://static.crates.io/crates/brotli/brotli-%{version}.crate
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
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-stdlib-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+alloc-stdlib-devel

This package contains library source intended for building other packages which
use the "alloc-stdlib" feature of the "%{crate}" crate.

%package     -n %{name}+benchmark-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+benchmark-devel

This package contains library source intended for building other packages which
use the "benchmark" feature of the "%{crate}" crate.

%package     -n %{name}+billing-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+billing-devel

This package contains library source intended for building other packages which
use the "billing" feature of the "%{crate}" crate.

%package     -n %{name}+disable-timer-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+disable-timer-devel

This package contains library source intended for building other packages which
use the "disable-timer" feature of the "%{crate}" crate.

%package     -n %{name}+disallow_large_window_size-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+disallow_large_window_size-devel

This package contains library source intended for building other packages which
use the "disallow_large_window_size" feature of the "%{crate}" crate.

%package     -n %{name}+external-literal-probability-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+external-literal-probability-devel

This package contains library source intended for building other packages which
use the "external-literal-probability" feature of the "%{crate}" crate.

%package     -n %{name}+ffi-api-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+ffi-api-devel

This package contains library source intended for building other packages which
use the "ffi-api" feature of the "%{crate}" crate.

%package     -n %{name}+float64-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+float64-devel

This package contains library source intended for building other packages which
use the "float64" feature of the "%{crate}" crate.

%package     -n %{name}+floating_point_context_mixing-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+floating_point_context_mixing-devel

This package contains library source intended for building other packages which
use the "floating_point_context_mixing" feature of the "%{crate}" crate.

%package     -n %{name}+no-stdlib-ffi-binding-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+no-stdlib-ffi-binding-devel

This package contains library source intended for building other packages which
use the "no-stdlib-ffi-binding" feature of the "%{crate}" crate.

%package     -n %{name}+pass-through-ffi-panics-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+pass-through-ffi-panics-devel

This package contains library source intended for building other packages which
use the "pass-through-ffi-panics" feature of the "%{crate}" crate.

%package     -n %{name}+seccomp-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+seccomp-devel

This package contains library source intended for building other packages which
use the "seccomp" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+validation-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+validation-devel

This package contains library source intended for building other packages which
use the "validation" feature of the "%{crate}" crate.

%package     -n %{name}+vector_scratch_space-devel
Summary:        A brotli compressor and decompressor that with an interface avoiding...
BuildArch:      noarch
%description -n %{name}+vector_scratch_space-devel

This package contains library source intended for building other packages which
use the "vector_scratch_space" feature of the "%{crate}" crate.

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
%files -n rust-brotli-devel -f %{oreon_filedir}/rust-brotli-devel.list

%changelog

%autochangelog
