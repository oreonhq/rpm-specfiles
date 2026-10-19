%global source0_hash 5fe242ee9e646acec9ab73a5c540e8543ed1b107f0ce42be831e0775d423c396
%bcond check 1
%global debug_package %{nil}
%global crate tryfn
Name:           rust-tryfn0.2
Version:        0.2.3
Release:        1%{?dist}
Summary:        File-driven snapshot testing for a function
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tryfn
Source0:        https://static.crates.io/crates/tryfn/tryfn-%{version}.crate
Patch:          tryfn-fix-metadata.diff
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
Summary:        File-driven snapshot testing for a function
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        File-driven snapshot testing for a function
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+color-auto-devel
Summary:        File-driven snapshot testing for a function
BuildArch:      noarch
%description -n %{name}+color-auto-devel

This package contains library source intended for building other packages which
use the "color-auto" feature of the "%{crate}" crate.

%package     -n %{name}+diff-devel
Summary:        File-driven snapshot testing for a function
BuildArch:      noarch
%description -n %{name}+diff-devel

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

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
%files -n rust-tryfn0.2-devel -f %{oreon_filedir}/rust-tryfn0.2-devel.list

%changelog

%autochangelog
