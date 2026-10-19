%global source0_hash 95832e849adfb21180ccb6826a99da14e5d266ae5c2e668e1602cf234f153797
%bcond check 1
%global debug_package %{nil}
%global crate bytemuck
Name:           rust-bytemuck
Version:        1.25.2
Release:        1%{?dist}
Summary:        Muck around with piles of bytes
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/bytemuck
Source0:        https://static.crates.io/crates/bytemuck/bytemuck-%{version}.crate
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
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aarch64_simd-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+aarch64_simd-devel

This package contains library source intended for building other packages which
use the "aarch64_simd" feature of the "%{crate}" crate.

%package     -n %{name}+align_offset-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+align_offset-devel

This package contains library source intended for building other packages which
use the "align_offset" feature of the "%{crate}" crate.

%package     -n %{name}+alloc_uninit-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+alloc_uninit-devel

This package contains library source intended for building other packages which
use the "alloc_uninit" feature of the "%{crate}" crate.

%package     -n %{name}+avx512_simd-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+avx512_simd-devel

This package contains library source intended for building other packages which
use the "avx512_simd" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck_derive-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+bytemuck_derive-devel

This package contains library source intended for building other packages which
use the "bytemuck_derive" feature of the "%{crate}" crate.

%package     -n %{name}+const_zeroed-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+const_zeroed-devel

This package contains library source intended for building other packages which
use the "const_zeroed" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+extern_crate_alloc-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+extern_crate_alloc-devel

This package contains library source intended for building other packages which
use the "extern_crate_alloc" feature of the "%{crate}" crate.

%package     -n %{name}+extern_crate_std-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+extern_crate_std-devel

This package contains library source intended for building other packages which
use the "extern_crate_std" feature of the "%{crate}" crate.

%package     -n %{name}+impl_core_error-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+impl_core_error-devel

This package contains library source intended for building other packages which
use the "impl_core_error" feature of the "%{crate}" crate.

%package     -n %{name}+min_const_generics-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+min_const_generics-devel

This package contains library source intended for building other packages which
use the "min_const_generics" feature of the "%{crate}" crate.

%package     -n %{name}+must_cast-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+must_cast-devel

This package contains library source intended for building other packages which
use the "must_cast" feature of the "%{crate}" crate.

%package     -n %{name}+must_cast_extra-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+must_cast_extra-devel

This package contains library source intended for building other packages which
use the "must_cast_extra" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_stdsimd-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+nightly_stdsimd-devel

This package contains library source intended for building other packages which
use the "nightly_stdsimd" feature of the "%{crate}" crate.

%package     -n %{name}+track_caller-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+track_caller-devel

This package contains library source intended for building other packages which
use the "track_caller" feature of the "%{crate}" crate.

%package     -n %{name}+transparentwrapper_extra-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+transparentwrapper_extra-devel

This package contains library source intended for building other packages which
use the "transparentwrapper_extra" feature of the "%{crate}" crate.

%package     -n %{name}+unsound_ptr_pod_impl-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+unsound_ptr_pod_impl-devel

This package contains library source intended for building other packages which
use the "unsound_ptr_pod_impl" feature of the "%{crate}" crate.

%package     -n %{name}+zeroable_atomics-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+zeroable_atomics-devel

This package contains library source intended for building other packages which
use the "zeroable_atomics" feature of the "%{crate}" crate.

%package     -n %{name}+zeroable_maybe_uninit-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+zeroable_maybe_uninit-devel

This package contains library source intended for building other packages which
use the "zeroable_maybe_uninit" feature of the "%{crate}" crate.

%package     -n %{name}+zeroable_unwind_fn-devel
Summary:        Muck around with piles of bytes
BuildArch:      noarch
%description -n %{name}+zeroable_unwind_fn-devel

This package contains library source intended for building other packages which
use the "zeroable_unwind_fn" feature of the "%{crate}" crate.

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
%files -n rust-bytemuck-devel -f %{oreon_filedir}/rust-bytemuck-devel.list

%changelog

%autochangelog
