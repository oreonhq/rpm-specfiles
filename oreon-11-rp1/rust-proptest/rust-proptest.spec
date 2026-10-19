%global source0_hash 4b45fcc2344c680f5025fe57779faef368840d0bd1f42f216291f0dc4ace4744
%bcond check 0
%global debug_package %{nil}
%global crate proptest
Name:           rust-proptest
Version:        1.11.0
Release:        1%{?dist}
Summary:        Hypothesis-like property-based testing and shrinking.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proptest
Source0:        https://static.crates.io/crates/proptest/proptest-%{version}.crate
Patch:          proptest-fix-metadata-auto.diff
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
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+atomic64bit-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+atomic64bit-devel

This package contains library source intended for building other packages which
use the "atomic64bit" feature of the "%{crate}" crate.

%package     -n %{name}+attr-macro-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+attr-macro-devel

This package contains library source intended for building other packages which
use the "attr-macro" feature of the "%{crate}" crate.

%package     -n %{name}+bit-set-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+bit-set-devel

This package contains library source intended for building other packages which
use the "bit-set" feature of the "%{crate}" crate.

%package     -n %{name}+default-code-coverage-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+default-code-coverage-devel

This package contains library source intended for building other packages which
use the "default-code-coverage" feature of the "%{crate}" crate.

%package     -n %{name}+f16-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+f16-devel

This package contains library source intended for building other packages which
use the "f16" feature of the "%{crate}" crate.

%package     -n %{name}+fork-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+fork-devel

This package contains library source intended for building other packages which
use the "fork" feature of the "%{crate}" crate.

%package     -n %{name}+handle-panics-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+handle-panics-devel

This package contains library source intended for building other packages which
use the "handle-panics" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-macro-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+proptest-macro-devel

This package contains library source intended for building other packages which
use the "proptest-macro" feature of the "%{crate}" crate.

%package     -n %{name}+regex-syntax-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+regex-syntax-devel

This package contains library source intended for building other packages which
use the "regex-syntax" feature of the "%{crate}" crate.

%package     -n %{name}+rusty-fork-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+rusty-fork-devel

This package contains library source intended for building other packages which
use the "rusty-fork" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tempfile-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+tempfile-devel

This package contains library source intended for building other packages which
use the "tempfile" feature of the "%{crate}" crate.

%package     -n %{name}+timeout-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+timeout-devel

This package contains library source intended for building other packages which
use the "timeout" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Hypothesis-like property-based testing and shrinking.
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-proptest-devel -f %{oreon_filedir}/rust-proptest-devel.list

%changelog

%autochangelog
