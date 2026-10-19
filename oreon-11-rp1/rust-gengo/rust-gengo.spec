%global source0_hash 8ebd89f06047f610e79838ea0f8972400e3e3fae96b3abbe2d10927475540b2e
%bcond check 1
%global debug_package %{nil}
%global crate gengo
Name:           rust-gengo
Version:        0.15.0
Release:        1%{?dist}
Summary:        Get the language distribution stats of your repository
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gengo
Source0:        https://static.crates.io/crates/gengo/gengo-%{version}.crate
Patch:          gengo-fix-metadata.diff
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
Summary:        Get the language distribution stats of your repository
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+directory-devel
Summary:        Get the language distribution stats of your repository
BuildArch:      noarch
%description -n %{name}+directory-devel

This package contains library source intended for building other packages which
use the "directory" feature of the "%{crate}" crate.

%package     -n %{name}+git-devel
Summary:        Get the language distribution stats of your repository
BuildArch:      noarch
%description -n %{name}+git-devel

This package contains library source intended for building other packages which
use the "git" feature of the "%{crate}" crate.

%package     -n %{name}+max-performance-devel
Summary:        Get the language distribution stats of your repository
BuildArch:      noarch
%description -n %{name}+max-performance-devel

This package contains library source intended for building other packages which
use the "max-performance" feature of the "%{crate}" crate.

%package     -n %{name}+max-performance-safe-devel
Summary:        Get the language distribution stats of your repository
BuildArch:      noarch
%description -n %{name}+max-performance-safe-devel

This package contains library source intended for building other packages which
use the "max-performance-safe" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip test_git_javascript
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-gengo-devel -f %{oreon_filedir}/rust-gengo-devel.list

%changelog

%autochangelog
