%global source0_hash 439ee305def115ba05938db6eb1644ff94165c5ab5e9420d1c1bcedbba909391
%bcond check 0
%global debug_package %{nil}
%global crate powerfmt
Name:           rust-powerfmt
Version:        0.2.0
Release:        1%{?dist}
Summary:        `powerfmt` is a library that provides utilities for formatting values...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/powerfmt
Source0:        https://static.crates.io/crates/powerfmt/powerfmt-%{version}.crate
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
Summary:        `powerfmt` is a library that provides utilities for formatting values...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        `powerfmt` is a library that provides utilities for formatting values...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        `powerfmt` is a library that provides utilities for formatting values...
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        `powerfmt` is a library that provides utilities for formatting values...
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
%files -n rust-powerfmt-devel -f %{oreon_filedir}/rust-powerfmt-devel.list

%changelog

%autochangelog
