%global source0_hash 2604dd126bb14f13fb5d1bd6a66155079cb9fa655b37f875b3a742c705dbed17
%bcond check 0
%global debug_package %{nil}
%global crate lexical-util
Name:           rust-lexical-util
Version:        1.0.7
Release:        1%{?dist}
Summary:        Shared utilities for lexical creates.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lexical-util
Source0:        https://static.crates.io/crates/lexical-util/lexical-util-%{version}.crate
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
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+compact-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+compact-devel

This package contains library source intended for building other packages which
use the "compact" feature of the "%{crate}" crate.

%package     -n %{name}+f128-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+f128-devel

This package contains library source intended for building other packages which
use the "f128" feature of the "%{crate}" crate.

%package     -n %{name}+f16-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+f16-devel

This package contains library source intended for building other packages which
use the "f16" feature of the "%{crate}" crate.

%package     -n %{name}+float16-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+float16-devel

This package contains library source intended for building other packages which
use the "float16" feature of the "%{crate}" crate.

%package     -n %{name}+format-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+format-devel

This package contains library source intended for building other packages which
use the "format" feature of the "%{crate}" crate.

%package     -n %{name}+lint-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+lint-devel

This package contains library source intended for building other packages which
use the "lint" feature of the "%{crate}" crate.

%package     -n %{name}+parse-floats-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+parse-floats-devel

This package contains library source intended for building other packages which
use the "parse-floats" feature of the "%{crate}" crate.

%package     -n %{name}+parse-integers-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+parse-integers-devel

This package contains library source intended for building other packages which
use the "parse-integers" feature of the "%{crate}" crate.

%package     -n %{name}+power-of-two-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+power-of-two-devel

This package contains library source intended for building other packages which
use the "power-of-two" feature of the "%{crate}" crate.

%package     -n %{name}+radix-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+radix-devel

This package contains library source intended for building other packages which
use the "radix" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+write-floats-devel
Summary:        Shared utilities for lexical creates.
BuildArch:      noarch
%description -n %{name}+write-floats-devel

This package contains library source intended for building other packages which
use the "write-floats" feature of the "%{crate}" crate.

%package     -n %{name}+write-integers-devel
Summary:        Shared utilities for lexical creates.
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
%files -n rust-lexical-util-devel -f %{oreon_filedir}/rust-lexical-util-devel.list

%changelog

%autochangelog
