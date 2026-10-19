%global source0_hash 7d8d125a277f807e55a77304455eb7b1cb52f2b18c143b60e766c120bd64a594
%bcond check 0
%global debug_package %{nil}
%global crate lexical-core
Name:           rust-lexical-core1
Version:        1.0.6
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

%package     -n %{name}+compact-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+compact-devel

This package contains library source intended for building other packages which
use the "compact" feature of the "%{crate}" crate.

%package     -n %{name}+f128-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+f128-devel

This package contains library source intended for building other packages which
use the "f128" feature of the "%{crate}" crate.

%package     -n %{name}+f16-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+f16-devel

This package contains library source intended for building other packages which
use the "f16" feature of the "%{crate}" crate.

%package     -n %{name}+floats-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+floats-devel

This package contains library source intended for building other packages which
use the "floats" feature of the "%{crate}" crate.

%package     -n %{name}+format-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+format-devel

This package contains library source intended for building other packages which
use the "format" feature of the "%{crate}" crate.

%package     -n %{name}+integers-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+integers-devel

This package contains library source intended for building other packages which
use the "integers" feature of the "%{crate}" crate.

%package     -n %{name}+lexical-parse-float-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+lexical-parse-float-devel

This package contains library source intended for building other packages which
use the "lexical-parse-float" feature of the "%{crate}" crate.

%package     -n %{name}+lexical-parse-integer-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+lexical-parse-integer-devel

This package contains library source intended for building other packages which
use the "lexical-parse-integer" feature of the "%{crate}" crate.

%package     -n %{name}+lexical-write-float-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+lexical-write-float-devel

This package contains library source intended for building other packages which
use the "lexical-write-float" feature of the "%{crate}" crate.

%package     -n %{name}+lexical-write-integer-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+lexical-write-integer-devel

This package contains library source intended for building other packages which
use the "lexical-write-integer" feature of the "%{crate}" crate.

%package     -n %{name}+lint-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+lint-devel

This package contains library source intended for building other packages which
use the "lint" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+parse-floats-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+parse-floats-devel

This package contains library source intended for building other packages which
use the "parse-floats" feature of the "%{crate}" crate.

%package     -n %{name}+parse-integers-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+parse-integers-devel

This package contains library source intended for building other packages which
use the "parse-integers" feature of the "%{crate}" crate.

%package     -n %{name}+power-of-two-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+power-of-two-devel

This package contains library source intended for building other packages which
use the "power-of-two" feature of the "%{crate}" crate.

%package     -n %{name}+radix-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+radix-devel

This package contains library source intended for building other packages which
use the "radix" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+write-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+write-devel

This package contains library source intended for building other packages which
use the "write" feature of the "%{crate}" crate.

%package     -n %{name}+write-floats-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+write-floats-devel

This package contains library source intended for building other packages which
use the "write-floats" feature of the "%{crate}" crate.

%package     -n %{name}+write-integers-devel
Summary:        Lexical, to- and from-string conversion routines.
BuildArch:      noarch
%description -n %{name}+write-integers-devel

This package contains library source intended for building other packages which
use the "write-integers" feature of the "%{crate}" crate.

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
%files -n rust-lexical-core1-devel -f %{oreon_filedir}/rust-lexical-core1-devel.list

%changelog

%autochangelog
