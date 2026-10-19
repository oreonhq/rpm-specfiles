%global source0_hash 7d9334f725b46fb9bed8580b9b47a932587e044fadb344ed7fa98774b067ac1a
%bcond check 1
%global debug_package %{nil}
%global crate clircle
Name:           rust-clircle
Version:        0.6.1
Release:        1%{?dist}
Summary:        Detect IO circles in your CLI apps arguments
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clircle
Source0:        https://static.crates.io/crates/clircle/clircle-%{version}.crate
Patch:          clircle-fix-metadata-auto.diff
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
Summary:        Detect IO circles in your CLI apps arguments
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Detect IO circles in your CLI apps arguments
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+test-close-again-devel
Summary:        Detect IO circles in your CLI apps arguments
BuildArch:      noarch
%description -n %{name}+test-close-again-devel

This package contains library source intended for building other packages which
use the "test-close-again" feature of the "%{crate}" crate.

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
%files -n rust-clircle-devel -f %{oreon_filedir}/rust-clircle-devel.list

%changelog

%autochangelog
