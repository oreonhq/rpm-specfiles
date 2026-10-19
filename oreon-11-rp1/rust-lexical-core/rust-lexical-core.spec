%global source0_hash 6607c62aa161d23d17a9072cc5da0be67cdfc89d3afb1e8d9c842bebc2525ffe
%bcond check 0
%global debug_package %{nil}
%global crate lexical-core
Name:           rust-lexical-core
Version:        0.7.6
Release:        1%{?dist}
Summary:        Lexical, to- and from-string conversion routines.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lexical-core
Source0:        https://static.crates.io/crates/lexical-core/lexical-core-%{version}.crate
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
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+correct-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+correct-devel

This package contains library source intended for building other packages which
use the "correct" feature of the "%{crate}" crate.

%package     -n %{name}+dtoa-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+dtoa-devel

This package contains library source intended for building other packages which
use the "dtoa" feature of the "%{crate}" crate.

%package     -n %{name}+format-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+format-devel

This package contains library source intended for building other packages which
use the "format" feature of the "%{crate}" crate.

%package     -n %{name}+grisu3-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+grisu3-devel

This package contains library source intended for building other packages which
use the "grisu3" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+noinline-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+noinline-devel

This package contains library source intended for building other packages which
use the "noinline" feature of the "%{crate}" crate.

%package     -n %{name}+property_tests-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+property_tests-devel

This package contains library source intended for building other packages which
use the "property_tests" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+radix-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+radix-devel

This package contains library source intended for building other packages which
use the "radix" feature of the "%{crate}" crate.

%package     -n %{name}+rounding-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+rounding-devel

This package contains library source intended for building other packages which
use the "rounding" feature of the "%{crate}" crate.

%package     -n %{name}+ryu-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+ryu-devel

This package contains library source intended for building other packages which
use the "ryu" feature of the "%{crate}" crate.

%package     -n %{name}+static_assertions-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+static_assertions-devel

This package contains library source intended for building other packages which
use the "static_assertions" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+table-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+table-devel

This package contains library source intended for building other packages which
use the "table" feature of the "%{crate}" crate.

%package     -n %{name}+trim_floats-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+trim_floats-devel

This package contains library source intended for building other packages which
use the "trim_floats" feature of the "%{crate}" crate.

%package     -n %{name}+unchecked_index-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+unchecked_index-devel

This package contains library source intended for building other packages which
use the "unchecked_index" feature of the "%{crate}" crate.

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
%files -n rust-lexical-core-devel -f %{oreon_filedir}/rust-lexical-core-devel.list

%changelog

%autochangelog
