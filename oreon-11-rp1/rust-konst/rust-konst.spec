%global source0_hash 128133ed7824fcd73d6e7b17957c5eb7bacb885649bd8c69708b2331a10bcefb
%bcond check 0
%global debug_package %{nil}
%global crate konst
Name:           rust-konst
Version:        0.2.20
Release:        1%{?dist}
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
License:        Zlib
URL:            https://crates.io/crates/konst
Source0:        https://static.crates.io/crates/konst/konst-%{version}.crate
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
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__test-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+__test-devel

This package contains library source intended for building other packages which
use the "__test" feature of the "%{crate}" crate.

%package     -n %{name}+__ui-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+__ui-devel

This package contains library source intended for building other packages which
use the "__ui" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+cmp-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+cmp-devel

This package contains library source intended for building other packages which
use the "cmp" feature of the "%{crate}" crate.

%package     -n %{name}+const_generics-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+const_generics-devel

This package contains library source intended for building other packages which
use the "const_generics" feature of the "%{crate}" crate.

%package     -n %{name}+constant_time_slice-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+constant_time_slice-devel

This package contains library source intended for building other packages which
use the "constant_time_slice" feature of the "%{crate}" crate.

%package     -n %{name}+deref_raw_in_fn-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+deref_raw_in_fn-devel

This package contains library source intended for building other packages which
use the "deref_raw_in_fn" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+konst_proc_macros-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+konst_proc_macros-devel

This package contains library source intended for building other packages which
use the "konst_proc_macros" feature of the "%{crate}" crate.

%package     -n %{name}+mut_refs-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+mut_refs-devel

This package contains library source intended for building other packages which
use the "mut_refs" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_mut_refs-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+nightly_mut_refs-devel

This package contains library source intended for building other packages which
use the "nightly_mut_refs" feature of the "%{crate}" crate.

%package     -n %{name}+parsing-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+parsing-devel

This package contains library source intended for building other packages which
use the "parsing" feature of the "%{crate}" crate.

%package     -n %{name}+parsing_no_proc-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+parsing_no_proc-devel

This package contains library source intended for building other packages which
use the "parsing_no_proc" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_51-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+rust_1_51-devel

This package contains library source intended for building other packages which
use the "rust_1_51" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_55-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+rust_1_55-devel

This package contains library source intended for building other packages which
use the "rust_1_55" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_56-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+rust_1_56-devel

This package contains library source intended for building other packages which
use the "rust_1_56" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_57-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+rust_1_57-devel

This package contains library source intended for building other packages which
use the "rust_1_57" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_61-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+rust_1_61-devel

This package contains library source intended for building other packages which
use the "rust_1_61" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_64-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+rust_1_64-devel

This package contains library source intended for building other packages which
use the "rust_1_64" feature of the "%{crate}" crate.

%package     -n %{name}+rust_latest_stable-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+rust_latest_stable-devel

This package contains library source intended for building other packages which
use the "rust_latest_stable" feature of the "%{crate}" crate.

%package     -n %{name}+trybuild-devel
Summary:        Const equivalents of std functions, compile-time comparison, and parsing
BuildArch:      noarch
%description -n %{name}+trybuild-devel

This package contains library source intended for building other packages which
use the "trybuild" feature of the "%{crate}" crate.

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
%files -n rust-konst-devel -f %{oreon_filedir}/rust-konst-devel.list

%changelog

%autochangelog
