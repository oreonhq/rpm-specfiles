%global source0_hash 68354c5c6bd36d73ff3feceb05efa59b6acb7626617f4962be322a825e61f79a
%bcond check 0
%global debug_package %{nil}
%global crate minimal-lexical
Name:           rust-minimal-lexical
Version:        0.2.1
Release:        1%{?dist}
Summary:        Fast float parsing conversion routines.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/minimal-lexical
Source0:        https://static.crates.io/crates/minimal-lexical/minimal-lexical-%{version}.crate
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
Summary:        Fast float parsing conversion routines.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Fast float parsing conversion routines.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+compact-devel
Summary:        Fast float parsing conversion routines.
BuildArch:      noarch
%description -n %{name}+compact-devel

This package contains library source intended for building other packages which
use the "compact" feature of the "%{crate}" crate.

%package     -n %{name}+lint-devel
Summary:        Fast float parsing conversion routines.
BuildArch:      noarch
%description -n %{name}+lint-devel

This package contains library source intended for building other packages which
use the "lint" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Fast float parsing conversion routines.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast float parsing conversion routines.
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
%files -n rust-minimal-lexical-devel -f %{oreon_filedir}/rust-minimal-lexical-devel.list

%changelog

%autochangelog
