%global source0_hash e5a2455608f6a56fc2ce66c89dd005501c169688f29165468e65f0b47e060333
%bcond check 1
%global debug_package %{nil}
%global crate test-tag
Name:           rust-test-tag
Version:        0.1.6
Release:        1%{?dist}
Summary:        #[tag] attribute for convenient tagging/grouping of #[test] tests
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/test-tag
Source0:        https://static.crates.io/crates/test-tag/test-tag-%{version}.crate
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
Summary:        #[tag] attribute for convenient tagging/grouping of #[test] tests
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
%files -n rust-test-tag-devel -f %{oreon_filedir}/rust-test-tag-devel.list

%changelog

%autochangelog
