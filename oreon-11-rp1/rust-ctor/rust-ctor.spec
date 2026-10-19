%global source0_hash 914a755b7c2d4af2bdcff7ce1739e2db9a1b81a9b07123d8015786ae03c0980d
%bcond check 0
%global debug_package %{nil}
%global crate ctor
Name:           rust-ctor
Version:        1.0.13
Release:        1%{?dist}
Summary:        Global, no_std-compatible constructors for all platforms that run bef...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ctor
Source0:        https://static.crates.io/crates/ctor/ctor-%{version}.crate
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
Summary:        Global, no_std-compatible constructors for all platforms that run bef...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+priority-devel
Summary:        Global, no_std-compatible constructors for all platforms that run bef...
BuildArch:      noarch
%description -n %{name}+priority-devel

This package contains library source intended for building other packages which
use the "priority" feature of the "%{crate}" crate.

%package     -n %{name}+proc_macro-devel
Summary:        Global, no_std-compatible constructors for all platforms that run bef...
BuildArch:      noarch
%description -n %{name}+proc_macro-devel

This package contains library source intended for building other packages which
use the "proc_macro" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Global, no_std-compatible constructors for all platforms that run bef...
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
%files -n rust-ctor-devel -f %{oreon_filedir}/rust-ctor-devel.list

%changelog

%autochangelog
