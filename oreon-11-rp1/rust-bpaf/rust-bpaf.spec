%global source0_hash 473976d7a8620bb1e06dcdd184407c2363fe4fec8e983ee03ed9197222634a31
%bcond check 1
%global debug_package %{nil}
%global crate bpaf
Name:           rust-bpaf
Version:        0.9.20
Release:        1%{?dist}
Summary:        Simple Command Line Argument Parser with parser combinators
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bpaf
Source0:        https://static.crates.io/crates/bpaf/bpaf-%{version}.crate
Patch:          0001-use-correct-import-statement-to-fix-compilation-of-t.patch
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
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+autocomplete-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+autocomplete-devel

This package contains library source intended for building other packages which
use the "autocomplete" feature of the "%{crate}" crate.

%package     -n %{name}+batteries-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+batteries-devel

This package contains library source intended for building other packages which
use the "batteries" feature of the "%{crate}" crate.

%package     -n %{name}+bpaf_derive-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+bpaf_derive-devel

This package contains library source intended for building other packages which
use the "bpaf_derive" feature of the "%{crate}" crate.

%package     -n %{name}+bright-color-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+bright-color-devel

This package contains library source intended for building other packages which
use the "bright-color" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+docgen-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+docgen-devel

This package contains library source intended for building other packages which
use the "docgen" feature of the "%{crate}" crate.

%package     -n %{name}+dull-color-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+dull-color-devel

This package contains library source intended for building other packages which
use the "dull-color" feature of the "%{crate}" crate.

%package     -n %{name}+extradocs-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+extradocs-devel

This package contains library source intended for building other packages which
use the "extradocs" feature of the "%{crate}" crate.

%package     -n %{name}+owo-colors-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+owo-colors-devel

This package contains library source intended for building other packages which
use the "owo-colors" feature of the "%{crate}" crate.

%package     -n %{name}+supports-color-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+supports-color-devel

This package contains library source intended for building other packages which
use the "supports-color" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-docs-devel
Summary:        Simple Command Line Argument Parser with parser combinators
BuildArch:      noarch
%description -n %{name}+unstable-docs-devel

This package contains library source intended for building other packages which
use the "unstable-docs" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f autocomplete,derive
%install
%cargo_install -f autocomplete,derive
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f autocomplete,derive -- -- --exact --skip buffer::splitter::ticks_code_block
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-bpaf-devel -f %{oreon_filedir}/rust-bpaf-devel.list

%changelog

%autochangelog
