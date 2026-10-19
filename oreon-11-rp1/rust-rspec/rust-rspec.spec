%global source0_hash 89389e7c690310e855df3d9b507985ca0d323e2e766b2fedf369b02671e70e0a
%bcond check 0
%global debug_package %{nil}
%global crate rspec
Name:           rust-rspec
Version:        1.0.0
Release:        1%{?dist}
Summary:        Write Rspec-like tests with stable rust
License:        MPL-2.0
URL:            https://crates.io/crates/rspec
Source0:        https://static.crates.io/crates/rspec/rspec-%{version}.crate
Patch:          rspec-fix-metadata.diff
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
Summary:        Write Rspec-like tests with stable rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-rspec-devel -f %{oreon_filedir}/rust-rspec-devel.list

%changelog

%autochangelog
